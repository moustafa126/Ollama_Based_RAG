# Ollama-Based RAG Application

This project implements a Retrieval Augmented Generation (RAG) system using the Ollama model and LangChain. The application allows users to upload a PDF document, process it by splitting it into chunks, store the chunks in a FAISS vector database, and answer user queries based on the context retrieved from the document. Streamlit is used for the web interface, facilitating easy interaction with the RAG system.

## Ollama Model
<p align="center">
  <img src="https://ollama.com/public/assets/c889cc0d-cb83-4c46-a98e-0d0e273151b9/42f6b28d-9117-48cd-ac0d-44baaf5c178e.png" width="200" alt="Ollama model Logo">
</p>

## 🚀 Streamlit Web Application

Experience the power of our sentiment analysis model through our interactive web application:

<p align="center">
  <a href="https://amazon-alexa-sentiment-analysis-dfh55obrkh83nwut9kyfhn.streamlit.app/">
    <img src="https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png" width="250" alt="Streamlit Logo">
  </a>
</p>



## Features

- **Ollama Chat Model Integration:** Uses the `llama3` model from Ollama for generating responses based on user queries.
- **PDF Processing:** Users can upload PDF files, which are parsed and split into manageable chunks for easier processing.
- **Vector Database:** FAISS is used to store document chunks and perform similarity searches based on user queries.
- **Streamlit Interface:** Provides an interactive UI where users can upload files, input questions, and get responses in real-time.
- **Efficient Context Retrieval:** Uses LangChain to retrieve relevant document chunks from the vector database based on similarity search.

## Requirements

- Python 3.9+
- `streamlit`
- `langchain`
- `PyPDF2`
- `faiss`
- `langchain_ollama`
- `langchain_core`

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/venkatsubash2003/Ollama_Based_RAG
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    streamlit run app.py
    ```

## How It Works

1. **Upload PDF:** Users can upload a PDF document, which is read and split into chunks of 1000 characters with an overlap of 50 characters.
2. **Vector Embeddings:** Each chunk is embedded using the `llama3` model from Ollama.
3. **Similarity Search:** When a user inputs a query, the system retrieves the most relevant chunks from the FAISS vector store.
4. **Generating Responses:** The Ollama model generates an answer based on the user's question and the retrieved context.

## Project Structure

```bash
.
├── app.py                 # Streamlit application script
├──venv
├──requirements.txt
├──.gitignore
├──README.md
```

Developed with ❤️ by Venkat Sai Subash

[LinkedIn](https://www.linkedin.com/in/venkat-sai-subash-panchakarla-b166ba23a/) 👨‍💼


