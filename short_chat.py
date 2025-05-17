from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate,FewShotChatMessagePromptTemplate
from langchain_openai import ChatOpenAI
openai_api_key = "EMPTY"

openai_api_base = "http://192.168.56.1:1234/v1"

chat = ChatOpenAI(
    openai_api_key=openai_api_key,
    openai_api_base=openai_api_base,
    temperature=0.7
)

examples = [{"input":"2+2","output":"4"},{"input":"3+5","output":"8"},{"input":"1+1","output":"2"}]
example_prompt = ChatPromptTemplate.from_messages([("human","{input}"),("ai","{output}")])

few_shot_prompt = FewShotChatMessagePromptTemplate(
    examples=examples,
    example_prompt=example_prompt)    

final_prompt = ChatPromptTemplate.from_messages([("system","你是一位非常厉害的数学天才"),few_shot_prompt,("human","{input}")])

output_parser = StrOutputParser()

chain = final_prompt | chat | output_parser

# chain.invoke({"input":"3的平方加上4的平方等于多少？"})

print(chain.invoke({"input":"3的平方加上4的平方等于多少？"}))