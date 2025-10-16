# Products Chatbot API

A **FastAPI-based chatbot** that provides human-like responses to customer queries about products using the [DummyJSON Products API](https://dummyjson.com/products) and Groq LLM API.

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Folder Structure](#folder-structure)  
- [Setup Instructions](#setup-instructions)  
- [Environment Variables](#environment-variables)  
- [API Endpoints](#api-endpoints)  
- [Examples](#examples)  
- [AI Integration (RAG-style)](#ai-integration-rag-style)  
- [Error Handling](#error-handling)  
- [Testing the API](#testing-the-api)  

---

## Project Overview

The Products Chatbot API allows users to:

- Query products by name, category, price, or ratings.  
- Receive natural language responses like a human agent.  
- Integrate AI reasoning through Groq LLM API.

This project demonstrates **REST API design, FastAPI structure, modular coding, AI integration, and RAG-style chatbot logic**.

---

## Features

- **GET /api/products** – Fetch all products.  
- **POST /api/chat** – Ask questions like “Tell me about Kiwi” or “What’s the price of Mango?”.  
- Modular service layers (`chatbot_service`, `product_service`).  
- Environment-based configuration using `.env`.  
- AI-generated natural language responses using Groq LLM.

---

## Folder Structure

```
server/
 ├── app/
 │    ├── api/
 │    │    └── routes_chatbot.py      # API endpoints
 │    ├── core/
 │    │    └── config.py             # Environment & settings
 │    ├── services/
 │    │    ├── chatbot_service.py     # Chatbot logic
 │    │    └── product_service.py     # Product data retrieval
 │    ├── models/
 │    │    └── schemas.py             # Pydantic models
 │    ├── utils/
 │    │    └── groq_client.py         # Groq API client
 │    └── main.py                     # FastAPI entry point
 ├── .env                             # Environment variables
 ├── requirements.txt                 # Python dependencies
 └── README.md
```

---

## Setup Instructions

1. **Clone the repository:**

```bash
git clone <repo-url>
cd server
```

2. **Create a virtual environment and activate it:**

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Create a `.env` file** in the project root:

```text
GROQ_API_KEY=<your_groq_api_key>
GROQ_API_BASE=https://api.groq.com/openai/v1
GROQ_MODEL=<supported_model_name>
DUMMYJSON_BASE=https://dummyjson.com
```

5. **Run the server:**

```bash
uvicorn app.main:app --reload
```

6. **Open Swagger UI:**  
   Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to interact with the API.

---

## Environment Variables

| Variable          | Description                               |
|------------------|-------------------------------------------|
| `GROQ_API_KEY`    | Your Groq API key                          |
| `GROQ_API_BASE`   | Groq API base URL                          |
| `GROQ_MODEL`      | Supported model to use for responses      |
| `DUMMYJSON_BASE`  | DummyJSON API base URL                     |

---

## API Endpoints

### GET `/api/products`

Fetch all products.

**Response Example:**

```json
[
  {
    "id": 1,
    "title": "iPhone 9",
    "price": 549,
    "rating": 4.69,
    "category": "smartphones"
  },
  ...
]
```

---

### POST `/api/chat`

Send a message to the chatbot.

**Request Example:**

```json
{
  "message": "Tell me about Kiwi"
}
```

**Response Example:**

```json
{
  "response": "Kiwi is a nutrient-rich fruit priced at $2.49, rated 4.9 stars by our customers. It ships overnight and comes with a 6-month warranty."
}
```

**Supported Questions:**

- “What’s the price of Kiwi?”  
- “Do you have any electronics?”  
- “Show me products with ratings above 4.”  
- “Tell me the reviews for Kiwi.”

---

## AI Integration (RAG-style)

The chatbot uses **Retrieval-Augmented Generation (RAG)** to provide intelligent responses:

1. **Retrieval:** Identify products mentioned in the user's message and fetch relevant data from the DummyJSON API.
2. **Augmented Generation:** Use Groq LLM to generate a human-like natural language response using the retrieved product information.
3. **Response:** Deliver coherent and context-aware answers that combine factual data with conversational phrasing.

This ensures the chatbot is **data-driven** while maintaining a **natural conversation style**.

---

## Error Handling

- Returns HTTP status codes for invalid requests or failures.  
- Handles **invalid API keys** and **model deprecation** gracefully.  
- Provides fallback messages if Groq API fails.

---

## Testing the API

### Using Python `requests`

```python
import requests

BASE_URL = "http://127.0.0.1:8000"

# Test GET /api/products
r = requests.get(f"{BASE_URL}/api/products")
print(r.json())

# Test POST /api/chat
payload = {"message": "Tell me about iPhone 9"}
r = requests.post(f"{BASE_URL}/api/chat", json=payload)
print(r.json())
```

### Using `curl`

```bash
# Get products
curl http://127.0.0.1:8000/api/products

# Send chat message
curl -X POST http://127.0.0.1:8000/api/chat \
-H "Content-Type: application/json" \
-d '{"message": "Tell me about iPhone 9"}'
```

---


