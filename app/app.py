# ================================================================================================
#                                ATIVIDADES DO PROJETO
# ================================================================================================
# [X] Download automático do arquivo ZIP contendo os arquivos CSV
# [X] Extração dos arquivos arquivos CSV do arquivo ZIP
# [X] Criar o LLM MANAGER para facilitar a interação com as LLM
# [x] Criar script para a montagem do PROMPT para traduzir o arquivo CSV em um DDL de criação de uma tabela para o PostgreSQL
#   * [x] Recuperar o nome das colunas do CSV;
#   * [x] Recuperar 4 primeiras linhas do CSV;
#   * [x] Mecanismo de inclusão do nome da tabela do banco de dados;
# [X] Criar Script para extrair o DDL da tabela do banco de dados.
# [X] Criar script para a montagem do PROMPT para comparar os DDLs do CSV como o do Banco de dados e verificar mudanças.
# [X] Criar Script para salvar os resultados das verificações no banco de dados.
#   * [X] Criar Model para salvar os resultados da execução.
# [DEV] Criar uma interface Web para realizar a verificação das comparações entre DDLs.
# [X] Criar um Script para calcular o tamanho da amostra de execuções dos LLMs.
# [X] Criar um Script para executar cada um dos quatros Modelos LLM.
#   * [X] Llama3.1:8b
#   * [X] Llama3.2:3b
#   * [X] Llama3.2:1b
#   * [X] gpt-4o
# [ ] Criar um Script analisar os dados.
#   * [ ] Levantar tamanho da amostra por Modelo de LLM
#   * [ ] Métrica 1: Achou o problema e explicou?
#   * [ ] Métrica 2: SQL que funciona e resolve o problema.
# [ ] Criar mecânica para usuário realizar a comparação dos DDLs


#
# ================================================================================================
# ================================================================================================
# PARA O Flesk
from flask import Flask, render_template, Response, request, url_for, redirect, send_from_directory, jsonify
import requests
import json
from sqlalchemy import text
from db.databases import engine
from db.models.models import Base
from db.models.models import Base as bases
from services.create_table_by_csv_service import CreateTableByCsvService
from services.verificar_alteracao_nomes_colunas_service import VerificarAlteracaoNomesColunasService
from services.verificar_adicao_colunas_service import VerificarAdicaoColunasService
from services.comparar_create_tables_service import CompararCreateTableService
from services.debug_service import DebugService
from utils.time_util import TimeUtil
from experimento.exp_create_table_by_csv_llama_3_2_1b_service import ExpCreateTableByCsvLLama3_2_1bService
from experimento.exp_create_table_by_csv_llama_3_2_3b_service import ExpCreateTableByCsvLLama3_2_3bService
from experimento.exp_create_table_by_csv_llama_3_1_8b_service import ExpCreateTableByCsvLLama3_1_8bService
from experimento.exp_verificar_alteracao_nomes_colunas_llama_3_2_1b_service import ExpVerificarAlteracaoNomesColunasLLama_3_2_1b_service
from experimento.exp_verificar_alteracao_nomes_colunas_llama_3_2_3b_service import ExpVerificarAlteracaoNomesColunasLLama_3_2_3b_service
from experimento.exp_verificar_alteracao_nomes_colunas_llama_3_1_8b_service import ExpVerificarAlteracaoNomesColunasLLama_3_1_8b_service
# from app_log.AppLog import AppLog
# BANCO DE DADOS
# from sqlalchemy import text
# from src.db.models.models import TbComparacaoModel
# from src.db.models.models import Base
# from src.db.databases import engine
# MANIPULAÇÃO DE ARQUIVOS
# from src.utils.file_downloader import FileDownloader
# from src.utils.zip_manager import ZipManager
# AVALIAÇÃO
# from experimento.estatistica.tamanho_amostra import TamanhoAmostra
# from experimento.db.models.models import Base as experimento_Base
# from experimento.avaliacao.verificar_metrica import VerificarMetricas


# ================================================================================================
#                       APP CONFIG
# ================================================================================================

# Configura a estrutura do banco de dados
def CriarEstruturaBancoDados():
    with engine.connect() as conn:
        conn.execute( text('CREATE SCHEMA IF NOT EXISTS siconv_valida;') )
        conn.commit()
    Base.metadata.create_all(engine)

    bases.metadata.create_all(engine)

CriarEstruturaBancoDados()

# ================================================================================================
#                       CONFIG FLASK
# ================================================================================================

UPLOAD_FOLDER                       =  'uploads'
ALLOWED_EXTENSIONS                  = {'csv'}
MODELOS_PATH                        = 'modelos'
RESULTADOS_PATH                     = 'resultados'

app = Flask(__name__)
app.config['UPLOAD_FOLDER']         = UPLOAD_FOLDER

# ================================================================================================
#                            ROTAS
# ================================================================================================

# ROTA PÁGINA INICIAL
@app.route("/")
def index():
    rotas = [
        {
            "nome": "/run_exp_verificar_alteracao_nomes_colunas_llama_3_1_8b", 
            "link": "/run_exp_verificar_alteracao_nomes_colunas_llama_3_1_8b"
        },
        {
            "nome": "/run_exp_verificar_alteracao_nomes_colunas_llama_3_2_3b", 
            "link": "/run_exp_verificar_alteracao_nomes_colunas_llama_3_2_3b"
        },
        {
            "nome": "/run_exp_verificar_alteracao_nomes_colunas_llama_3_2_1b", 
            "link": "/run_exp_verificar_alteracao_nomes_colunas_llama_3_2_1b"
        },
        {
            "nome": "/run_exp_create_table_by_csv_llama_3_1_8b", 
            "link": "/run_exp_create_table_by_csv_llama_3_1_8b"
        },
        {
            "nome": "/run_exp_create_table_by_csv_llama_3_2_3b", 
            "link": "/run_exp_create_table_by_csv_llama_3_2_3b"
        },
        {
            "nome": "/run_exp_create_table_by_csv_llama_3_2_1b", 
            "link": "/run_exp_create_table_by_csv_llama_3_2_1b"
        },
        {
            "nome": "DEBUG DE CÓDIGO", 
            "link": "/debug"
        },
        {
            "nome": "run_create_csv llama3.2:1b", 
            "link": "/run_create_csv_llama3_2_1b"
        } ,
        {
            "nome": "run_verificar_alteracao_nomes_colunas_llama3_2_1b", 
            "link": "/run_verificar_alteracao_nomes_colunas_llama3_2_1b"
        }
        ,
        {
             "nome": "/run_verificar_adicao_coluna_llama3_2_1b", 
             "link": "/run_verificar_adicao_coluna_llama3_2_1b"
        },
        {
            "nome": "/run_prompt_verificar_adicao_coluna_llama3_2_1b", 
            "link": "/run_prompt_verificar_adicao_coluna_llama3_2_1b"
        },
        {
            "nome": "/run_comparar_create_table_llama3_2_1b", 
            "link": "/run_comparar_create_table_llama3_2_1b"
        },
        {
            "nome": "/run_time_util",
            "link": "/run_time_util"
        }
    ]

    return render_template('lista_rotas.html', rotas=rotas)





# ================================================================================================
# ROTA DEBUG
# ================================================================================================
@app.route('/debug', methods=['GET'])
def run_debug():
    # ds = DebugService()
    # ds.RunFileDownloader()
   
    # ds.RunZipManager()

    # ds.RunPromptCreateTableCsv()

    # ds.RunCreateTableByCSV()

    # ds.RunPromptVerificarAlteracaoNomesColunas()

    # ds.RunPromptVerificarAdicaoColunas()

    # ds.RunPromptAjustesTable()


    caminho_e_nome_csv="files/descompactados/siconv_convenio.csv"
    nome_tabela_banco="tb_convenios"
    llm_model_name="llama3.2:1b"

    cts = CreateTableByCsvService()
    cts.set_caminho_e_nome_csv(caminho_e_nome_csv=caminho_e_nome_csv)
    cts.set_nome_tabela_banco(nome_tabela_banco=nome_tabela_banco)
    cts.set_llm_model_name(llm_model_name=llm_model_name)

    html = cts.run_llm()
    print(html)

    print("Terminou a execução!!")

    return Response(html, mimetype="text/html")










# ================================================================================================
# ROTA LLAMA3.2:1b rum create table csv
# ================================================================================================
@app.route('/run_create_csv_llama3_2_1b', methods=['GET'])
def run_llama3_2_1b():
    caminho_e_nome_csv="files/descompactados/siconv_convenio.csv"
    nome_tabela_banco="tb_convenios"
    llm_model_name="llama3.2:1b"

    cts = CreateTableByCsvService()
    cts.set_caminho_e_nome_csv(caminho_e_nome_csv=caminho_e_nome_csv)
    cts.set_nome_tabela_banco(nome_tabela_banco=nome_tabela_banco)
    cts.set_llm_model_name(llm_model_name=llm_model_name)

    html = cts.run_llm()
    print(html)

    print("Terminou a execução!!")

    return Response(html, mimetype="text/html")






# ================================================================================================
# ROTA LLAMA3.2:1b verificar_alteracao_nomes_colunas
# ================================================================================================
@app.route('/run_verificar_alteracao_nomes_colunas_llama3_2_1b', methods=['GET'])
def run_verificar_alteracao_nomes_colunas_llama3_2_1b():
    llm_model_name="llama3.2:1b"
    
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

    service = VerificarAlteracaoNomesColunasService()
    service.set_llm_model_name(llm_model_name= llm_model_name)
    service.set_create_table_existente(create_table_existente= create_table_existente)
    service.set_create_table_novo(create_table_novo= create_table_novo)

    html = service.run_llm()
    print(html)

    print("Terminou a execução!!")

    return Response(html, mimetype="text/html")






# ================================================================================================
# ROTA LLAMA3.2:1b PROMPT verificar_alteracao_nomes_colunas
# ================================================================================================
@app.route('/run_prompt_verificar_adicao_coluna_llama3_2_1b', methods=['GET'])
def run_prompt_verificar_adicao_coluna_llama3_2_1b():
    llm_model_name="llama3.2:1b"
    
    create_table_existente = """
    CREATE TABLE public.servidores (
        id SERIAL PRIMARY KEY,
        nome TEXT NOT NULL,
        cpf VARCHAR(11),
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

    debug = DebugService()

    prompt = debug.RunPromptVerificarAdicaoColunas()
    
    print(prompt)

    print("Terminou a execução!!")

    return Response("<p>CERTO</p>", mimetype="text/html")




# ================================================================================================
# ROTA LLAMA3.2:1b verificar_alteracao_nomes_colunas
# ================================================================================================
@app.route('/run_verificar_adicao_coluna_llama3_2_1b', methods=['GET'])
def run_verificar_adicao_coluna_llama3_2_1b():
    llm_model_name="llama3.2:1b"
    
    create_table_existente = """
    CREATE TABLE public.servidores (
        id SERIAL PRIMARY KEY,
        nome TEXT NOT NULL,
        cpf VARCHAR(11),
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

    service = VerificarAdicaoColunasService()
    service.set_llm_model_name(llm_model_name= llm_model_name)
    service.set_create_table_existente(create_table_existente= create_table_existente)
    service.set_create_table_novo(create_table_novo= create_table_novo)

    html = service.run_llm()
    print(html)

    print("Terminou a execução!!")

    return Response(html, mimetype="text/html")




# ================================================================================================
# ROTA LLAMA3.2:1b comparar create table
# ================================================================================================
@app.route('/run_comparar_create_table_llama3_2_1b', methods=['GET'])
def run_comparar_create_table_llama3_2_1b():
    llm_model_name="llama3.2:1b"
    
    create_table_existente = """
    CREATE TABLE public.servidores (
        id SERIAL PRIMARY KEY,
        nome TEXT NOT NULL,
        cpf VARCHAR(11),
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

    service = CompararCreateTableService()
    service.set_llm_model_name(llm_model_name= llm_model_name)
    service.set_create_table_existente(create_table_existente= create_table_existente)
    service.set_create_table_novo(create_table_novo= create_table_novo)

    html = service.run_llm()
    print(html)

    print("Terminou a execução!!")

    return Response(html, mimetype="text/html")





# ================================================================================================
# ROTA TimeUtil
# ================================================================================================
@app.route('/run_time_util', methods=['GET'])
def run_time_util():
    tu = TimeUtil()
    inicio = tu.get_time()
    tu.pause(5)
    fim = tu.get_time()


    html = f'<p>{inicio}  {fim}</p>'
    print(html)

    print("Terminou a execução!!")

    return Response(html, mimetype="text/html")





# ================================================================================================
# ROTA Experiemnto Create Table by CSV LLama 3.2 1b
# ================================================================================================
@app.route('/run_exp_create_table_by_csv_llama_3_2_1b', methods=['GET'])
def run_exp_create_table_by_csv_llama_3_2_1b():

    for i in range(385):
        experimento = ExpCreateTableByCsvLLama3_2_1bService()
        experimento.run()
        print(f'Execução: {i +1}')

    html = '<p>Terminou</p>'
    print(html)

    print("Terminou a execução!!")

    return Response(html, mimetype="text/html")



# ================================================================================================
# ROTA Experiemnto Create Table by CSV LLama 3.2 3b
# ================================================================================================
@app.route('/run_exp_create_table_by_csv_llama_3_2_3b', methods=['GET'])
def run_exp_create_table_by_csv_llama_3_2_3b():

    for i in range(385):
        experimento = ExpCreateTableByCsvLLama3_2_3bService()
        experimento.run()
        print(f'Execução: {i +1}')

    html = '<p>Terminou</p>'
    print(html)

    print("Terminou a execução!!")

    return Response(html, mimetype="text/html")



# ================================================================================================
# ROTA Experiemnto Create Table by CSV LLama 3.1 8b
# ================================================================================================
@app.route('/run_exp_create_table_by_csv_llama_3_1_8b', methods=['GET'])
def run_exp_create_table_by_csv_llama_3_1_8b():

    # for i in range(385):
    
    for i in range(324):
        experimento = ExpCreateTableByCsvLLama3_1_8bService()
        experimento.run()
        print(f'Execução: {i +1}')

    html = '<p>Terminou</p>'
    print(html)

    print("Terminou a execução!!")

    return Response(html, mimetype="text/html")




# ================================================================================================
# ROTA Experiemnto Verificar Alterações de Nomes Colunas LLama 3.2 1b
# ================================================================================================
@app.route('/run_exp_verificar_alteracao_nomes_colunas_llama_3_2_1b', methods=['GET'])
def run_exp_verificar_alteracao_nomes_colunas_llama_3_2_1b():

    # for i in range(385):
    
    for i in range(61):
        experimento = ExpVerificarAlteracaoNomesColunasLLama_3_2_1b_service()
        experimento.run()
        print(f'Execução: {i +1}')

    html = '<p>Terminou</p>'
    print(html)

    print("Terminou a execução!!")

    return Response(html, mimetype="text/html")



# ================================================================================================
# ROTA Experiemnto Verificar Alterações de Nomes Colunas LLama 3.2 3b
# ================================================================================================
@app.route('/run_exp_verificar_alteracao_nomes_colunas_llama_3_2_3b', methods=['GET'])
def run_exp_verificar_alteracao_nomes_colunas_llama_3_2_3b():

    # for i in range(385):    
    for i in range(15):
        experimento = ExpVerificarAlteracaoNomesColunasLLama_3_2_3b_service()
        experimento.run()
        print(f'Execução: {i +1}')

    html = '<p>Terminou</p>'
    print(html)

    print("Terminou a execução!!")

    return Response(html, mimetype="text/html")



# ================================================================================================
# ROTA Experiemnto Verificar Alterações de Nomes Colunas LLama 3.1 8b
# ================================================================================================
@app.route('/run_exp_verificar_alteracao_nomes_colunas_llama_3_1_8b', methods=['GET'])
def run_exp_verificar_alteracao_nomes_colunas_llama_3_1_8b():

    # for i in range(385):    
    for i in range(1):
        experimento = ExpVerificarAlteracaoNomesColunasLLama_3_1_8b_service()
        experimento.run()
        print(f'Execução: {i +1}')

    html = '<p>Terminou</p>'
    print(html)

    print("Terminou a execução!!")

    return Response(html, mimetype="text/html")





