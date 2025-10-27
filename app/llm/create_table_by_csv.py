from llm.llm_manager import LLMManager
from llm.prompt.prompt_create_table_by_csv import PromptCreateTableCsv


# from src.llm.prompt.prompt_csv_create_tb import PromptCsvCreateTable


class CreateTableByCSV():
    def __init__(self):
        self._caminho_e_nome_csv = None
        self._nome_tabela_banco = None
        self._llm_model_name = None



    def set_caminho_e_nome_csv(self, caminho_e_nome_csv):
        self._caminho_e_nome_csv = caminho_e_nome_csv



    def set_nome_tabela_banco(self, nome_tabela_banco):
        self._nome_tabela_banco = nome_tabela_banco



    def set_llm_model_name(self, llm_model_name):
        self._llm_model_name = llm_model_name



    def run_create_table_by_csv(self,):
        prompt = PromptCreateTableCsv()
        prompt.set_caminho_e_nome_csv(caminho_e_nome_csv= self._caminho_e_nome_csv)
        prompt.set_nome_tabela_banco(nome_tabela_banco= self._nome_tabela_banco)
        template = prompt.run_montar_prompt()

        try:
            llm_manager = LLMManager()
            llm_manager.set_model(model=self._llm_model_name)
            llm_manager.set_template(template=template)

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

            print(resultado)

            return resultado
        except Exception as e:
            return False



