from fastapi import FastAPI, Query
import pandas as pd
import json  # Import json for JSON operations
import requests

# Update with your Gemini API key
GEMINI_API_KEY = "AIzaSyAxWeCoz2DvnYl0DvjIfaO2lUKTF5MIbdE"

# Function to load sales data
def load_sales_data(file_path):
    try:
        if file_path.endswith('.csv'):
            data = pd.read_csv(file_path)
        elif file_path.endswith('.json'):
            data = pd.read_json(file_path)
        else:
            raise ValueError("Unsupported file format")
        return data
    except Exception as e:
        return {"error": str(e)}

# Function to integrate with Gemini API
def analyze_sales_with_gemini(query):
    try:
        # API endpoint URL
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

        # HTTP headers
        headers = {
            "Content-Type": "application/json",  # Specify JSON content
        }

        # Payload to send with the request
        payload = json.dumps({
            "contents": [
                {
                    "parts": [
                        {"text": query}  # Use the query parameter
                    ]
                }
            ]
        })

        # Make a POST request to the API
        response = requests.post(url, headers=headers, data=payload)

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Parse the response and extract analysis
        result = response.json()
        return result  # Or access specific keys from the JSON response
    except requests.exceptions.RequestException as e:
        return {"error": f"Gemini API request failed: {str(e)}"}