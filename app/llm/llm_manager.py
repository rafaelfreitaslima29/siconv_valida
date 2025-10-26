import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser


class LLMManager:
    def __init__(self):
        self._model = "llama3.2:1b"
        self._template = '''Question: {question}
                Answer: 
                    # A retorne uma aviso que o template não foi configurado'''
        self._question = "Avise também que a question não foi configurada."

        load_dotenv()

        key_api = os.getenv('OPENAI_API_KEY')
        # usando no caso do código no Virtul Box e Ollama na maquina HOST
        # is_vbox_use = os.getenv('USE_VIRTUAL_BOX')
        # self._vbox_use = is_vbox_use.lower() in ("true", "1", "yes", "on", "sim")
        os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')



    def set_model(self, model:str):
        self._model = model


    def set_template(self, template:str):
        self._template = template


    def set_question(self, question:str):
        self._question = question


    def runOllama(self):
        prompt = ChatPromptTemplate.from_template(self._template)
        
        # if self._vbox_use:
        #     # USADO CASO ESTIVER USANDO NO VITUAL BOX
        #     model = OllamaLLM(
        #         model=self._model, 
        #         base_url='http://10.0.2.2:11434'
        #     ) 
        # else:
        # OLLAMA NA MESMA MAQUINA
        model = OllamaLLM( model=self._model )

        chain = prompt | model
        txt = chain.invoke({"question": self._question })
        return txt



    def runOpenIA(self):
        prompt =  PromptTemplate( 
            input_variables= ["question"],
            template=self._template
        )
        model = ChatOpenAI(model= self._model, temperature=0.7)
        chain = prompt | model | StrOutputParser()
        txt = chain.invoke({"question": self._question })
        return txt
