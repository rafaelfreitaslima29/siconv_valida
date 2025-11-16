from utils.csv_util import CSVUtil



class PromptVerificarAlteracaoNomesColunas():
    def __init__(self):
        self._create_table_existente = None
        self._create_table_novo = None
        self._txt_prompt = """
Contexto:
Compare dois comandos CREATE TABLE e identifique apenas renomeações de colunas, ignorando todos os outros aspectos.

Entrada

DDL atual: 
[[DDL_ATUAL]]

DDL novo: 
[[DDL_NOVO]]


Regras obrigatórias:

Compare nomes de colunas sem aspas, sem acentos e ignorando maiúsculas/minúsculas.

Ignore tipos, chaves, defaults, comentários, ordem das colunas etc.

Para decidir se uma coluna foi renomeada, use similaridade lexical/semântica.

Seja conservador: se houver dúvida, não classifique como renomeação.

Não retorne colunas adicionadas, removidas ou inalteradas — apenas renomeações.

Proibido retornar qualquer código, incluindo Python, SQL, JSON, pseudocódigo ou trechos formatados como código.


O que deve fazer:

Extrair e normalizar apenas os nomes das colunas dos dois DDLs.

Detectar correspondências prováveis de renomeação entre nomes exclusivos do DDL atual e nomes exclusivos do DDL novo.

Retornar somente a lista de renomeações no formato abaixo.


Formato da saída (único formato permitido):

Renomeações de colunas:
de: NOME_ANTIGO → para: NOME_NOVO
de: OUTRO_ANTIGO → para: OUTRO_NOVO


Se não houver renomeações, retornar apenas:

Renomeações de colunas:
(nenhuma)
"""



    def set_create_table_existente(self, create_table_existente):
        self._create_table_existente = create_table_existente



    def set_create_table_novo(self, create_table_novo):
        self._create_table_novo = create_table_novo



    def run_montar_prompt(self):
        self._trocar_create_table_existente()
        self._trocar_create_table_novo()
        return self._txt_prompt



    def _trocar_create_table_existente(self):
        self._txt_prompt = self._txt_prompt.replace('[[DDL_ATUAL]]', self._create_table_existente )



    def _trocar_create_table_novo(self):
        self._txt_prompt = self._txt_prompt.replace('[[DDL_NOVO]]', self._create_table_novo)



