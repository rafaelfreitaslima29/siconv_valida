from utils.csv_util import CSVUtil



class PromptCreateTableCsv():
    def __init__(self):
        self._caminho_e_nome_csv  = None
        self._nome_tabela_banco   = None
        self._txt_prompt         = """
Contexto:
Você é um especialista em bancos de dados relacionais e SQL.
Sua tarefa é analisar a estrutura de um arquivo CSV e gerar o script SQL para criar a tabela correspondente.

Instruções:
1. Use nomes de coluna iguais aos cabeçalhos do CSV.
2. Escolha o tipo de dado apropriado com base nos exemplos fornecidos.
3. Crie restrições de NOT NULL se fizer sentido.
4. Defina uma chave primária, se houver coluna apropriada.

Formato da resposta:
Retorne apenas o script `CREATE TABLE`, formatado em SQL padrão PostgreSQL, sem explicações extras.

Exemplo de entrada:
Nome da Tabela: [[NOME_TABELA]]
Cabeçalhos: [[CABECALHOS]]
Amostras: 
- [[ROW1]]
- [[ROW2]]
- [[ROW3]]
- [[ROW4]]
"""



    def set_caminho_e_nome_csv(self, caminho_e_nome_csv):
        self._caminho_e_nome_csv = caminho_e_nome_csv



    def set_nome_tabela_banco(self, nome_tabela_banco):
        self._nome_tabela_banco = nome_tabela_banco



    def run_montar_prompt(self):
        self._trocar_cabecalho()
        self._trocar_linhas()
        self._trocar_nome_tabela()

        return self._txt_prompt



    def _trocar_nome_tabela(self):
        self._txt_prompt = self._txt_prompt.replace('[[NOME_TABELA]]', self._nome_tabela_banco )



    def _trocar_cabecalho(self):
        csv_util = CSVUtil()
        csv_util.set_caminho_e_nome_csv(caminho_e_nome_csv = self._caminho_e_nome_csv)

        list_cabecalho_csv = csv_util.get_cabecalho()
        self._txt_prompt = self._txt_prompt.replace('[[CABECALHOS]]', str( list_cabecalho_csv ))



    def _trocar_linhas(self):
        csv_util = CSVUtil()
        csv_util.set_caminho_e_nome_csv(self._caminho_e_nome_csv)

        row1 = csv_util.get_linha(row_numero=0 )
        self._txt_prompt = self._txt_prompt.replace('[[ROW1]]', str(row1) )

        row2 = csv_util.get_linha(row_numero=1)
        self._txt_prompt = self._txt_prompt.replace('[[ROW2]]', str(row2) )

        row3 = csv_util.get_linha(row_numero=2)
        self._txt_prompt = self._txt_prompt.replace('[[ROW3]]', str(row3) )

        row4 = csv_util.get_linha(row_numero=3)
        self._txt_prompt = self._txt_prompt.replace('[[ROW4]]', str(row4) )


