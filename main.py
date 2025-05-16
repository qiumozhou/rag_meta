from langchain_community.chat_models.openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os
 
 
API_SECRET_KEY = "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"
BASE_URL = "your api base"
os.environ["OPENAI_API_KEY"] = API_SECRET_KEY
os.environ["OPENAI_API_BASE"] = BASE_URL
 
 
# 这里的temperature参数控制答案生成的随机性，0表示按照概率最大的结果生成，也就是最稳定
# 如果温度设置为1则表示生成极富随机性的结果
# 由于我们没有指定调用哪个openai模型，默认会是gpt-3.5-turbo
chat = ChatOpenAI(temperature=0.0)
 
# 定义template字符串，这里不需要使用f字符串来赋值
template = """请将下面的中文文本翻译为{language}。\
文本：'''{text}'''
"""
 
# 将template字符串转换为langchain模板，这时候会自动识别prompt模板需要的参数，即{}中的内容
prompt_template = ChatPromptTemplate.from_template(template)
 
customer_language = '英文'
customer_text = '你好，我来自中国。'
 
# 传入相应字符串生成符合大模型输入要求的prompt
customer_messages = prompt_template.format_messages(language=customer_language, text=customer_text)
print(customer_messages[0])
 
# 调用大语言模型
customer_response = chat.invoke(customer_messages, temperature=0.0)
print(customer_response.content)