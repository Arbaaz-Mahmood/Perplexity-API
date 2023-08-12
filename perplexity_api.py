import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

class PerplexityAPI:
    def __init__(
            self,
            headless=True,
            user_agent=None,
            stealth=True,
            incognito=False,
            user_data_dir=None,
            proxy=None,
            timeout=30.0,
            response_timeout=60.0
    ):
        options = Options()
        # Other option settings...

        chrome_driver_path = ChromeDriverManager("112.0.5615.137").install()
        chrome_driver_service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=chrome_driver_service, options=options)

        self.timeout = timeout
        self.response_timeout = response_timeout

    def query(self, prompt):
        logging.info("Starting query function")

        self.driver.get("https://perplexity.ai")
        logging.info("Navigated to perplexity.ai")

        search_box = self.driver.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Ask anything..."]')
        search_box.send_keys(prompt)
        search_box.send_keys(Keys.ENTER)

        logging.info(f"Submitted query: {prompt}")
        time.sleep(10)  # Adjust the delay time as needed

        response_selector = '.prose'
        # Wait for the presence of the specific selector
        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, response_selector))
        )

        # Get all elements matching the selector
        elements = self.driver.find_elements(By.CSS_SELECTOR, response_selector)

        # Get the last element's inner HTML
        element = elements[-1]
        inner_html = element.get_attribute('innerHTML')
        

        # You can convert the HTML to Markdown here if needed
        # response = markdownify(inner_html)  # Assuming you have a markdownify function

        self.driver.quit()

        # Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(inner_html, 'html.parser')

        # Extract text from all <span> elements
        span_texts = [span.text for span in soup.find_all('span')]

        # Join the texts together, or process them as needed
        response = ' '.join(span_texts)

        logging.info("Query processed successfully")
        print(response)  # Print the response to the console
        return response  # Return the response

        logging.info("Query processed successfully")
        print(inner_html)  # Print the HTML content to the console
        return inner_html  # Return the HTML content

    def quit(self):
        self.driver.quit()


def test():
    query_text = input("Enter Your Question: ")
    
    # Create an instance of the PerplexityAPI class
    ppl = PerplexityAPI()

    # Call the query method for the provided query_text
    results = ppl.query(query_text)
    
    print(results)

if __name__ == "__main__":
    test()
