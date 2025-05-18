
import json
import psycopg2

def load_to_db():
    conn = psycopg2.connect(
        dbname="airflow", user="airflow", password="airflow", host="postgres"
    )
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS tech_news (
            id SERIAL PRIMARY KEY,
            title TEXT,
            description TEXT,
            url TEXT,
            published_at TIMESTAMP
        )
    """)

    with open('/tmp/news_transformed.json', 'r') as f:
        news_data = json.load(f)

    for article in news_data:
        cur.execute("""
            INSERT INTO tech_news (title, description, url, published_at)
            VALUES (%s, %s, %s, %s)
        """, (article["title"], article["description"], article["url"], article["published_at"]))

    conn.commit()
    cur.close()
    conn.close()
