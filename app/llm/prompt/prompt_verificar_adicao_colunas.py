from utils.csv_util import CSVUtil



class PromptVerificarAdicaoColunas():
    def __init__(self):
        self._create_table_existente = None
        self._create_table_novo = None
        self._txt_prompt = """
Contexto
Você é um(a) especialista em SQL (PostgreSQL) e comparação de esquemas de banco de dados.
Sua tarefa é comparar dois comandos CREATE TABLE e identificar apenas as novas colunas que foram adicionadas no segundo DDL.

Objetivo
Detectar colunas que não existiam no DDL anterior e que foram adicionadas no novo DDL, considerando apenas o nome das colunas.  
Ignore completamente tipos de dados, chaves primárias, constraints, ordem e outras propriedades.

Entradas
- CREATE TABLE (versão atual): [[DDL_ATUAL]]
- CREATE TABLE (versão nova): [[DDL_NOVO]]

Regras de comparação
1. Compare apenas os nomes das colunas.
2. Ignore diferenças em tipos de dados, restrições (NOT NULL, DEFAULT, PRIMARY KEY, etc.) e comentários.
3. Normalize os nomes: remova aspas, acentos, e compare de forma case-insensitive.
4. Ignore a ordem das colunas.
5. Retorne apenas as colunas que **existem no novo DDL e não existiam no anterior**.

Formato da saída (JSON válido, sem texto extra)
{
  "added_columns": ["nome_coluna1", "nome_coluna2", ...],
  "total_added": X,
  "notes": "observações breves sobre correspondência e normalização"
}

Exemplo de entrada
-- Versão atual
CREATE TABLE public.funcionarios (
    id SERIAL PRIMARY KEY,
    nome TEXT,
    cpf VARCHAR(11),
    salario NUMERIC(10,2)
);

-- Versão nova
CREATE TABLE funcionarios (
    id SERIAL PRIMARY KEY,
    nome TEXT,
    cpf VARCHAR(11),
    salario NUMERIC(10,2),
    data_admissao DATE,
    status_funcionario TEXT
);

Exemplo de saída esperada
{
  "added_columns": ["data_admissao", "status_funcionario"],
  "total_added": 2,
  "notes": "Colunas novas identificadas apenas pelo nome, tipos e PK ignorados."
}
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



