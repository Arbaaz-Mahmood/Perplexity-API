# Perplexity Query API

This project offers both a TypeScript server (Node.js and Express) and a Python script to query the [perplexity.ai](https://perplexity.ai) website and fetch answers to user's questions. Both implementations use browser automation: the TypeScript server uses Puppeteer, while the Python script uses Selenium.

## Prerequisites

- Node.js (v14.0.0 or higher) and npm (v6.14.0 or higher) for TypeScript server
- Python (3.6 or higher) for Python script

## TypeScript Server Installation and Usage

1. Clone the repository or download the source code.

```bash
git clone [https://github.com/your-repo-url/perplexity-query-api](https://github.com/Arbaaz-Mahmood/Perplexity-API.git)
```

2. Navigate to the project directory.

```bash
cd perplexity-query-api
```

3. Install the required dependencies.

```bash
npm install
```

4. Run the server using `ts-node`:

```bash
npx ts-node app.ts
```

The server will start at `http://localhost:3000` by default. Users can send a POST request to the `/query` endpoint with a JSON payload that includes a `prompt` field.

## Python Script Installation and Usage

1. Install the required Python packages:

```bash
pip install selenium beautifulsoup4 webdriver-manager
```

2. Install ChromeDriver:

- **macOS**:
  - You can use Homebrew to install ChromeDriver: `brew install chromedriver`
  - Make sure the installed ChromeDriver is in your `PATH` environment variable.
- **Windows**:
  - Download ChromeDriver from the [official site](https://sites.google.com/a/chromium.org/chromedriver/downloads).
  - Extract the executable and add the folder containing the executable to your `PATH` environment variable.
- **Linux**:
  - Use the package manager for your distribution to install ChromeDriver.
  - For example, on Ubuntu-based systems: `sudo apt-get install chromium-chromedriver`
  - Make sure the installed ChromeDriver is in your `PATH` environment variable.

3. Run the `perplexity_query.py` script:

```bash
python perplexity_query.py
```

The Python script will prompt for a question, interact with the perplexity.ai website, and print the response to the console.

## License

This project is licensed under the [MIT License](http://opensource.org/licenses/MIT). See the [LICENSE](LICENSE) file for the full license text.
