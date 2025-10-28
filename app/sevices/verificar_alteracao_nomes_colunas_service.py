from llm.llm_manager import LLMManager
from llm.prompt.prompt_verificar_alteracao_nomes_colunas import PromptVerificarAlteracaoNomesColunas




class VerificarAlteracaoNomesColunasService():
    def __init__(self):
        self._create_table_existente = None
        self._create_table_novo = None
        self._llm_model_name = None


    def set_llm_model_name(self, llm_model_name):
        self._llm_model_name = llm_model_name



    def set_create_table_existente(self, create_table_existente):
        self._create_table_existente = create_table_existente



    def set_create_table_novo(self, create_table_novo):
        self._create_table_novo = create_table_novo



    def run_llm(self,):
        prompt = PromptVerificarAlteracaoNomesColunas()
        prompt.set_create_table_existente(create_table_existente= self._create_table_existente )
        prompt.set_create_table_novo(create_table_novo= self._create_table_novo )
        template = prompt.run_montar_prompt()

        print(f'EXECUTANDO: {self.__class__.__name__}')
        # print(template)

        try:
            llm_manager = LLMManager()
            llm_manager.set_model(model= self._llm_model_name)
            llm_manager.set_template(template=template)
            llm_manager.set_question(question= "Retorne o pedido" )

            if self._llm_model_name == None:
                print("ERRO Falta preencher o Nome do Modelo LLM")
            if self._llm_model_name.startswith("gpt"):
                # Se estiver usando o ChatGPT
                resultado = llm_manager.run_open_ia()
            else:
                # Outras LLM
                resultado = llm_manager.run_ollama()
           
            return resultado
        except Exception as e:
            print(e)
            return False



