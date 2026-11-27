from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
load_dotenv()



#model loaded
model = ChatOpenAI(model='gpt-6-luna')


# ready the prompt
prompt = PromptTemplate(
    template = "write a summary for the following poem - \n{poem}",
    input_variables = ['poem']
)


# load the parser
parser = StrOutputParser()


# document loader loaded
loader = TextLoader('cricket.txt', encoding='utf-8')
docs = loader.load()


# print(docs)  # contains the page_content and metadata
# print(docs[0].page_content)
# print(docs[0].metadata)

print(type(docs))# its a list

print(len(docs))  # 1 length

# print(docs[0])  # getting the content

print(type(docs[0]))  # <class 'langchain_core.documents.base.Document'>



#ready the chain
chain = prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))