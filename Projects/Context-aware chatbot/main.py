# from fastapi import FastAPI
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
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


model = ChatOpenAI(model='gpt-6-luna',max_completion_tokens=1000)

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

# while True:
#     query = input("Enter your question to be asked from LLM?")


#     if(query.lower()=='exit'):
#         break
#     else:
#         chat_history.append(HumanMessage(content=query))

#     response = model.invoke(chat_history)
#     print(response.content)
#     chat_history.append(response) # its better to have additional info to llm



# made a context-aware chatbot




# Let's move to Stage 4 — Giving chatbot a personality using ChatPromptTemplate.


# make the chatbot behave like a cybersecurity instructor rather than a general-purpose assistant.

system_instruction = """
You are an experienced cybersecurity instructor.

Your scope is limited to:
- Cybersecurity
- Cryptography
- Network security
- Computer networks
- Information security
- Secure software development

Rules:
1. Answer questions related to the above topics.
2. Explain technical concepts in simple language.
3. Use practical examples wherever appropriate.
4. Correct misconceptions politely.
5. If the user asks something unrelated to these topics,
   politely explain that you are a cybersecurity instructor
   and cannot help with unrelated questions.
6. You may use previous conversation history to understand
   follow-up questions, such as "explain this further".
"""


chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_instruction),
        MessagesPlaceholder(variable_name="chat_history")
    ]
)

while True:
    query = input("Ask your cybersecurity question (type exit to quit): ")


    if(query.lower()=='exit'):
        break
    else:
        chat_history.append(HumanMessage(content=query))

    prompt = chat_template.invoke({"chat_history": chat_history})
    
    response = model.invoke(prompt)  # Returns AIMessage
    
    print(f"\n{response.content}")
    chat_history.append(response) # its better to have additional info to llm








