# Perplexity Query API

This project is a simple server that runs on Node.js and uses Express to create an HTTP API for querying the [perplexity.ai](https://perplexity.ai) website. It uses Puppeteer for browser automation to interact with the website and fetch answers to user's questions. The server exposes a `/query` endpoint that accepts JSON POST requests with a `prompt` field.

## Prerequisites

- Node.js (v14.0.0 or higher)
- npm (v6.14.0 or higher)

## Installation

1. Clone the repository or download the source code.

```bash
git clone https://github.com/your-repo-url/perplexity-query-api
```

2. Navigate to the project directory.

```bash
cd perplexity-query-api
```

3. Install the required dependencies.

```bash
npm install
```

## Usage

1. Run the server using `ts-node`:

```bash
npx ts-node app.ts
```

The server will start at `http://localhost:3000` by default.

2. Send a POST request to the `/query` endpoint with a JSON payload that includes a `prompt` field. For example:

```bash
curl -X POST -H "Content-Type: application/json" -d '{ "prompt": "What is the capital of France?" }' http://localhost:3000/query
```

Alternatively, you can use tools like [Postman](https://www.postman.com/) or create a simple HTML form to interact with the `/query` endpoint.

3. The server will respond with a JSON object containing the status, status text, and the fetched content (answer) from perplexity.ai.

## License

This project is licensed under the [MIT License](http://opensource.org/licenses/MIT). See the [LICENSE](LICENSE) file for the full license text.
