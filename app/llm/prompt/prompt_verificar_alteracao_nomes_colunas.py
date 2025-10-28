from utils.csv_util import CSVUtil



class PromptVerificarAlteracaoNomesColunas():
    def __init__(self):
        self._create_table_existente = None
        self._create_table_novo = None
        self._txt_prompt = """
Contexto
Você é um(a) especialista em SQL (PostgreSQL) e comparação de esquemas. Sua tarefa é comparar dois comandos CREATE TABLE e indicar se houve mudança de nomes de colunas, ignorando completamente tipos de dados, chaves, defaults, comentários, ordem das colunas e quaisquer outras propriedades.

Objetivo
Detectar renomeações, adições e remoções de colunas considerando apenas os nomes (case-insensitive). Se houver ambiguidade, seja conservador(a) e explique.

Entradas
- CREATE TABLE (atual): [[DDL_ATUAL]]

- CREATE TABLE (novo): [[DDL_NOVO]]

Regras de normalização (obrigatórias)
1) Compare nomes de colunas sem aspas, sem acentos e case-insensitive (ex.: "CPF", cpf, Cpf → cpf).
2) Ignore tudo além do identificador da coluna (tipos, NOT NULL, DEFAULT, CONSTRAINT, COMMENT, etc.).
3) Ignore a ordem das colunas.
4) Se um nome existir em ambos, considere-o “inalterado”.
5) Para suspeita de renomeação, use similaridade de string/semântica (ex.: "nome" ↔ "nome_completo" pode ser renomeação; "uf" ↔ "estado" possivelmente também). Seja cauteloso(a) ao inferir renomeações quando existirem múltiplas correspondências plausíveis.


Procedimento
1) Extrair apenas a lista de nomes de colunas de cada DDL (após normalização).
2) Identificar interseção (unchanged).
3) Para os nomes presentes apenas no DDL atual, tentar pareá-los com nomes presentes apenas no DDL novo:
   3.1) Propor renomeações quando houver forte evidência lexical/semântica (ex.: distância pequena, sinônimos/siglas usuais).
   3.2) Quando não houver evidência suficiente, classificar como removed (no atual) e added (no novo).
4) Preencher o JSON exatamente no formato solicitado. Não inclua comentários fora do JSON.

Exemplo mínimo
-- Atual
CREATE TABLE public.pessoas (
  id INTEGER PRIMARY KEY,
  Nome TEXT NOT NULL,
  cpf TEXT,
  dt_nascimento DATE
);

-- Novo
CREATE TABLE pessoas (
  id BIGINT PRIMARY KEY,
  nome_completo TEXT NOT NULL,
  cpf TEXT,
  data_nascimento DATE
);

Saída esperada (exemplo):
  colunas não alteradas: ["id", "cpf"],
  
  colunas renomeadas:  
    de: "nome", para: "nome_completo"
    
  
  
  
  notes": "Tipos e PK ignorados conforme instruções.

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



