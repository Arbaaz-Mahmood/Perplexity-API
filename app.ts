import puppeteer from 'puppeteer';
import express from 'express';

async function fetch_perplexity(
  prompt: string
): Promise<{ status: number; statusText: string; content: any }> {
  try {
    console.log('Launching browser...');
    const browser = await puppeteer.launch();

    console.log('Opening new page...');
    const page = await browser.newPage();

    const url = 'https://perplexity.ai';
    console.log(`Navigating to URL: ${url}...`);
    await page.goto(url);

    console.log('Entering query...');
    const searchBoxSelector = 'textarea[placeholder="Ask anything..."]';
    await page.type(searchBoxSelector, prompt);
    await page.keyboard.press('Enter');

    // Add a delay (e.g., 5 seconds) before starting extraction
    await new Promise((r) => setTimeout(r, 10000));

    const responseSelector = '.prose';
    await page.waitForSelector(responseSelector);

    // Get the last element's inner HTML
    const elements = await page.$$(responseSelector);
    const element = elements[elements.length - 1];
    const innerHtml = await page.evaluate(
      (element) => element.innerHTML,
      element
    );

    // Parse the HTML to extract text from <span> elements
    const content = await page.evaluate((innerHtml) => {
      const parser = new DOMParser();
      const doc = parser.parseFromString(innerHtml, 'text/html');
      const spans = doc.querySelectorAll('span');
      return Array.from(spans)
        .map((span) => span.textContent)
        .join(' ');
    }, innerHtml);

    console.log('Closing browser...');
    await browser.close();
    console.log(`Fetch complete. Status: 200, Content: ${content}`);
    return { status: 200, statusText: 'OK', content: content };
  } catch (error: any) {
    console.error(`Error during fetch: ${error.message}`);
    return { status: 500, statusText: error.message, content: null };
  }
}

const app = express();
app.use(express.json());

app.post('/query', async (req, res) => {
  const { prompt } = req.body;
  if (!prompt) {
    res.status(400).send({ status: 400, statusText: 'Bad Request', content: 'Missing prompt' });
    return;
  }

  try {
    const result = await fetch_perplexity(prompt);
    res.send(result);
  } catch (error) {
    res.status(500).send({ status: 500, statusText: 'Internal Server Error', content: error.message });
  }
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});
