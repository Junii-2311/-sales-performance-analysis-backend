import requests

# Update with your Gemini API key
# GEMINI_API_KEY = "AIzaSyAULfCLE-In5rsITsMIj92NU69MMAcE7Uc"
GEMINI_API_KEY = "AIzaSyCVQayDc3yo69DchduXTZcW9e-Qjmgq_Vk"

def analyze_sales_with_gemini(data, query):
    try:
        
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

        
        headers = {
            "Authorization": f"Bearer {GEMINI_API_KEY}",  # Bearer token for authentication
            "Content-Type": "application/json",          # Specify JSON content
        }
        
        # Create the payload to send with the request
        payload = {
            "contents": [
                {
                    "parts": [{"text": query}],  # Query to the Gemini API
                }
            ]
        }
        
        # Make a POST request to the API
        response = requests.post(url, json=payload, headers=headers)
        
        # Raise an exception for HTTP errors
        response.raise_for_status()
        
        # Parse the response and extract analysis
        result = response.json()
        return result  # Or access specific keys from the JSON response
    except requests.exceptions.RequestException as e:
        return {"error": f"Gemini API request failed: {str(e)}"}
