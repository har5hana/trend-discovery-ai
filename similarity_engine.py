import pandas as pd
import pyodbc

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=TrendDiscoveryAI;"
    "Trusted_Connection=yes;"
)

df = pd.read_sql(
    "SELECT TOP 50 Keyword FROM Trends",
    conn
)

keywords = df["Keyword"].tolist()

print(keywords)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

embeddings = model.encode(keywords)

similarity_matrix = cosine_similarity(
    embeddings
)

print(similarity_matrix.shape)