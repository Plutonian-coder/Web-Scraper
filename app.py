import nest_asyncio
nest_asyncio.apply()
import streamlit as st
import os
import json
import pandas as pd
import google.generativeai as genai
from scrapegraphai.graphs import SmartScraperGraph

# Configure Gemini API key from environment variable
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    st.error("GOOGLE_API_KEY environment variable not set. Please set it in your environment.")
    st.stop()
genai.configure(api_key=GOOGLE_API_KEY)

# Define the graph configuration for SmartScraperGraph
graph_config = {
    "llm": {
        "model": "gemini-2.5-flash-preview-04-17",
        "temperature": 0,
        "format": "json"
    },
    "embeddings": {
        "model": "nomic-embed-text"
    },
    "verbose": True,
}

# Streamlit UI elements
st.title("Smart Scraper Graph")
st.caption("This app allows you to scrape a website using Gemini API")

# Input fields for URL and user prompt
url = st.text_input("Enter the URL to scrape")
user_prompt = st.text_input("Enter your prompt")

# Scrape button logic
if st.button("Scrape"):
    # Basic validation for inputs
    if not url or not user_prompt:
        st.warning("Please provide both a URL and a user prompt.")
    else:
        try:
            # Instantiate SmartScraperGraph
            smart_scrape_graph = SmartScraperGraph(
                prompt=user_prompt,
                source=url,
                config=graph_config
            )
            
            # Run the scraping process
            with st.spinner("Scraping in progress..."):
                result = smart_scrape_graph.run()
            
            st.success("Scraping completed successfully!")
            
            # Display the result in the Streamlit app
            st.subheader("Scraping Result:")
            st.write(result)

            # Save result to output.json
            output_json_file = "output.json"
            with open(output_json_file, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=4)
            st.success(f"Result saved to {output_json_file}")

            # Save result to output.csv if it's a list of dictionaries
            if isinstance(result, list) and all(isinstance(item, dict) for item in result):
                output_csv_file = "output.csv"
                df = pd.DataFrame(result)
                df.to_csv(output_csv_file, index=False)
                st.success(f"Result saved to {output_csv_file}")
            elif isinstance(result, dict):
                output_csv_file = "output.csv"
                df = pd.DataFrame([result]) # Convert single dict to DataFrame
                df.to_csv(output_csv_file, index=False)
                st.success(f"Result saved to {output_csv_file}")
            else:
                st.info("Result is not in a suitable format (list of dicts or single dict) to be saved as CSV.")

        except Exception as e:
            st.error(f"An error occurred during scraping: {e}")
