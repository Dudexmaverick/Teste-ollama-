#from PyPDF2 import PdfReader
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import CharacterTextSplitter
#import csv     
text = ""
loader = CSVLoader("./transcript_table(1).csv")
print(loader)
def create_text_chunks(text):

    text_splitter = CharacterTextSplitter(
            separator='/n',
            chunk_size = 500,
            chunk_overlap = 100,
            length_function = len
    )
    chunks = text_splitter.split_text(text)
    return chunks
