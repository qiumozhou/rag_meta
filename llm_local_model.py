from langchain.llms.base import LLM
from transformers import AutoTokenizer,AutoModel
from langchain_core.messages.ai import AIMessage

class ChatGPT5(LLM):
    max_tokens: int = 4096
    do_sampling: bool = True
    temperature: float = 0.3
    top_p: float = 0.0
    tokenlizer: object = None
    model: object = None
    history: list = []

    def __init__(self):
        super().__init__()

    @property
    def _llm_type(self):
        return "ChatGPT5"
    
    def load_model(self, modelPath=None):
        tokenlizer = AutoTokenizer.from_pretrained(modelPath,trust_remote_code=True,use_fast=True)

        model = AutoModel.from_pretrained(modelPath,trust_remote_code=True,device_map="auto")

        model = model.eval()

        self.model = model
        self.tokenlizer = tokenlizer

    
    def _call(self,prompt,config={},history=[]):
        return self.invoke(prompt,history)
    
    def invoke(self,prompt,config={},history=[]):
        if not isinstance(prompt,str):
            prompt = prompt.to_string()
        # print(1111,dir(self.model))
        response,history = self.model.chat(
            self.tokenlizer,
            prompt,
            history=history,
            do_sample = self.do_sampling,
            max_length = self.max_tokens,
        )
        self.history=history
        return AIMessage(content=response)
    
    def stream(self,prompt,config={},history={}):
        if not isinstance(prompt,str):
            prompt = prompt.to_string()
        preResponse = ""
        for response,new_history in self.model.stream_chat(
            self.tokenlizer,
            prompt
        ):
            if preResponse == "": 
                result = response
            else: 
                result = response[len(preResponse):]
            preResponse = response
            yield result


llm = ChatGPT5()
# model_path = "/mnt/workspace/chatglm3-6b"
# llm.load_model(model_path)
# llkm = llm.invoke("你好，我来自中国。")
# print(llkm)

# for response in llm.stream("写一首情诗"):
#     print(response, end = "")

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template("请根据下面的主题写一篇小红书营销的短文: {topic}")
out_parser = StrOutputParser()


chain = prompt | llm | out_parser
for chunk in chain.stream({"topic":"绿茶"}):
    print(chunk, end = "")