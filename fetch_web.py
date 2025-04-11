# utils/fetch_web.py
import requests
import os
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

def search_web(query, num_results=5):
    url = "https://api.tavily.com/search"
    headers = {"Authorization": f"Bearer {TAVILY_API_KEY}"}
    payload = {"query": query, "num_results": num_results}
    
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    
    results = response.json().get("results", [])
    return [r.get("content", "") for r in results]
