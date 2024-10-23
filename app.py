## Imports
from langchain_ollama.chat_models import ChatOllama
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import streamlit as st
from langchain.prompts import PromptTemplate

## Application Title
st.title("OpenAI Embeddings with LLaMA Chatbot RAG Application")

## Defining the LLaMA Model (chatbot)
model = ChatOllama(model="llama3")  # Using LLaMA model for the chatbot

## Defining the prompt template for answering questions
prompt = PromptTemplate.from_template("Answer the question based on the given context. \n Question: {question}\n Context: {context}")

# Defining a function to read the contents inside a PDF file
def read_pdf(file):
    text = ""
    try:
        pdf_reader = PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    except Exception as e:
        st.error(f"Error reading the PDF file: {e}")
    return text

entire_docs = None

# Uploading the file using streamlit browse option
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file is not None:
    ## Displaying the file name that has been uploaded
    st.write("File Name:", uploaded_file.name)
    pdf_content = read_pdf(uploaded_file)
    ## Defining a text splitter to split the documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=50,
        length_function=len
    )
    ## Applying the text splitter on the documents
    docs = text_splitter.create_documents([pdf_content])
    entire_docs = docs

    ## Displaying some description about the document like number of chunks, sample chunk
    st.write(f"The document is divided into {len(docs)} chunks")
    st.write("Sample Chunk for the given document:")
    st.write(docs[0])
    ## Loading.. displayed on UI
    st.subheader("Loading....")

# Defining the vector embeddings using OpenAI Embeddings
embeddings = OpenAIEmbeddings()

# Creating the vector database using the embeddings
if entire_docs:
    db = FAISS.from_documents(entire_docs, embedding=embeddings)

    # Function to retrieve the context based on similarity search from the vector database
    def retrieve_query(query):
        matching_results = db.similarity_search(query)
        return matching_results

    # Taking the question as input from the user
    user_input = st.text_input("Enter your query from the inserted PDF:")

    # Fetching the context based on the user's query from vector db
    if user_input:
        results = retrieve_query(user_input)

        # Modify the chain to remove RunnablePassthrough
        chain = {"question": user_input, "context": results} | prompt | model
        
        # Invoke the chain directly
        final = chain.invoke({"question": user_input, "context": results})
        
        # Return the response
        st.write("The Response is: \n", final)


