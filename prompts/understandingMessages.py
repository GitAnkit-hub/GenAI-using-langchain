from langchain.messages import SystemMessage, HumanMessage

model = ""

messages = [
    SystemMessage(
        content="You are a cybersecurity instructor."
    ),
    HumanMessage(
        content="Explain AES encryption."
    )
]

response = model.invoke(messages)

print(response.content)