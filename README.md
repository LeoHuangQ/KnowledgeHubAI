# KnowledgeHub AI - Retrieval-Augmented Generation (RAG) System

## Overview

KnowledgeHub AI is a Retrieval-Augmented Generation (RAG) application that allows users to upload their own knowledge base and ask natural language questions grounded in those documents.

Unlike a simple chatbot, the application retrieves the most relevant document chunks from a vector database before generating a response with an LLM, reducing hallucinations and enabling responses based on user-provided data.

This project was built to demonstrate practical AI application development, backend engineering, API design, and modern Retrieval-Augmented Generation architecture.

---

## Features

* Upload text documents into a knowledge base
* Automatic document chunking
* OpenAI Embedding API integration
* Chroma vector database for semantic search
* Context-aware question answering
* Streaming AI responses using Server-Sent Events (SSE)
* Modular backend architecture
* RESTful APIs built with FastAPI

---

## Tech Stack

### Backend

* Python
* FastAPI
* Uvicorn

### AI

* OpenAI API
* GPT Models
* OpenAI Embedding API (`text-embedding-3-small`)

### Vector Database

* ChromaDB

### Document Processing

* LangChain Community Document Loaders
* RecursiveCharacterTextSplitter

### Future Improvements

* PDF support
* DOCX support
* Metadata filtering
* Hybrid Search (Vector + Keyword)
* Conversation Memory
* Authentication
* Multi-user Knowledge Bases
* Docker Deployment
* Kubernetes Deployment

---

# System Architecture

```text
                 +----------------+
                 |     Client     |
                 +--------+-------+
                          |
                          |
                    REST / SSE API
                          |
                          ▼
                 +----------------+
                 |    FastAPI      |
                 +--------+---------+
                          |
          +---------------+---------------+
          |                               |
          ▼                               ▼
 Loading Service                  Chat Service
          |                               |
          ▼                               ▼
 Document Loader                 Similarity Search
          |                               |
          ▼                               ▼
 Text Splitter                 Retrieved Context
          |                               |
          ▼                               ▼
 OpenAI Embedding API             Prompt Builder
          |                               |
          ▼                               ▼
 Chroma Vector DB  <------------- GPT Model
```

---

# Project Structure

```text
KnowledgeHubAI/

├── data/
│
├── services/
│   ├── loading_service.py
│   └── chat_service.py
│
├── util/
│   ├── doc_loader.py
│   ├── text_splitter.py
│   ├── embedding.py
│   └── db_loader.py
│
├── chroma_db/
│
├── main.py
│
└── README.md
```

---

# RAG Pipeline

## 1. Document Upload

The user uploads one or more documents through the FastAPI endpoint.

---

## 2. Document Loading

Documents are loaded into memory using LangChain document loaders.

Supported today:

* TXT

Planned:

* PDF
* DOCX
* Markdown

---

## 3. Text Chunking

Large documents are divided into overlapping chunks using RecursiveCharacterTextSplitter.

Example configuration:

* Chunk Size: 1000 characters
* Chunk Overlap: 200 characters

Overlapping chunks preserve context between adjacent sections and improve retrieval quality.

---

## 4. Embedding Generation

Each chunk is converted into a dense vector using the OpenAI Embedding API.

Embedding Model:

```
text-embedding-3-small
```

Batch embedding requests are used to reduce API calls and improve ingestion performance.

---

## 5. Vector Storage

Each document chunk is stored in ChromaDB together with:

* Document text
* Embedding vector
* Metadata
* Source filename

This enables semantic similarity search across uploaded knowledge.

---

## 6. Question Answering

When a user submits a question:

1. Generate an embedding for the question.
2. Perform similarity search in ChromaDB.
3. Retrieve the most relevant chunks.
4. Build a prompt using the retrieved context.
5. Send the prompt to the GPT model.
6. Stream the response back to the client.

---

# Design Decisions

## Separation of Concerns

The project separates responsibilities into independent modules:

* Document Loading
* Text Splitting
* Embedding Generation
* Vector Database
* Business Logic
* API Layer

This makes the code easier to maintain, test, and extend.

---

## Why Use the OpenAI SDK for Embeddings?

Instead of relying on LangChain wrappers, embeddings are generated directly through the OpenAI SDK.

Benefits:

* Better understanding of the RAG pipeline
* Framework-independent implementation
* Easier debugging
* Easier migration to another vector database or embedding provider

---

## Why ChromaDB?

ChromaDB is lightweight, open source, and ideal for local RAG development.

It provides:

* Persistent vector storage
* Similarity search
* Metadata filtering
* Simple Python API

---

## Future Roadmap

* Support multiple knowledge bases
* Async document ingestion
* Background embedding jobs
* Redis caching
* Re-ranking models
* Citation support
* Source highlighting
* Evaluation pipeline
* Hybrid retrieval
* Docker deployment
* CI/CD pipeline
* Cloud deployment (AWS)

---

# Skills Demonstrated

## Backend Engineering

* REST API Design
* FastAPI
* Dependency Management
* Modular Architecture
* Service Layer Design
* Error Handling

## AI Engineering

* Retrieval-Augmented Generation (RAG)
* Prompt Engineering
* Semantic Search
* Vector Embeddings
* OpenAI API Integration
* Context Window Management

## Data Processing

* Document Parsing
* Text Chunking
* Metadata Management
* Vector Storage

## Software Engineering

* Clean Architecture
* Separation of Concerns
* Reusable Components
* Maintainable Code
* Extensible Project Structure

---

# Running the Project

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
```

## Start the Server

```bash
uvicorn main:app --reload
```

## Upload Documents

```http
POST /upload
```

## Ask Questions

```http
POST /chatbot
```

---

# Learning Goals

This project was built to deepen practical experience with modern AI application development and demonstrate an understanding of how production Retrieval-Augmented Generation systems are designed beyond simply using high-level frameworks.

The focus is on building each stage of the RAG pipeline in a modular, maintainable way while keeping the implementation understandable, extensible, and suitable for real-world backend services.

# Author
Built by Leo Huang Full-stack engineer with 10+ years experience in scalable systems, fin tech, e-commerce, BI, SaaS, customer-facing web applications and AI-powered products.
