# from fastapi import FastAPI
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# app = FastAPI()

# @app.get("/")
# def home():
#     return " this is context-aware Chatbot"

# @qpp.get("/chat")
# def chat():
#     pass


model = ChatOpenAI(model='gpt-6-luna',max_completion_tokens=300)

# response1 = model.invoke("what is encryption?")
# # response2 = model.invoke([
# #     HumanMessage(content="What is encryption?")
# # ])
# response3 = model.invoke("what is its purpose?")
# print(response1.content)
# print("\n")
# # print(response2)
# print(response3.content)  # without chat history

# response4 = model.invoke([HumanMessage(content='What is encryption'), AIMessage(content='Encryption converts plaintext into ciphertext.'), HumanMessage(content='What is its purpose?')])

# print(response4.content)

#here we get the right response of the question "What is its purpose"?

# But imagine having a conversation with 20 questions

# we need a python list to maintain this


chat_history = []

while True:
    query = input("Enter your question to be asked from LLM?")


    if(query.lower()=='exit'):
        break
    else:
        chat_history.append(HumanMessage(content=query))

    response = model.invoke(chat_history)
    print(response.content)
    chat_history.append(response) # its better to have additional info to llm



# made a context-aware chatbot




# Let's move to Stage 4 — Giving chatbot a personality using ChatPromptTemplate.


# make the chatbot behave like a cybersecurity instructor rather than a general-purpose assistant.









