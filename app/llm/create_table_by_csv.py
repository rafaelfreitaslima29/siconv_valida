# from app_log.AppLog import AppLog
from src.llm.prompt.prompt_csv_create_tb import PromptCsvCreateTable
from llm.llm_manager import LLMManager


class CreateTableByCSV():
    def __init__(self):
        pass
        # self._log = log = AppLog(name="src/llm/CSV2CreateTable.py").get_logger()



    def run_create_table_by_csv(self, caminho_csv:str="", nome_tabela_banco:str = "", model_name:str = ""):
        # path_and_file_csv = "data/extracted/siconv_convenio.csv"
        # nome_tb_banco = "pcr_siconv.tb_convenios"

        prompt = PromptCsvCreateTable(path_and_file_csv=caminho_csv, nome_tb_banco=nome_tabela_banco)
        template = prompt.GetPrompt()

        try:
            llm_manager = LLMManager()
            llm_manager.set_model(model=model_name)
            llm_manager.set_template(template=template)
            llm_manager.set_question(question= prompt.GetQuestion() )
             
            if model_name.startswith("gpt"):
                # Se estiver usando o ChatGPT
                resultado = llm_manager.runOpenIA()
            else:
                # Outras LLM
                resultado = llm_manager.run()
            
            self._log.info(resultado)

            return resultado

        except Exception as e:
            self._log.info(e)
            return False

