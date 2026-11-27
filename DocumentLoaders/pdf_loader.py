from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader('dl-curriculum.pdf')


docs = loader.load()

# print(docs)
print(type(docs))    # list
print(len(docs))    # shows number of pages



print(docs[0].page_content)  # first page ka content
print(docs[0].metadata)
# print(docs[1].page_content)



# there exists multiple pdf loader
# PyPDFLoader works well only when data in the pdf is text only


# more PDF Loaders

#go to -> langchain official website




