import pandas as pd
import pyodbc
from sklearn.feature_extraction.text import TfidfVectorizer

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=TrendDiscoveryAI;"
    "Trusted_Connection=yes;"
)

query = "SELECT Title FROM NewsArticles"

df = pd.read_sql(query, conn)

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=20
)

X = vectorizer.fit_transform(df["Title"])

print(vectorizer.get_feature_names_out())