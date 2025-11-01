# 🏥 RAG-Based Healthcare Assistant Chatbot

> An intelligent AI-powered chatbot that helps users identify potential diseases based on their symptoms and provides medical insights, precautions, diet suggestions, and medication recommendations — powered by **Retrieval-Augmented Generation (RAG)** using **LangChain**, **FAISS**, and **GPT-4**.

---

## 📋 Table of Contents
1. [Project Overview](#-project-overview)
2. [Features](#-features)
3. [About Dataset](#-about-dataset)
4. [Architecture Overview](#-architecture-overview)
5. [LangChain and Vector Database Integration](#-langchain-and-vector-database-integration)
6. [GPT-4 Integration](#-gpt-4-integration)
7. [System Workflow](#-system-workflow)
8. [Installation and Setup](#-installation-and-setup)
9. [Usage](#-usage)
10. [Project Structure](#-project-structure)
11. [Demo Screenshots](#-demo-screenshots)
12. [Future Enhancements](#-future-enhancements)
13. [Contributing](#-contributing)
14. [License](#-license)
15. [Author](#-author)

---

## 🧠 Project Overview

The **RAG-Based Healthcare Chatbot** is designed to act as a **virtual healthcare assistant** that provides intelligent health insights based on user-input symptoms. It bridges the gap between medical awareness and accessibility.

### 🎯 Objectives
- Help users **recognize possible diseases** early through AI-powered symptom analysis.  
- Provide **immediate health insights** for people who might ignore minor symptoms.  
- Enable **self-monitoring** for users who track their daily health.  
- Offer clear, concise, and context-aware responses within seconds.

---

## ✨ Features

- 🩺 **Symptom-Based Disease Prediction** — identifies possible health conditions.  
- 💬 **Conversational Chat Interface** — interact naturally in plain English or Hindi.  
- 🧠 **RAG-Driven Responses** — ensures accuracy by combining retrieval and generation.  
- ⚙️ **LangChain + FAISS Integration** — fast, contextual medical data retrieval.  
- 🥗 **Personalized Recommendations** — diets, precautions, and medication advice.  
- 📊 **Token and Cost Tracking** — monitors model usage for transparency.  
- 🧾 **Chat History Storage** — saves user conversations for follow-up or analysis.  
- ❓ **Dynamic Question Generation** — generates 3 new health-related questions to keep users engaged.  
- 🌐 **Multilingual Support (English 🇬🇧 & Hindi 🇮🇳)** — powered by GPT-4’s multilingual capabilities.

---

## 📊 About Dataset

The chatbot’s intelligence is powered by a curated **medical dataset** containing:

| Data Type | Description |
|------------|-------------|
| 🩺 **Symptoms** | Symptom–disease mappings |
| 🧴 **Precautions** | Safety measures and lifestyle recommendations |
| 🥗 **Diet Plans** | Disease-specific dietary guidelines |
| 💊 **Medications** | Common medication suggestions |

## 🧠 How It Works  

The chatbot workflow is divided into three stages:  

1. **Preprocessing:** Clean and chunk the dataset (removing null values, splitting large text).  
2. **Embedding:** Convert text chunks into numerical vectors using OpenAI embeddings.  
3. **Retrieval + Response Generation:** Retrieve the most relevant chunks using FAISS and generate the final response with LLM.

---

## 🧱 Architecture Overview
The architecture of the RAG-Based Healthcare Chatbot integrates preprocessing, embedding generation, and retrieval-augmented generation using a vector database.  
This enables the chatbot to provide accurate, context-aware health information by combining stored medical data with LLM reasoning.

### 🧩 System Workflow
<img width="1041" height="624" alt="image" src="https://github.com/user-attachments/assets/0a205daf-3220-41ee-bb48-ce5332ee6a80" />

**Explanation:**

1. **Dataset (Source - Kaggle):** Medical data (CSV file) is collected and loaded.  
2. **Preprocessing:** Data is cleaned and split into manageable chunks.  
3. **Vector Embeddings:** Each chunk is converted into a numerical vector using **OpenAI Embeddings**.  
4. **Vector Database (FAISS):** Stores embeddings for semantic retrieval.  
5. **User Query:** The user asks a health-related question.  
6. **Retrieval:** The system fetches the most relevant context.  
7. **LLM Response:** The LLM combines retrieved knowledge with reasoning to generate the answer.  
8. **Output:** A final, context-aware and human-like response is returned to the user.


## 🧩 Data Chunking & Semantic Indexing  

This process ensures that even large text data can be processed and retrieved efficiently.  

The following diagram illustrates how the CSV medical dataset is processed into embeddings for storage in the FAISS vector database:

<img width="1127" height="489" alt="image" src="https://github.com/user-attachments/assets/f359a684-c032-461f-bab8-fd343884892d" />

**Steps:**

1. Extract context from the CSV dataset.  
2. Split text into multiple chunks.  
3. Generate embeddings for each chunk.  
4. Create a semantic index stored in the **Vector Database**.

## 🛠️ Tech Stack  

## 🧩 Tech Stack

| **Component**        | **Technology**                      |
|----------------------|-------------------------------------|
| **Backend**          | Flask (Python)                      |
| **LLM**              | OpenAI GPT-4                        |
| **Framework**        | LangChain                           |
| **Vector Database**  | FAISS                               |
| **Dataset Source**   | Kaggle                              |
| **Embeddings**       | OpenAI Embeddings                   |
| **Frontend**         | HTML, CSS, JavaScript (Flask Templates) |


## 🚀 Setup Instructions  

# 1️⃣ Clone the repository
git clone https://github.com/Chandni2204/RAG-BASED-HEALTHCARE-CHATBOT.git
cd RAG-BASED-HEALTHCARE-CHATBOT

# 2️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Set your OpenAI API key
echo "OPENAI_API_KEY=your_api_key_here" > .env

# 5️⃣ Run the Flask app
python app.py

Now open http://127.0.0.1:5000/ in your browser 🎉


## 🖼️ Project Outputs

### 🩺 Chat Interface (English)

### 🌐 Multilingual Support (Hindi Example)

<img width="445" height="361" alt="image" src="https://github.com/user-attachments/assets/e651534e-9c57-4644-a606-5e55bfe2067f" />

### 🧠 Disease Prediction Result
<img width="425" height="564" alt="image" src="https://github.com/user-attachments/assets/90acbdb4-5b55-4e12-9dcc-f8a6dacb911c" />

## 🩺 Symptoms of Diseases
<img width="442" height="218" alt="image" src="https://github.com/user-attachments/assets/0f239313-ea9b-4db3-9ff7-9cb3866bd516" />

## 🩺 Precautions of Diseases
<img width="447" height="415" alt="image" src="https://github.com/user-attachments/assets/ace0cf5c-abe9-44a8-9e5f-baf3d8fcebc4" />

