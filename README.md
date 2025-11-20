# Smart Scraper Graph Application

This application is a Streamlit-based web scraper that uses `scrapegraphai` with Google's Gemini 2.5 Flash model and Nomic Embeddings to extract structured data from websites based on user-provided instructions.

## Features
- Scrapes data from a specified URL using natural language instructions.
- Utilizes Gemini 2.5 Flash for intelligent content extraction.
- Saves extracted data in both JSON (`output.json`) and CSV (`output.csv`) formats.
- Provides a user-friendly web interface powered by Streamlit.
- Includes basic error handling for common scraping issues.

## Prerequisites
Before running the application, ensure you have the following installed:
- Python 3.8+
- pip (Python package installer)

## Setup

### 1. Clone the repository (or create the files manually)
```bash
git clone <your-repository-url>
cd <your-repository-directory>
```
(If you've created `app.py` and `requirements.txt` directly, ensure they are in the same directory.)

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
Install the required Python packages using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 4. Set up your Google Gemini API Key
This application requires a Google API Key to access the Gemini 2.5 Flash model.

1.  **Obtain an API Key**: If you don't have one, create a key in [Google AI Studio](https://makersuite.google.com/app/apikey).
2.  **Set as Environment Variable**: The application expects the API key to be available as an environment variable named `GOOGLE_API_KEY`. 

    *   **In Google Colab**: Use the "🔑 Secrets" panel on the left sidebar to add a new secret named `GOOGLE_API_KEY` with your API key as the value.
    *   **Locally (Linux/macOS)**:
        ```bash
        export GOOGLE_API_KEY="YOUR_API_KEY_HERE"
        ```
    *   **Locally (Windows Command Prompt)**:
        ```bash
        set GOOGLE_API_KEY="YOUR_API_KEY_HERE"
        ```
    *   **Locally (Windows PowerShell)**:
        ```powershell
        $env:GOOGLE_API_KEY="YOUR_API_KEY_HERE"
        ```

    Replace `"YOUR_API_KEY_HERE"` with your actual API key.

## Usage

1.  **Run the Streamlit application**:
    ```bash
    streamlit run app.py
    ```

2.  **Access the App**: Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

3.  **Input Details**: In the Streamlit interface:
    *   Enter the **URL** of the website you wish to scrape.
    *   Enter your **prompt/instructions** specifying what data you want to extract (e.g., "Extract all product names and their prices").

4.  **Scrape**: Click the "Scrape" button. The application will process your request, display the scraped data, and save it to `output.json` and `output.csv` in the same directory as `app.py`.

## Output Files
- `output.json`: Contains the raw scraped data in JSON format.
- `output.csv`: Contains the scraped data in a tabular CSV format, if the extracted data is suitable.

## Technologies Used
- [Streamlit](https://streamlit.io/): For creating interactive web applications.
- [ScrapeGraphAI](https://github.com/ScrapeGraphAI/ScrapeGraphAI): The intelligent web scraping framework.
- [Google Gemini API](https://ai.google.dev/): For advanced language model capabilities.
- [Nomic Embed](https://www.nomic.ai/): For text embeddings.
- [Pandas](https://pandas.pydata.org/): For data manipulation and CSV export.
