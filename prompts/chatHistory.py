from langchain_core.messages import HumanMessage, AIMessage

chat_history = []

while True:

    user_input = input("You: ")

    if user_input == "exit":
        break

    chat_history.append(
        HumanMessage(content=user_input)
    )

    response = model.invoke(chat_history)

    chat_history.append(response)

    print("AI:", response.content)