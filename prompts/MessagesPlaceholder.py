from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)


model = ''
chat_history = []
chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a cryptography instructor."),

    MessagesPlaceholder(
        variable_name="chat_history"
    ),

    ("human", "{input}")
])



prompt = chat_template.invoke({
    "chat_history": chat_history,
    "input": "Explain its key expansion."
})

response = model.invoke(prompt)

print(response.content)