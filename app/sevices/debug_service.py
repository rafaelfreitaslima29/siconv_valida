from llm.llm_manager import LLMManager
from utils.file_downloader import FileDownloader
from utils.zip_manager import ZipManager
from llm.prompt.prompt_create_table_by_csv import PromptCreateTableCsv



# ================================================================================================
#                               SERVICE DEBUG
# ================================================================================================
class DebugService():
    def __init__(self):
        pass

    # ================================================================================================
    # Executa a FileDownloader
    # ================================================================================================
    def RunFileDownloader(self):
        url = 'https://repositorio.dados.gov.br/seges/detru/siconv.zip'
        name = "arquivos.zip"
        
        fd = FileDownloader()
        fd.set_url(url=url)
        fd.set_file_name(name=name)
        fd.run_download()


    # ================================================================================================
    # Executa ZipManager
    # ================================================================================================
    def RunZipManager(self):
        zip_path="files/csv/arquivos.zip"
        extract_to="files/descompactados"
        zm = ZipManager()
        zm.run_extract(zip_path=zip_path, extract_to=extract_to)


    # ================================================================================================
    # Executa PromptCreateTableCsv
    # ================================================================================================
    def RunPromptCreateTableCsv(self):
        pctb = PromptCreateTableCsv()

        pctb.set_caminho_e_nome_csv(caminho_e_nome_csv="files/descompactados/siconv_convenio.csv")
        pctb.set_nome_tabela_banco(nome_tabela_banco="tb_convenios")

        prompt = pctb.run_montar_prompt()
        print(prompt)





    # ================================================================================================
    # Executa a rotina
    # ================================================================================================
    def Run(self):
        llm_m = LLMManager()
        retorno = llm_m.runOllama()
        return retorno


