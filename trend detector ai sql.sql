USE TrendDiscoveryAI;
GO

CREATE TABLE NewsArticles (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Title NVARCHAR(MAX),
    PublishedDate DATETIME NULL,
    Source NVARCHAR(255),
    CollectedAt DATETIME DEFAULT GETDATE()
);
USE TrendDiscoveryAI;

SELECT TOP 20 *
FROM NewsArticles
ORDER BY Id DESC;

CREATE TABLE Trends (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Keyword NVARCHAR(100),
    Frequency INT,
    TrendDate DATETIME DEFAULT GETDATE()
);

CREATE TABLE TrendHistory (
    Id INT IDENTITY PRIMARY KEY,
    Keyword NVARCHAR(100),
    Frequency FLOAT,
    TrendScore FLOAT,
    RecordedAt DATETIME DEFAULT GETDATE()
);

CREATE TABLE RelatedTrends(
    Id INT IDENTITY PRIMARY KEY,
    Keyword NVARCHAR(100),
    RelatedKeyword NVARCHAR(100),
    SimilarityScore FLOAT
);