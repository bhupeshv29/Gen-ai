from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


file_path = "./Companies in India Hiring Remote Workers.pdf"    
loader = PyPDFLoader(file_path)
docs = loader.load()


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200,
)

spiltted_docs = text_splitter.split_documents(documents=docs)


print(len(docs))
print(len(spiltted_docs))