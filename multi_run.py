from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from  langchain_core.output_parsers import StrOutputParser
from operator import itemgetter


openai_api_key = "EMPTY"

openai_api_base = "http://192.168.56.1:1234/v1"


model = ChatOpenAI(openai_api_key=openai_api_key,openai_api_base=openai_api_base,temperature=0.5)


outlinePromptTemplate = """
主题:{theme},如果要根据主题写一篇文章，请列出文章的大纲
"""

outline_prompt = ChatPromptTemplate.from_template(outlinePromptTemplate)

tipsPromptTemplate = """
主题:{theme},如果要根据主题写一篇文章，应该需要注意文章的哪些方面，才能把文章写好
"""


tips_prompt = ChatPromptTemplate.from_template(tipsPromptTemplate)

str_output = StrOutputParser()

outline = outline_prompt | model | str_output
tips = tips_prompt | model | str_output
# print(out_line_chain.invoke({"theme":"2023年中国经济形势分析"}))

articalPromprtTempdate = """
主题:
{theme}

大纲:
{outline}

注意事项:
{tips}

请根据上面的主题,大纲和注意事项，写一篇文章
"""


artical_prompt = ChatPromptTemplate.from_template(articalPromprtTempdate)

artical_chain = artical_prompt | model | str_output

query = "2023年中国经济形势分析"
# print(artical_chain.invoke({"theme":query,"outline":outline,"tips":tips}))

map_chain = RunnableParallel(outline=outline,tips=tips,theme=itemgetter("theme"))

# print(map_chain.invoke({"theme":query}))

all_chanin = map_chain | artical_chain | str_output

print(all_chanin.invoke({"theme":query}))