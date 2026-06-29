# Trend Discovery AI

> Discover emerging technology trends before they become mainstream.

Trend Discovery AI is an intelligence platform that continuously collects data from technology-focused news sources, identifies rapidly growing topics, analyzes relationships between trends, and forecasts future momentum using machine learning.

Unlike traditional trend dashboards that simply display current popularity, Trend Discovery AI focuses on detecting *what is about to become important* by combining trend scoring, semantic similarity analysis, clustering, forecasting, and interactive knowledge graphs.

---
## Screenshots

<img width="949" height="436" alt="Screenshot 2026-06-30 140331" src="https://github.com/user-attachments/assets/c36a09be-8ef5-4bbb-93c3-1c1009a5e259" />

<img width="209" height="314" alt="Screenshot 2026-06-30 140359" src="https://github.com/user-attachments/assets/a778b993-9e74-4be8-bcca-1cd2bc14b0fe" />

<img width="953" height="441" alt="Screenshot 2026-06-30 140459" src="https://github.com/user-attachments/assets/4de9dd19-cc5d-4bb8-9d84-119015710906" />

<img width="950" height="431" alt="Screenshot 2026-06-30 140523" src="https://github.com/user-attachments/assets/b4861ce6-47b1-4eca-9058-afa0e84ae2b7" />

<img width="944" height="419" alt="Screenshot 2026-06-30 140538" src="https://github.com/user-attachments/assets/2721de0b-c862-4de4-8fd7-1f8c7a7dc254" />

<img width="952" height="430" alt="Screenshot 2026-06-30 140612" src="https://github.com/user-attachments/assets/1987ca8b-b086-439e-be83-afcc77c63569" />

<img width="181" height="200" alt="Screenshot 2026-06-30 140658" src="https://github.com/user-attachments/assets/8a089b5d-0840-44bb-9241-8d4068e85aff" />


## Why I Built This

Technology trends move faster than ever.

New frameworks, AI models, research breakthroughs, and developer tools emerge daily. Most people only discover these trends after they have already become popular.

I wanted to build a system capable of answering questions such as:

* What technologies are gaining momentum right now?
* Which trends are related to each other?
* What topics are likely to grow over the next few weeks?
* What hidden connections exist between emerging technologies?

Trend Discovery AI was built to solve that problem.

---

## What It Does

### Multi-Source Trend Collection

The platform automatically gathers technology-related information from multiple online sources including:

* Google News
* Hacker News

The collected information is stored inside a SQL Server database for further analysis.

---

### Trend Detection Engine

Using Natural Language Processing techniques, the system extracts meaningful keywords and topics from collected articles.

Instead of simply counting mentions, a custom trend scoring mechanism identifies topics that are accelerating in popularity.

Examples:

* AI Agents
* MCP
* LangGraph
* Gemini
* Open Source LLMs

---

### Semantic Similarity Engine

Traditional keyword systems treat every topic as independent.

Trend Discovery AI uses transformer embeddings to understand semantic relationships between concepts.

For example:

AI Agents

→ CrewAI

→ LangGraph

→ AutoGen

→ MCP

This allows discovery of related technologies even when exact keywords do not match.

---

### Topic Clustering

Similar trends are automatically grouped into broader categories.

Examples:

LLMs

* GPT
* Gemini
* Claude

AI Agents

* CrewAI
* AutoGen
* LangGraph

Research

* Papers
* Benchmarks
* Model Architectures

This helps users understand larger movements instead of isolated keywords.

---

### Trend Forecasting

Historical trend data is analyzed to estimate future growth patterns.

The forecasting engine predicts:

* Short-term momentum
* Emerging technologies
* Potential breakout trends

This transforms the platform from a monitoring tool into a predictive intelligence system.

---

### Interactive Knowledge Graph

Trend relationships are visualized through an interactive graph.

Instead of viewing trends as isolated entities, users can explore how technologies connect and influence each other.

The graph is generated dynamically using semantic similarity relationships discovered by the platform.

---

## System Architecture

Data Sources

↓

Data Collection Layer

↓

SQL Server Database

↓

NLP Processing

↓

Trend Analysis Engine

↓

Machine Learning Models

↓

Knowledge Graph Generation

↓

Interactive Dashboard

---

## Technology Stack

### Backend

* Python
* SQL Server
* PyODBC

### Data Processing

* Pandas
* NumPy

### Machine Learning

* Scikit-Learn
* Sentence Transformers
* Prophet

### Visualization

* Streamlit
* Plotly
* PyVis
* NetworkX

### NLP

* TF-IDF
* Transformer Embeddings
* Cosine Similarity

---

## Current Features

* Automated news collection
* Trend extraction
* Trend scoring
* Topic clustering
* Semantic similarity analysis
* Knowledge graph generation
* Interactive analytics dashboard
* Trend forecasting

---

## Future Roadmap

* Real-time data pipelines
* RAG-powered trend assistant
* Email and Telegram alerts
* Social media trend integration
* User watchlists
* Personalized trend recommendations
* API access for developers

---

## Author

Harshana Yadav

