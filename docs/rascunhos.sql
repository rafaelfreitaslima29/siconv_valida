GPT:
	* Qualidade do retorno e bem preciso.
	* alter table e colocando um schema public com o schema 




select
	id,
	llm_model_name,
	inicio_execucao::timestamp,
	fim_execucao::timestamp,
	(fim_execucao::timestamp - inicio_execucao::timestamp) AS execucao,
	SUM( (fim_execucao::timestamp - inicio_execucao::timestamp) ) over (partition by llm_model_name) as total_execucao,
	EXTRACT(EPOCH FROM (fim_execucao::timestamp - inicio_execucao::timestamp))::numeric AS duracao_segundos,
	EXTRACT(EPOCH FROM AVG(fim_execucao::timestamp - inicio_execucao::timestamp) OVER (PARTITION BY llm_model_name)) AS media_segundos,
    AVG( (fim_execucao::timestamp - inicio_execucao::timestamp) ) over (PARTITION BY llm_model_name) AS media,
    385 as total,
    COUNT(*) OVER (PARTITION BY llm_model_name) AS total_execucoes_llm_model,
    ROUND(((  (COUNT(*) OVER (PARTITION BY llm_model_name)) / 385.0 ) * 100.0)::numeric, 2) ||'%' AS completou,
    385 - COUNT(*) OVER (PARTITION BY llm_model_name) as falta,
    resultado
FROM siconv_valida.tb_ajustes_tabela
order by 1 desc
;

	



select
	id,
	llm_model_name,
	inicio_execucao::timestamp,
	fim_execucao::timestamp,
	(fim_execucao::timestamp - inicio_execucao::timestamp) AS execucao,
	SUM( (fim_execucao::timestamp - inicio_execucao::timestamp) ) over (partition by llm_model_name) as total_execucao,
	EXTRACT(EPOCH FROM (fim_execucao::timestamp - inicio_execucao::timestamp))::numeric AS duracao_segundos,
	EXTRACT(EPOCH FROM AVG(fim_execucao::timestamp - inicio_execucao::timestamp) OVER (PARTITION BY llm_model_name)) AS media_segundos,
    AVG( (fim_execucao::timestamp - inicio_execucao::timestamp) ) over (PARTITION BY llm_model_name) AS media,
    385 as total,
    COUNT(*) OVER (PARTITION BY llm_model_name) AS total_execucoes_llm_model,
    ROUND(((  (COUNT(*) OVER (PARTITION BY llm_model_name)) / 385.0 ) * 100.0)::numeric, 2) ||'%' AS completou,
    385 - COUNT(*) OVER (PARTITION BY llm_model_name) as falta,
    resultado
FROM siconv_valida.tb_create_table_by_csv
order by 1 desc
;

	
	
	

	
select
	id,
	llm_model_name,
	inicio_execucao::timestamp,
	fim_execucao::timestamp,
	(fim_execucao::timestamp - inicio_execucao::timestamp) AS execucao,
	SUM( (fim_execucao::timestamp - inicio_execucao::timestamp) ) over (partition by llm_model_name) as total_execucao,
	EXTRACT(EPOCH FROM (fim_execucao::timestamp - inicio_execucao::timestamp))::numeric AS duracao_segundos,
	EXTRACT(EPOCH FROM AVG(fim_execucao::timestamp - inicio_execucao::timestamp) OVER (PARTITION BY llm_model_name)) AS media_segundos,
    AVG( (fim_execucao::timestamp - inicio_execucao::timestamp) ) over (PARTITION BY llm_model_name) AS media,
    385 as total,
    COUNT(*) OVER (PARTITION BY llm_model_name) AS total_execucoes_llm_model,
    ROUND(((  (COUNT(*) OVER (PARTITION BY llm_model_name)) / 385.0 ) * 100.0)::numeric, 2) ||'%' AS completou,
    385 - COUNT(*) OVER (PARTITION BY llm_model_name) as falta,
    resultado
FROM siconv_valida.tb_verificar_adicao_coluna
order by 1 desc
;

	
	
	
	
select
	id,
	llm_model_name,
	inicio_execucao::timestamp,
	fim_execucao::timestamp,
	(fim_execucao::timestamp - inicio_execucao::timestamp) AS execucao,
	SUM( (fim_execucao::timestamp - inicio_execucao::timestamp) ) over (partition by llm_model_name) as total_execucao,
	EXTRACT(EPOCH FROM (fim_execucao::timestamp - inicio_execucao::timestamp))::numeric AS duracao_segundos,
	EXTRACT(EPOCH FROM AVG(fim_execucao::timestamp - inicio_execucao::timestamp) OVER (PARTITION BY llm_model_name)) AS media_segundos,
    AVG( (fim_execucao::timestamp - inicio_execucao::timestamp) ) over (PARTITION BY llm_model_name) AS media,
    385 as total,
    COUNT(*) OVER (PARTITION BY llm_model_name) AS total_execucoes_llm_model,
    ROUND(((  (COUNT(*) OVER (PARTITION BY llm_model_name)) / 385.0 ) * 100.0)::numeric, 2) ||'%' AS completou,
    385 - COUNT(*) OVER (PARTITION BY llm_model_name) as falta,
    resultado
FROM siconv_valida.tb_verificar_alteracao_nome_coluna
order by 1 desc
;

	
	
	
	
	
	
	
select
	id,
	llm_model_name,
	inicio_execucao::timestamp,
	fim_execucao::timestamp,
	(fim_execucao::timestamp - inicio_execucao::timestamp) AS execucao,
	SUM( (fim_execucao::timestamp - inicio_execucao::timestamp) ) over (partition by llm_model_name) as total_execucao,
	EXTRACT(EPOCH FROM (fim_execucao::timestamp - inicio_execucao::timestamp))::numeric AS duracao_segundos,
	EXTRACT(EPOCH FROM AVG(fim_execucao::timestamp - inicio_execucao::timestamp) OVER (PARTITION BY llm_model_name)) AS media_segundos,
    AVG( (fim_execucao::timestamp - inicio_execucao::timestamp) ) over (PARTITION BY llm_model_name) AS media,
    385 as total,
    COUNT(*) OVER (PARTITION BY llm_model_name) AS total_execucoes_llm_model,
    ROUND(((  (COUNT(*) OVER (PARTITION BY llm_model_name)) / 385.0 ) * 100.0)::numeric, 2) ||'%' AS completou,
    385 - COUNT(*) OVER (PARTITION BY llm_model_name) as falta,
    resultado
FROM siconv_valida.tb_create_table_by_csv
order by 1 desc
;







select
	id,
	llm_model_name,
	inicio_execucao::timestamp,
	fim_execucao::timestamp,
	(fim_execucao::timestamp - inicio_execucao::timestamp) AS execucao,
	SUM( (fim_execucao::timestamp - inicio_execucao::timestamp) ) over (partition by llm_model_name) as total_execucao,
    AVG( (fim_execucao::timestamp - inicio_execucao::timestamp) ) over (PARTITION BY llm_model_name) AS media,
    385 as total,
    COUNT(*) OVER (PARTITION BY llm_model_name) AS total_execucoes_llm_model,
    ROUND(((  (COUNT(*) OVER (PARTITION BY llm_model_name)) / 385.0 ) * 100.0)::numeric, 2) ||'%' AS completou,
    385 - COUNT(*) OVER (PARTITION BY llm_model_name) as falta,
    resultado
FROM siconv_valida.tb_verificar_alteracao_nome_coluna
order by 1 desc
;


select
	id,
	llm_model_name,
	inicio_execucao::timestamp,
	fim_execucao::timestamp,
	(fim_execucao::timestamp - inicio_execucao::timestamp) AS execucao,
	SUM( (fim_execucao::siconv_valida.tb_ajustes_tabelatimestamp - inicio_execucao::timestamp) ) over (partition by llm_model_name) as total_execucao,
    AVG( (fim_execucao::timestamp - inicio_execucao::timestamp) ) over (PARTITION BY llm_model_name) AS media,
    385 as total,
    COUNT(*) OVER (PARTITION BY llm_model_name) AS total_execucoes_llm_model,
    ROUND(((  (COUNT(*) OVER (PARTITION BY llm_model_name)) / 385.0 ) * 100.0)::numeric, 2) ||'%' AS completou,
    385 - COUNT(*) OVER (PARTITION BY llm_model_name) as falta,
    resultado
FROM siconv_valida.tb_verificar_adicao_coluna
order by 1 desc
;



select
	id,
	llm_model_name,
	inicio_execucao::timestamp,
	fim_execucao::timestamp,
	(fim_execucao::timestamp - inicio_execucao::timestamp) AS tempo,
	SUM( (fim_execucao::timestamp - inicio_execucao::timestamp) ) over (partition by llm_model_name) as tempo_total_execucao,
    AVG( (fim_execucao::timestamp - inicio_execucao::timestamp) ) over (PARTITION BY llm_model_name) AS media,
    385 as total,
    COUNT(*) OVER (PARTITION BY llm_model_name) AS total_execucoes_llm_model,
    ROUND(((  (COUNT(*) OVER (PARTITION BY llm_model_name)) / 385.0 ) * 100.0)::numeric, 2) ||'%' AS completou,
    385 - COUNT(*) OVER (PARTITION BY llm_model_name) as falta,
    resultado
FROM siconv_valida.tb_ajustes_tabela
order by 1 desc
;



select
	id,
	llm_model_name,
	inicio_execucao::timestamp,
	fim_execucao::timestamp,
	(fim_execucao::timestamp - inicio_execucao::timestamp) AS tempo,
	SUM( (fim_execucao::timestamp - inicio_execucao::timestamp) ) over (partition by llm_model_name) as tempo_total_execucao,
    AVG( (fim_execucao::timestamp - inicio_execucao::timestamp) ) over (PARTITION BY llm_model_name) AS media,
    385 as total,
    COUNT(*) OVER (PARTITION BY llm_model_name) AS total_execucoes_llm_model,
    ROUND(((  (COUNT(*) OVER (PARTITION BY llm_model_name)) / 385.0 ) * 100.0)::numeric, 2) ||'%' AS completou,
    385 - COUNT(*) OVER (PARTITION BY llm_model_name) as falta,
    resultado
FROM siconv_valida.tb_verificar_adicao_coluna
order by 1 desc
;



SELECT id, llm_model_name, create_table_existente, create_table_novo, inicio_execucao, fim_execucao, resultado
FROM siconv_valida.tb_verificar_adicao_coluna;





select
	id,
	llm_model_name,
	inicio_execucao::timestamp,
	fim_execucao::timestamp,
	(fim_execucao::timestamp - inicio_execucao::timestamp) AS tempo,
	SUM( (fim_execucao::timestamp - inicio_execucao::timestamp) ) over (partition by llm_model_name) as tempo_total_execucao,
    AVG( (fim_execucao::timestamp - inicio_execucao::timestamp) ) over (PARTITION BY llm_model_name) AS media,
    385 as total,
    COUNT(*) OVER (PARTITION BY llm_model_name) AS total_execucoes_llm_model,
    ROUND(((  (COUNT(*) OVER (PARTITION BY llm_model_name)) / 385.0 ) * 100.0)::numeric, 2) ||'%' AS completou,
    385 - COUNT(*) OVER (PARTITION BY llm_model_name) as falta,
    resultado
from
	siconv_valida.tb_verificar_alteracao_nome_coluna
order by 1 desc
;







select
--	id,
	llm_model_name,
	count(llm_model_name),
	(count(llm_model_name) - 385) as falta
--	caminho_e_nome_csv,
--	nome_tabela_banco,
--	inicio_execucao,
--	fim_execucao,
--	resultado
from
	siconv_valida.tb_create_table_by_csv
group by llm_model_name 
	;




++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Prompt
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


Ajuste tabela
        self._txt_prompt         = """
Contexto
Você é um(a) especialista em bancos de dados relacionais (PostgreSQL) e em automação de ETL.
Sua tarefa é analisar dois comandos CREATE TABLE e sugerir os ajustes SQL necessários para adaptar a tabela existente no banco de dados (DDL atual) à nova estrutura (DDL novo).  
Os ajustes devem ser válidos e funcionais, garantindo a continuidade do processo de ingestão de dados sem perda ou corrupção de informações.

Objetivo
Gerar comandos SQL (ALTER TABLE) que tornem a estrutura atual compatível com o novo layout, de forma incremental e segura.

Entradas
- CREATE TABLE (atual, já existente no banco): 
[[DDL_ATUAL]]

- CREATE TABLE (novo, derivado do novo layout do CSV): 
[[DDL_NOVO]]

Regras e diretrizes obrigatórias
1. Compare os nomes das colunas, ignorando diferenças de tipos e constraints, mas preserve compatibilidade.
2. Se uma nova coluna existir no DDL novo e não no DDL atual → **gerar `ALTER TABLE ADD COLUMN`** com tipo compatível ao indicado no DDL novo.
3. Se uma coluna foi renomeada → **gerar `ALTER TABLE RENAME COLUMN antigo TO novo`**.
4. Se um tipo de dado for incompatível e o novo tipo for mais amplo (ex: `INTEGER → BIGINT` ou `VARCHAR(50) → TEXT`) → **gerar `ALTER TABLE ALTER COLUMN ... TYPE ...`**.
5. Nunca remova ou alterar drasticamente colunas existentes que possam causar perda de dados.
6. Ignore chaves primárias e constraints, a menos que sejam imprescindíveis para manter a integridade referencial.
7. Todos os comandos devem ser sintaticamente válidos em PostgreSQL.
8. Se não houver diferença estrutural, retorne uma mensagem clara informando que nenhum ajuste é necessário.
9. Proibido retornar qualquer código, incluindo Python, SQL, JSON, pseudocódigo ou trechos formatados como código.
10. Não retorne sua lógica de resolução, só a resolução.



Formato da saída (único formato permitido):

```sql
ALTER TABLE public.funcionarios
    ADD COLUMN data_admissao DATE,
    ADD COLUMN status_funcionario TEXT,
    RENAME COLUMN nome TO nome_completo,
    ALTER COLUMN salario TYPE NUMERIC(12,2);
```

Se não houver ajustes, retornar apenas:

Ajustes:
(nenhuma)

"""













        self._txt_prompt = """
Context
Compare two CREATE TABLE statements and identify changes only in column names.

Goal
Detect:

unchanged columns

renamed columns

added columns

removed columns

Comparison must consider column names only, ignoring types, constraints, defaults, comments, and column order.

Inputs

Current DDL: 

[[DDL_ATUAL]]

New DDL: 

[[DDL_NOVO]]

Normalization Rules (mandatory)

Compare column names without quotes, without accents, and case-insensitive.

Ignore everything except the column identifier.

If a name exists in both DDLs after normalization, treat it as unchanged.

For renames, use lexical/semantic similarity, but be conservative.

If uncertain, do not assume a rename — classify as removed + added.

What you must do

Extract and normalize column names from both DDLs.

Identify unchanged columns.

Try pairing columns exclusive to the current DDL with those exclusive to the new DDL to detect renames.

Anything not paired becomes:

added (only in new DDL)

removed (only in current DDL)

Output format (return only this)

Unchanged columns: [list]

Renamed columns:

from: X → to: Y

from: A → to: B

Added columns: [list]

Removed columns: [list]

Notes: short text when needed
"""





        self._txt_prompt = """
Contexto
Você é um(a) especialista em SQL (PostgreSQL) e comparação de esquemas. Sua tarefa é comparar dois comandos CREATE TABLE e identificar mudanças exclusivamente nos nomes das colunas, ignorando todos os demais detalhes.

Objetivo
Detectar colunas inalteradas, colunas renomeadas, colunas adicionadas e colunas removidas, considerando apenas os nomes das colunas (case-insensitive).
Se houver ambiguidade, adote postura conservadora e explique no campo “notes”.

Entradas

CREATE TABLE (atual): 

[[DDL_ATUAL]]

CREATE TABLE (novo): [[DDL_NOVO]]

Regras de Normalização (obrigatórias)

Comparar nomes de colunas sem aspas, sem acentos e case-insensitive
(ex.: "CPF", cpf, Cpf → cpf).

Ignorar tudo além do nome da coluna: tipo, NOT NULL, DEFAULT, CHECK, CONSTRAINT, comentário, PK/FK etc.

Ignorar a ordem das colunas.

Se um nome existir nos dois esquemas (após normalização), considerar como não alterado.

Para inferir renomeações:

Usar similaridade lexical/semântica.

Ex.: nome ↔ nome_completo; uf ↔ estado.

Ser conservador quando houver múltiplas opções plausíveis.

Procedimento

Extrair e normalizar os nomes das colunas dos dois DDLs.

Identificar colunas não alteradas.

Das colunas exclusivas do DDL atual, tentar pareá-las com as colunas exclusivas do DDL novo:

Se houver forte evidência, classificar como renomeada.

Caso contrário, classificar como removida.

Colunas exclusivas do DDL novo que não foram mapeadas como renomeações devem ser classificadas como adicionadas.

Retornar somente o bloco final de listas conforme o formato abaixo.

📌 Formato da saída (somente isso)

Colunas não alteradas: [lista]

Colunas renomeadas:

de: X → para: Y

de: A → para: B

Colunas adicionadas: [lista]

Colunas removidas: [lista]

Notes: texto breve (opcional, apenas quando necessário)

✨ Exemplo (mínimo)

Entrada: (DDL atual e novo conforme o exemplo original)

Saída esperada:

Colunas não alteradas: [id, cpf]

Colunas renomeadas:

de: nome → para: nome_completo

de: dt_nascimento → para: data_nascimento

Colunas adicionadas: []

Colunas removidas: []

Notes: Tipos e PK ignorados conforme instruções.
"""








++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
app.py
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# ROTA PÁGINA INICIAL
# @app.route("/comparacao")
# def pg_comparacao():
#     rotas = 'rotas'
#     return render_template('comparacao.html', rotas=rotas)



# ================================================================================================
#                   ROTAS DE MANUTENÇÃO DAS CARGAS E EXECUÇÃO DE TAREFAS
# ================================================================================================



# ================================================================================================
# ATUALIZAR CARGA DE DADOS FEDERAIS TRANSFERE GOV
# ================================================================================================
# @app.route('/carga_csv_convenios', methods=['GET'])
# def update_carga():
#     try:
#         url = 'https://repositorio.dados.gov.br/seges/detru/siconv.zip'
        
#         log.info("# => /carga_csv_convenios - Início atualização da carga de dados federais")

#         fd = FileDownloader()
#         fd.set_url(url=url)
#         fd.download()

#         log.info("# => => Base baixada")

#         log.info("# => => Início descompactação da base de dados")
#         # EXTRACT FILES
#         zip_path = "data/raw/siconv.zip"
#         extract_to = "data/extracted"
#         zm = ZipManager()
#         zm.extract(zip_path=zip_path, extract_to=extract_to)
#         log.info("# => => Base descompactada")
#         log.info("# => Atualização da carga de dados federais concluída com sucesso!")

#         return jsonify({
#             "status_post": 200,
#             "resposta_post": 'Atualização da carga de dados federais iniciada com sucesso!',
#         }), 200
#     except requests.exceptions.RequestException as e:
#         return jsonify({
#             "erro": "Erro ao atualizar base!",
#             "detalhes": str(e)
#         }), 500



# ================================================================================================
# ROTA TESTE MODELO 1
# ================================================================================================
# @app.route('/debug', methods=['GET'])
# def run_debug():

#     tam_amostra = TamanhoAmostra()
#     tam_amostra = tam_amostra.CalcularTamanhoAmostraProporcao()
#     log.info(f'Tamanho da Amostra:{tam_amostra}')

#     # for i in range(385): 1 vez 100 + 200
#     for i in range(39):
        
#         # 385
#         # service = AvaliacaoChatGPT_4o_Service()
#         # service.Run()

#         # 385
#         # service = AvaliacaoLlama_3_2_1b_Service()
#         # service.Run()

#         # 385 
#         # service = AvaliacaoLlama_3_2_3b_Service()
#         # service.Run()
        
#         # 385
#         # service = AvaliacaoLlama_3_1_8b_Service()
#         # service.Run()
        
#         log.info(f'====> EXECUÇÃO:{i}')

#     log.info("##### FIM ######" )

#     return jsonify({
#             "status_post": 200,
#             "resposta_post": f'- Debug Finalizado!',
#         }), 200
   




# ================================================================================================
# ROTA TESTE MODELO 1
# ================================================================================================
# @app.route('/verificacao_criacao_tb_csv', methods=['GET'])
# def run_verificacao_criacao_tb_csv():

#     verif = VerificarMetricas()
#     verif.Verificar()


#     log.info("##### FIM ######" )

#     return jsonify({
#             "status_post": 200,
#             "resposta_post": f'- Debug Finalizado!',
#         }), 200
   


# ================================================================================================
# ROTA TESTE MODELO 1
# ================================================================================================
# @app.route('/cenario_execucao', methods=['GET'])
# def run_cenario_execucao():
#     model = 'llama3.1:8b'
# #     # model = 'llama3.2:1b'
# #     # model = 'llama3.2:3b'
# #     # model = 'gpt-4o'

#     # Testar tamanho da amostra
#     calc_tam = TamanhoAmostra()
#     log.info(f"TAMANHO DA AMOSTRA: {calc_tam.CalcularTamanhoAmostraProporcao()}")

#     # Ajusta o Timezone
#     timezone = pytz.timezone('America/Sao_Paulo')
#     offset_hours = -3
#     offset = timedelta(hours=offset_hours)

#     log.info("##### INÍCIO ######" )pass
#     exec_start = timezone.localize(datetime.now() + offset ).strftime('%Y-%m-%d %H:%M:%S')

#     # DDL Tabela Banco de Dados
#     get_ddl = GetDDL()
#     db_ddl_create_table = get_ddl.Get()

#     # DDL CSV
#     path_and_file_csv = 'data/extracted/siconv_convenio.csv'
#     nome_tb_banco = 'pcr_siconv.tb_convenios'

#     create_csv_ddl = CSV2CreateTable()
#     csv_create_table = create_csv_ddl.GetCreateTabelByCSV(path_and_file_csv=path_and_file_csv, nome_tb_banco=nome_tb_banco, model_name=model)

#     tbdb_vs_tbcsv = TbDb_Vs_TbCSV()
#     result = tbdb_vs_tbcsv.GetComparison(csv_create_table=csv_create_table, db_ddl_create_table=db_ddl_create_table, model_name=model)
#     exec_end = timezone.localize(datetime.now() + offset ).strftime('%Y-%m-%d %H:%M:%S')

#     # SALVAR NO BANCO DE DADOS
#     model = TbComparacaoModel(
#         tb_name=nome_tb_banco, 
#         file_csv_name= path_and_file_csv, 
#         create_table_from_csv= csv_create_table,
#         create_table_from_table= db_ddl_create_table,
#         result= result,
#         exec_start= str(exec_start), 
#         exec_end= exec_end,
#         vlr_avaliacao = False
#     )

#     repository = TbComparacaoRepository()
#     repository.Insert(model=model)

#     # DEBUG
#     log.info(db_ddl_create_table)
#     log.info(csv_create_table)
#     # log.info(prompt)

#     log.info("##### FIM ######" )

#     return jsonify({
#             "status_post": 200,
#             "resposta_post": f'- Debug Finalizado!',
#         }), 200
   




# # ================================================================================================
# # ATUALIZAR CARGA DE DADOS FEDERAIS TRANSFERE GOV
# # ================================================================================================
# # ROTA PÁGINA INICIAL
# @app.route("/run_llama3_1_8b")
# def rota_testes():
#     # model = 'llama3.2:1b'
#     model = 'llama3.1:8b'
#     # model = 'llama3.2:3b'
#     # model = 'gpt-4o'
#     # model = 'gpt-4.1-nano'


#     path_and_file_csv = "data/extracted/siconv_convenio.csv"
#     nome_tb_banco = "pcr_siconv.tb_convenios"

#     prompt = PromptCsvCreateTable(path_and_file_csv=path_and_file_csv, nome_tb_banco=nome_tb_banco)

#     template = prompt.GetPrompt()

#     try:
#         llm_manager = LLMManager()
#         llm_manager.set_model(model=model)
#         llm_manager.set_template(template=template)
#         llm_manager.set_question(question= prompt.GetQuestion )
#         resultado = llm_manager.run()
#         # resultado = llm_manager.runOpenIA()
#         log.info(resultado)

#         # Data Hora de execução
#         data_hora = datetime.now()
#         data_hora = data_hora + timedelta(hours=-3)
#         data_hora = data_hora.strftime("%d/%m/%Y %H:%M")

#         return jsonify({
#             "status_post": 200,
#             "resposta_post": f'{ data_hora } - Teste Finalizado! \n{resultado}',
#         }), 200
#     # 
#     except requests.exceptions.RequestException as e:
#         return jsonify({
#             "erro": "Erro ao executar!",
#             "detalhes": str(e)
#         }), 500






=======================================================================================================================
# from sqlalchemy.sql.expression import select
# from sqlalchemy import update
# from sqlalchemy import delete

# from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey, Boolean
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
# from sqlalchemy.sql import func





    @classmethod
    def get_by_id(cls, db, id: int):
        """Método de classe para consultar por id"""
        return db.query(cls).filter(cls.id == id).first()



    @classmethod
    def get_all(cls, db):
        """Método de classe para obter todos os registros"""
        return db.query(cls).all()











# class TbComparacaoModel(Base):
#     '''Comparação de tabelas'''
#     __tablename__ = "tb_comparison"
#     __table_args__ = {'schema': 'dm'}

#     id                      = Column(Integer,   primary_key=True, index=True)
#     llm_model               = Column(Text,      nullable=False)
#     file_csv_name           = Column(Text,      nullable=False)
#     tb_name                 = Column(Text,      nullable=False)
#     create_table_from_csv   = Column(Text,      nullable=False)
#     create_table_from_table = Column(Text,      nullable=False)
#     result                  = Column(Text,      nullable=False)
#     exec_start              = Column(Text,      nullable=True)
#     exec_end                = Column(Text,      nullable=True)
#     vlr_avaliacao           = Column(Boolean,   nullable=False, default=False) 


#     def __repr__(self):
#         return f"<TbComparacaoModel(id={self.id}, llm_model={self.llm_model}, file_csv_name={self.file_csv_name}, tb_name={self.tb_name})>"



#     @classmethod
#     def Insert(cls, db,
#                llm_model:str,
#                file_csv_name: str,
#                tb_name: str, 
#                create_table_from_csv: str,
#                create_table_from_table: str, 
#                result: str, 
#                exec_start: str, 
#                exec_end: str, 
#                vlr_avaliacao:bool
#     ):
#         """Método de classe para criar um novo registro"""
#         model = cls(
#             llm_model               = llm_model,
#             file_csv_name           = file_csv_name,
#             tb_name                 = tb_name,
#             create_table_from_csv   = create_table_from_csv,
#             create_table_from_table = create_table_from_table,
#             result                  = result,
#             exec_start              = exec_start, 
#             exec_end                = exec_end,
#             vlr_avaliacao           = vlr_avaliacao 
#         )
#         db.add(model)
#         db.commit()
#         db.refresh(model)
#         return model



#     @classmethod
#     def get_by_id(cls, db, id: int):
#         """Método de classe para consultar por id"""
#         return db.query(cls).filter(cls.id == id).first()



#     @classmethod
#     def get_all(cls, db):
#         """Método de classe para obter todos os registros"""
#         return db.query(cls).all()



#     @classmethod
#     def update(cls, db, id: int, llm_model:str, file_csv_name: str, tb_name: str, create_table_from_csv: str,
#                create_table_from_table: str, result: str):
#         """Método de classe para atualizar um registro"""
#         model = db.query(cls).filter(cls.id == id).first()
#         if model:
#             model.llm_model = llm_model
#             model.file_csv_name = file_csv_name
#             model.tb_name = tb_name
#             model.create_table_from_csv = create_table_from_csv
#             model.create_table_from_table = create_table_from_table
#             model.result = result
#             db.commit()  # Commit para salvar as mudanças
#             db.refresh(model)
#             return model
#         return None



#     @classmethod
#     def delete(cls, db, id: int):
#         """Método de classe para deletar um registro"""
#         model = db.query(cls).filter(cls.id == id).first()
#         if model:
#             db.delete(model)
#             db.commit()
#             return True
#         return False




# # ================================================================================================
# # MODELO PARA ANÁLISE
# # ================================================================================================
# class TbAnaliseComparacaoModel(Base):
#     '''Análise da Comparação tabelas'''
#     __tablename__ = "tb_analise_comparacao"
#     __table_args__ = {'schema': 'analise'}

#     id                          = Column(Integer,   primary_key=True, index=True)
#     llm_model                   = Column(Text,      nullable=False)
#     file_csv_name               = Column(Text,      nullable=False)
#     tb_name                     = Column(Text,      nullable=False)
#     create_table_from_csv       = Column(Text,      nullable=False)
#     create_table_from_table     = Column(Text,      nullable=False)
#     result                      = Column(Text,      nullable=False)
#     exec_start                  = Column(Text,      nullable=True)
#     exec_end                    = Column(Text,      nullable=True)
#     bool_criou_ddl_csv          = Column(Text,      nullable=True)
#     bool_achou                  = Column(Boolean,   nullable=True)
#     bool_explicou               = Column(Boolean,   nullable=True)
#     bool_sql_retornado_resolve  = Column(Boolean,   nullable=True)


#     def __repr__(self):
#         return (
#             f"<TbAnaliseComparacaoModel("
#             f"id={self.id}, "
#             f"llm_model={self.llm_model}, "
#             f"file_csv_name={self.file_csv_name}, "
#             f"tb_name={self.tb_name}, "
#             f"create_table_from_csv={self.create_table_from_csv}, "
#             f"create_table_from_table={self.create_table_from_table}, "
#             f"result={self.result}, "
#             f"exec_start={self.exec_start}, "
#             f"exec_end={self.exec_end}, "
#             f"bool_criou_ddl_csv={self.bool_criou_ddl_csv}, "            
#             f"bool_achou={self.bool_achou}, "
#             f"bool_explicou={self.bool_explicou}, "
#             f"bool_sql_retornado_resolve={self.bool_sql_retornado_resolve}"
#             f")>"
#         )



#     @classmethod
#     def Insert(cls, db,
#         llm_model:str,
#         file_csv_name: str,
#         tb_name: str, 
#         create_table_from_csv: str,
#         create_table_from_table: str, 
#         result: str, 
#         exec_start: str, 
#         exec_end: str,
#         bool_criou_ddl_csv:bool,
#         bool_achou:bool,
#         bool_explicou:bool,
#         bool_sql_retornado_resolve:bool
#     ):
#         """Método de classe para criar um novo registro"""
#         model = cls(
#             llm_model                  = llm_model,
#             file_csv_name              = file_csv_name,
#             tb_name                    = tb_name,
#             create_table_from_csv      = create_table_from_csv,
#             create_table_from_table    = create_table_from_table,
#             result                     = result,
#             exec_start                 = exec_start, 
#             exec_end                   = exec_end,
#             bool_criou_ddl_csv         = bool_criou_ddl_csv,
#             bool_achou                 = bool_achou,
#             bool_explicou              = bool_explicou,
#             bool_sql_retornado_resolve = bool_sql_retornado_resolve
#         )
#         db.add(model)
#         db.commit()
#         db.refresh(model)
#         return model



#     @classmethod
#     def get_by_id(cls, db, id: int):
#         """Método de classe para consultar por id"""
#         return db.query(cls).filter(cls.id == id).first()



#     @classmethod
#     def get_all(cls, db):
#         """Método de classe para obter todos os registros"""
#         return db.query(cls).all()



#     @classmethod
#     def update(cls, db, 
#         id: int, 
#         llm_model:str, 
#         file_csv_name: str, 
#         tb_name: str, 
#         create_table_from_csv: str,
#         create_table_from_table: str, 
#         result: str,
#         bool_criou_ddl_csv:bool,
#         bool_achou:bool, 
#         bool_explicou:bool, 
#         bool_sql_retornado_resolve:bool
#     ):
#         """Método de classe para atualizar um registro"""
#         model = db.query(cls).filter(cls.id == id).first()
#         if model:
#             model.llm_model                  = llm_model
#             model.file_csv_name              = file_csv_name
#             model.tb_name                    = tb_name
#             model.create_table_from_csv      = create_table_from_csv
#             model.create_table_from_table    = create_table_from_table
#             model.result                     = result
#             model.bool_criou_ddl_csv         = bool_criou_ddl_csv
#             model.bool_achou                 = bool_achou
#             model.bool_explicou              = bool_explicou
#             model.bool_sql_retornado_resolve = bool_sql_retornado_resolve
#             db.commit() 
#             db.refresh(model)
#             return model
#         return None



#     @classmethod
#     def delete(cls, db, id: int):
#         """Método de classe para deletar um registro"""
#         model = db.query(cls).filter(cls.id == id).first()
#         if model:
#             db.delete(model)
#             db.commit()
#             return True
#         return False









    # @classmethod
    # def update(cls, db, id: int, 
    #     llm_model_name:str,
    #     caminho_e_nome_csv:str,
    #     nome_tabela_banco:str,
    #     inicio_execucao:str,
    #     fim_execucao:str,
    #     resultado:str
    #     ):
    #     """Método de classe para atualizar um registro"""
    #     model = db.query(cls).filter(cls.id == id).first()
    #     if model:
    #         model.llm_model_name = llm_model_name
    #         model.caminho_e_nome_csv = caminho_e_nome_csv
    #         model.nome_tabela_banco = nome_tabela_banco
    #         model.inicio_execucao = inicio_execucao
    #         model.fim_execucao = fim_execucao
    #         model.resultado = resultado
    #         db.commit()  # Commit para salvar as mudanças
    #         db.refresh(model)
    #         return model
    #     return None

