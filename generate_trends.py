import pandas as pd
import pyodbc
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=TrendDiscoveryAI;"
    "Trusted_Connection=yes;"
)

df = pd.read_sql("SELECT Title FROM NewsArticles", conn)

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=50
)

X = vectorizer.fit_transform(df["Title"])

words = vectorizer.get_feature_names_out()

counts = X.sum(axis=0).A1

top_words = sorted(
    zip(words, counts),
    key=lambda x: x[1],
    reverse=True
)[:20]

cursor = conn.cursor()

for word, score in top_words:
    cursor.execute(
        """
        INSERT INTO Trends
        (Keyword, Frequency)
        VALUES (?, ?)
        """,
        word,
        int(score)
    )

conn.commit()

print("Trends saved")