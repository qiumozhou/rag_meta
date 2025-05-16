from zhipuai import ZhipuAI

llm = ZhipuAI(api_key="")

prompt = "写一遍关于爱的文章"

response = llm.chat.completions.create(
    model="glm-4",
    messages=[{
        "role":"user","content":"你好"
    },{
        "role":"assistant","content":"我是人工智能助手"
    },{
        "role":"user","content":prompt 
    }],
    stream=True
)
for chunk in response:
    print(chunk.choices[0].delta.content,end="")