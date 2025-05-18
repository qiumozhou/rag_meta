from langchain_community.document_loaders import TextLoader

loader=TextLoader("./1.txt",encoding="utf8")

doc = loader.load()

print(doc)