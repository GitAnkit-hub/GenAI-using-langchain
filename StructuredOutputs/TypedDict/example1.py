from typing import TypedDict
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

class Person(TypedDict):
    name:str
    age:int
    brother_name: str
    brother_age: int

class Person1(TypedDict):
    name:list[str]
    age:list[int]

model = ChatOpenAI(model='gpt-6-luna', max_completion_tokens=300)

# using Person and Person1 Schema
structured_model = model.with_structured_output(Person1)
# print(f"\n{structured_model}")


# response = structured_model.invoke("My name is Ankit and I am 25 years old. I have brother name rohit and his age is 27 years old.")

response = structured_model.invoke("My name is Ankit and I am 25 years old. I have brother name rohit and his age is twenty-seven years old.")

print(f"\n{response}")
print(f"\n{type(response)}")

