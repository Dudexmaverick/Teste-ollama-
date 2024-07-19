from langchain.document_loaders.pdf import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from embeddings import embedding
from langchain.vectorstores.chroma import Chroma
import chroma 


client = chroma.PersistentClient(path="/path/to/save/to")

def add_to_chroma(chunks:list[Document]):
    db = Chroma(
        persist_directory=CHROMA_PATH, embedding_function=embedding
    )
    db.add_documents(chunks, ids= load_documents)
    db.persist()

def load_documents():
    documents_loader = PyPDFDirectoryLoader()
    return documents_loader.load()
documents = load_documents()
print(documents[0])

def split_documents(documents: list[Document]):
    

    text_splitter = RecursiveCharacterTextSplitter(
            separator='/n',
            chunk_size = 500,
            chunk_overlap = 100,
            length_function = len
        
    )

    return text_splitter.split_documents(Document)
