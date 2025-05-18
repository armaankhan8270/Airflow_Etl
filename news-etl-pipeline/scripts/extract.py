
import requests
import json

def extract_news():
    url = "https://newsapi.org/v2/top-headlines?category=technology&language=en&apiKey=YOUR_API_KEY"
    response = requests.get(url)
    data = response.json()

    with open('/tmp/news_raw.json', 'w') as f:
        json.dump(data['articles'], f)
