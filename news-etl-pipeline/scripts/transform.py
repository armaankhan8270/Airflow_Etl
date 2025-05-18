
import json
import re

def clean_text(text):
    return re.sub(r'<[^>]*>', '', text).strip()

def transform_news():
    with open('/tmp/news_raw.json', 'r') as f:
        raw_data = json.load(f)

    transformed = []
    for article in raw_data:
        transformed.append({
            "title": clean_text(article.get("title", "")),
            "description": clean_text(article.get("description", "")),
            "url": article.get("url", ""),
            "published_at": article.get("publishedAt", "")
        })

    with open('/tmp/news_transformed.json', 'w') as f:
        json.dump(transformed, f)
