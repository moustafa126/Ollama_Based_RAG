##Imports
from langchain_ollama.chat_models import ChatOllama
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.runnables import RunnablePassthrough

## Application Title
st.title("Ollama Based RAG application")

## Defining the Ollama Model
model = ChatOllama(model="llama3")

## Defining the prompt
prompt = PromptTemplate.from_template("Answer the question based on the given context. \n Question: {question}\n Context: {context}")

# Defining the parser
parser = StrOutputParser()

# Defining a function to read the contents inside a pdf file..
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
        ##Displaying the file name that has been uploaded
        st.write("File Name:", uploaded_file.name)
        pdf_content = read_pdf(uploaded_file)
        ## Defining a text splitter to split the documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap = 50,
            length_function = len,
            is_separator_regex = False
        )
        ## applying the text splitter on the documents..
        docs = text_splitter.create_documents([pdf_content])
        entire_docs = docs

        ## displaying some description about document like number of chunks, sample chunk
        st.write(f"The document is divided into {len(docs)} chunks")
        st.write("Sample Chunk for the given document:")
        st.write(docs[0])
        ## Loading.. displayed on UI
        st.subheader("Loading....")



# Defining the vector embeddings
embeddings = OllamaEmbeddings(model="llama3")

#Creating the vector database
if entire_docs:
     
    db = FAISS.from_documents(entire_docs,embedding=embeddings)

    #Function to retrieve the context based on similiarity search from vector database
    def retrieve_query(query):
            matching_results = db.similarity_search(query)
            return matching_results

    #Taking the question as input from the user
    user_input = st.text_input("Enter your query from the inserted PDF:")

    ## fetching the context based on the user's query from vector db
    results = retrieve_query(user_input)
    #Defining the chain
    chain = {"question": RunnablePassthrough(), "context": RunnablePassthrough()} | prompt | model | parser

    ## invoking the chain by passing the user's input and context retrieved fron vector db
    final = chain.invoke({"question":user_input,"context":results})
    #Finally returning the response..
    st.write("The Response is: \n",final)


     


