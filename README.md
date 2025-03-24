# Scrap-Brows

## WebScraperAi

An **AI-powered web scraper** using **Browser Use**, **LangChain**, and **Anthropic Claude** to autonomously navigate websites, search for AI-related news, and extract structured data.

## Features

✅ **Autonomous Web Browsing** – The agent can open multiple tabs and navigate dynamically.
✅ **LLM-Powered Processing** – Uses **Anthropic Claude** for intelligent decision-making.
✅ **Async Execution** – Optimized with `asyncio` for better performance.
✅ **Structured Data Extraction** – Outputs data in a clean format using **Pydantic**.

## Installation & Setup

> **No virtual environment (venv) was used.** Ensure you have the necessary dependencies installed globally or in your existing environment.

````

### 2️⃣ Install Dependencies
Ensure you have Python **3.10+** installed. Then, install the required dependencies:
```bash
pip install langchain-anthropic browser-use pydantic python-dotenv
````

### 3️⃣ Set Up Environment Variables

Create a `.env` file in the root directory and add your API keys:

```
ANTHROPIC_API_KEY=your_anthropic_key_here
```

### 4️⃣ Run the Web Scraper

```bash
python main.py
```

## Project Structure

```
WebScraperAi/
│── main.py            # The AI-powered web scraper
│── .gitignore         # Ignoring unnecessary files
│── README.md          # Project documentation
│── .env (not included) # API keys and credentials (create this manually)
```
