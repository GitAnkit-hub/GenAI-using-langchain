from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful Python instructor."),
    ("human", "Explain {topic} in simple language.")
])

prompt = chat_template.invoke({
    "topic": "List comprehension"
})

response = model.invoke(prompt)

print(response.content)