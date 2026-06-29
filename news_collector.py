import feedparser
import pyodbc

print("Fetching news...")

feed = feedparser.parse(
    "https://news.google.com/rss/search?q=Artificial+Intelligence"
)

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=TrendDiscoveryAI;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

count = 0

for entry in feed.entries:
    cursor.execute("""
        INSERT INTO NewsArticles
        (Title, Source)
        VALUES (?, ?)
    """,
    entry.title,
    "Google News")

    count += 1

conn.commit()

print(f"{count} articles saved!")

conn.close()