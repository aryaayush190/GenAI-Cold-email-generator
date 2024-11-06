
from langchain_groq import ChatGroq

llm = ChatGroq(
    temperature=0, 
    groq_api_key='<add your API key here.>', 
    model_name="llama-3.1-70b-versatile"
)

response = llm.invoke("The first person to land on moon was ...")
print(response.content)
