from llm.llm_manager import LLMManager
from utils.file_downloader import FileDownloader
from utils.zip_manager import ZipManager
from llm.prompt.prompt_create_table_by_csv import PromptCreateTableCsv
from llm.prompt.prompt_verificar_alteracao_nomes_colunas import PromptVerificarAlteracaoNomesColunas
from llm.prompt.prompt_verificar_adicao_colunas import PromptVerificarAdicaoColunas
from llm.create_table_by_csv import CreateTableByCSV




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
    # Executa PromptVerificarAlteracaoNomesColunas
    # ================================================================================================
    def RunPromptVerificarAlteracaoNomesColunas(self):
        create_table_existente = """
CREATE TABLE public.servidores (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    cpf VARCHAR(11),
    cargo TEXT,
    salario NUMERIC(10,2)
);
        """

        create_table_novo = """
CREATE TABLE public.servidores (
    id SERIAL PRIMARY KEY,
    nome_completo TEXT NOT NULL,
    cpf VARCHAR(11),
    funcao TEXT,
    remuneracao NUMERIC(12,2)
);
        """
        prmpt_make = PromptVerificarAlteracaoNomesColunas()
        prmpt_make.set_create_table_existente(create_table_existente=create_table_existente)
        prmpt_make.set_create_table_novo(create_table_novo=create_table_novo)

        prompt = prmpt_make.run_montar_prompt()
        print(prompt)




    # ================================================================================================
    # Executa PromptVerificarAdicaoColunas
    # ================================================================================================
    def RunPromptVerificarAdicaoColunas(self):
        create_table_existente = """
CREATE TABLE public.servidores (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    cpf VARCHAR(11),
    cargo TEXT,
    remuneracao NUMERIC(12,2)
);
        """

        create_table_novo = """
CREATE TABLE public.servidores (
    id SERIAL PRIMARY KEY,
    nome_completo TEXT NOT NULL,
    cpf VARCHAR(11),
    cargo TEXT,
    categoria TEXT,
    remuneracao NUMERIC(12,2)
);
        """
        prmpt_make = PromptVerificarAlteracaoNomesColunas()
        prmpt_make.set_create_table_existente(create_table_existente=create_table_existente)
        prmpt_make.set_create_table_novo(create_table_novo=create_table_novo)

        prompt = prmpt_make.run_montar_prompt()
        print(prompt)








    # ================================================================================================
    # Executa CreateTableByCSV
    # ================================================================================================
    def RunCreateTableByCSV(self):
        caminho_e_nome_csv="files/descompactados/siconv_convenio.csv"
        nome_tabela_banco="tb_convenios"
        llm_model_name="llama3.2:1b"

        ctbc = CreateTableByCSV()
        ctbc.set_caminho_e_nome_csv(caminho_e_nome_csv= caminho_e_nome_csv)
        ctbc.set_nome_tabela_banco(nome_tabela_banco= nome_tabela_banco)
        ctbc.set_llm_model_name(llm_model_name=llm_model_name)
        resultado_llm = ctbc.run_create_table_by_csv()
        print(resultado_llm)





    # ================================================================================================
    # Executa a rotina
    # ================================================================================================
    def Run(self):
        llm_m = LLMManager()
        retorno = llm_m.runOllama()
        return retorno


