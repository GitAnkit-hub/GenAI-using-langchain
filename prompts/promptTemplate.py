from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template(
    "Explain {topic} in {style} language."
)

prompt = template.invoke({
    "topic": "Cryptography",
    "style": "simple"
})

print(prompt)   