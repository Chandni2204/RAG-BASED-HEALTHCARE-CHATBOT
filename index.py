import os
from pathlib import Path
import faiss
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS

#import os
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env
openai_api_key = os.getenv("OPENAI_API_KEY")



# Define the folder containing CSV files
folder_path = "Data"

# Get all CSV file paths in the folder
file_paths = [str(file) for file in Path(folder_path).glob("*.csv")]

# Initialize an empty list to store all documents
all_docs = []

# Load documents from CSV files
for file_path in file_paths:
    loader = CSVLoader(file_path=file_path)
    docs = loader.load_and_split()
    all_docs.extend(docs)

# Initialize embeddings
embeddings = OpenAIEmbeddings()

# Determine embedding dimension
embedding_dim = len(embeddings.embed_query(" "))

# Create a FAISS index with L2 (Euclidean) distance
index = faiss.IndexFlatL2(embedding_dim)

# Initialize FAISS vector store
vector_store = FAISS(
    embedding_function=embeddings,
    index=index,
    docstore=InMemoryDocstore({}),
    index_to_docstore_id={}
)

# Add documents to the vector store
vector_store.add_documents(all_docs)

# Save the index locally
save_path = "faiss_index1"
vector_store.save_local(save_path)