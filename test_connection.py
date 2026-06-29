import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=TrendDiscoveryAI;"
    "Trusted_Connection=yes;"
)

print("Connected successfully!")

conn.close()