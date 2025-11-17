from utils.csv_util import CSVUtil



class PromptAjustesTable():
    def __init__(self):
        self._create_table_existente = None
        self._create_table_novo = None
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

