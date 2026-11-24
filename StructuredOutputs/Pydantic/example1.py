from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field



# A. creating a pydantic model
class Student(BaseModel):
    name:str


# creating an object
std = Student(name="Ankit")
print(std)


# B. Data Validation
std1 = Student(name=123)
print(std1)
# model = ChatOpenAI(model="gpt-6-luna", max_completion_tokens=300)

