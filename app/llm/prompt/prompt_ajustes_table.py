from utils.csv_util import CSVUtil



class PromptAjustesTable():
    def __init__(self):
        self._create_table_existente = None
        self._create_table_novo = None
        self._txt_prompt         = """
Tarefa
Comparar o DDL atual com o DDL novo e gerar somente o SQL necessário para adaptar a estrutura atual à nova.

Entradas:

Create Table Atual =
[[DDL_ATUAL]]

Create Table Novo =
[[DDL_NOVO]]


Regras (todas obrigatórias):

Faça uma lista com só com os nomes do CREATE TABLE ATUAL e outra lista CREATE TABLE NOVO e compare diferenças entre as listas.

Caso os nomes existam nas duas listas retire eles da lista.

Comparar apenas nomes de colunas (ignorar ordem, tipos, defaults, constraints).

Coluna presente no novo e ausente no atual → gerar ADD COLUMN com o tipo do novo.

Colunas com nomes diferentes, que não existem no create table, mas claramente correspondentes → gerar RENAME COLUMN. Se houver dúvida, não renomear.

Não altere o tipo das colunas.

Nunca remover colunas, nem gerar alterações que possam causar perda de dados.

Ignorar todas as constraints.

Saída deve conter apenas SQL PostgreSQL válido.

Proibido qualquer explicação, comentário, JSON, pseudocódigo ou texto fora do SQL de saída.

Proibido retornar a lista de nomes das colunas.

Comportamento determinístico: mesma entrada → mesma saída, sem variação.

Se não houver ajustes, retornar exatamente:
Ajustes:
(nenhuma)


Formato de saída obrigatório:

Quando houver ajustes, seguir estritamente este padrão:

ALTER TABLE public.tabela
    AJUSTES_NECESSARIOS -- COMENTÁRIO O PORQUÊ DO AJUSTE
;

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

