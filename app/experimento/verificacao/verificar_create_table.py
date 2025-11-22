import re
from db.repositories.tb_create_table_by_csv_repository import TbCreateTableByCsvRepository
from db.models.models import TbCreateTableByCsvVerificarModel
from db.models.models import TbCreateTableByCsvModel


class VerificarCreateTable():
    def __init__(self):
        pass



    def verificar_create_table_by_csv(self, model:TbCreateTableByCsvModel ):
        input_model = model
        
        # lista de colunas esperadas no DDL de cração de uma tabela a partir do CSV.
        lista_colunas = [
            'NR_CONVENIO',
            'ID_PROPOSTA',
            'DIA',
            'MES',
            'ANO',
            'DIA_ASSIN_CONV',
            'SIT_CONVENIO',
            'SUBSITUACAO_CONV',
            'SITUACAO_PUBLICACAO',
            'INSTRUMENTO_ATIVO',
            'IND_OPERA_OBTV',
            'NR_PROCESSO',
            'UG_EMITENTE',
            'DIA_PUBL_CONV',
            'DIA_INIC_VIGENC_CONV',
            'DIA_FIM_VIGENC_CONV',
            'DIA_FIM_VIGENC_ORIGINAL_CONV',
            'DIAS_PREST_CONTAS',
            'DIA_LIMITE_PREST_CONTAS',
            'DATA_SUSPENSIVA',
            'DATA_RETIRADA_SUSPENSIVA',
            'DIAS_CLAUSULA_SUSPENSIVA',
            'SITUACAO_CONTRATACAO',
            'IND_ASSINADO',
            'MOTIVO_SUSPENSAO',
            'IND_FOTO',
            'QTDE_CONVENIOS',
            'QTD_TA',
            'QTD_PRORROGA',
            'VL_GLOBAL_CONV',
            'VL_REPASSE_CONV',
            'VL_CONTRAPARTIDA_CONV',
            'VL_EMPENHADO_CONV',
            'VL_DESEMBOLSADO_CONV',
            'VL_SALDO_REMAN_TESOURO',
            'VL_SALDO_REMAN_CONVENENTE',
            'VL_RENDIMENTO_APLICACAO',
            'VL_INGRESSO_CONTRAPARTIDA',
            'VL_SALDO_CONTA',
            'VALOR_GLOBAL_ORIGINAL_CONV'
        ]



        # Retorna o nome das colunas
        input_create_table = input_model.resultado
        colunas_create_table = re.findall(r'^\s*([A-Z0-9_]+)\s+(?:BOOLEAN|INT|INTEGER|BIGINT|SMALLINT|DATE|CHAR|VARCHAR|CHARACTER|TEXT|NUMERIC|DOUBLE|FLOAT|REAL|DECIMAL)', input_create_table, re.MULTILINE)
        print(colunas_create_table)

        # Verificar faltantes e extras
        colunas_menos = set(lista_colunas) - set(colunas_create_table)
        colunas_mais = set(colunas_create_table) - set(lista_colunas)
        
        saida = f'''
        ##### VERIFICAÇÂO DE COLUNAS #####

        COLUNAS FALTENTES:
        {colunas_menos}

        COLUNAS EXTRAS:
        {colunas_mais}
'''
        print(saida)

        # Saída esperada
        save_model = TbCreateTableByCsvVerificarModel()
        save_model.tb_create_table_by_csv_id = input_model.id
        save_model.llm_model_name            = input_model.llm_model_name
        save_model.nome_tabela_banco         = input_model.nome_tabela_banco
        save_model.create_table              = input_model.resultado
        save_model.colunas_mais              = str(colunas_mais)  # Convertido para String, set() não é aceito. 
        save_model.colunas_menos             = str(colunas_menos) # Convertido para String, set() não é aceito.

        save_model.Insert(model=save_model)


        # Execução da verificação da criação dos DDLs a partir do CSV 
        # for obj in rep.GetAll():
            

    #         ddl_create_tb_csv = obj.create_table_from_csv
    #         ddl_create_tb_csv = ddl_create_tb_csv.upper()
          
    #         # self._log.info(f'ddl_create_tb_csv {ddl_create_tb_csv}')

    #         # Retorna o nome das colunas
    #         colunas_sql = re.findall(r'^\s*([A-Z0-9_]+)\s+(?:BOOLEAN|INT|INTEGER|BIGINT|SMALLINT|DATE|CHAR|VARCHAR|CHARACTER|TEXT|NUMERIC|DOUBLE|FLOAT|REAL|DECIMAL)', ddl_create_tb_csv, re.MULTILINE)
           
    #         # Verificar faltantes e extras
    #         faltando = set(lista_colunas) - set(colunas_sql)
    #         extras = set(colunas_sql) - set(lista_colunas)
            
    #         # Para se considerado criado com sucesso e necessário ter todas as colunas do CSV e não ter colunas extras
    #         criou_ddl_csv = None
    #         if len(faltando) == 0 and len(extras) == 0:
    #             criou_ddl_csv = True
    #         else:
    #             criou_ddl_csv = False

    #         # Salvar os dados no banco de dados
    #         rep_m = TbMetricasRepository()
    #         model_m = TbMetricasModel()

    #         model_m.id_tb_avaliacao = obj.id

    #         model_m.bo_metr1_criou_ddl_csv_todas_col = criou_ddl_csv
    #         model_m.tx_metr2_criou_ddl_csv_col_faltantes = str(faltando)
    #         model_m.tx_metr3_criou_ddl_csv_col_extras = str(extras)
    #         rep_m.Insert(model=model_m)



    # def _VerificarMetricas_4_AlteracaoNomeColuna(self):
    #     '''Verifica se a LLM verificou a alteração do nome da coluna "SIT_CONTRATACAO" para "SITUACAO_CONTRATACAO".'''
    #     # repositorio das execuções das LLMs.
    #     rep_avaliacao = TbAvaliacaoRepository()

    #     # Coluna que dever ser procurada no resultado.
    #     lista_colunas = [
    #         'SITUACAO_CONTRATACAO'
    #     ]

    #     # Execução da verificação da criação dos DDLs a partir do CSV 
    #     for obj in rep_avaliacao.GetAll():
    #         # Retorna o nome das colunas
    #         colunas_sql = re.findall(r'^\s*([A-Z0-9_]+)\s+(?:BOOLEAN|INT|INTEGER|BIGINT|SMALLINT|DATE|CHAR|VARCHAR|CHARACTER|TEXT|NUMERIC|DOUBLE|FLOAT|REAL|DECIMAL)', obj.resultado.upper(), re.MULTILINE)
           
    #         # Verificar faltantes e extras
    #         col_verificada_menos_col_sql = set(lista_colunas) - set(colunas_sql)
    #         # faltando = set(lista_colunas) - set(colunas_sql)

    #         print(f" ###################### faltando:{col_verificada_menos_col_sql} |  set(lista_colunas): {set(lista_colunas)} | set(colunas_sql): {set(colunas_sql)}  ")
            
    #         nome_alterado = None
    #         if len(col_verificada_menos_col_sql) == 0:
    #             nome_alterado = True
    #         else:
    #             nome_alterado = False

    #         # Salvar os dados no banco de dados
    #         rep_m = TbMetricasRepository()
    #         model_metricas = rep_m.FindByIdAvaliacao(obj.id)

    #         model_metricas.bo_metr4_nome_col_alterado          = nome_alterado
    #         model_metricas.tx_metr4_saida_col_verif_ms_col_sql = str( col_verificada_menos_col_sql ) 
    #         # self._log.info(msg=f'faltando: {faltando} | model_metricas:{model_metricas} ')

    #         rep_m.Update(model=model_metricas)



    # def _VerificarMetricas_5_Adicao_coluna(self):
    #     '''Verifica se a LLM verificou a adição de uma nova coluna "NR_PROCESSO".'''
    #     # repositorio das execuções das LLMs.
    #     rep_avaliacao = TbAvaliacaoRepository()

    #     # Coluna que dever ser procurada no resultado.
    #     lista_colunas = [
    #         'NR_PROCESSO'
    #     ]

    #     # Execução da verificação da criação dos DDLs a partir do CSV 
    #     for obj in rep_avaliacao.GetAll():
    #         # Retorna o nome das colunas
    #         colunas_sql = re.findall(r'^\s*([A-Z0-9_]+)\s+(?:BOOLEAN|INT|INTEGER|BIGINT|SMALLINT|DATE|CHAR|VARCHAR|CHARACTER|TEXT|NUMERIC|DOUBLE|FLOAT|REAL|DECIMAL)', obj.resultado.upper(), re.MULTILINE)
           
    #         # Verificar faltantes e extras
    #         coluna_adicionada = set(lista_colunas) - set(colunas_sql)
            
    #         verificacao_resultado = None
    #         if len(coluna_adicionada) == 0:
    #             verificacao_resultado = True
    #         else:
    #             verificacao_resultado = False

    #         # Salvar os dados no banco de dados
    #         rep_m = TbMetricasRepository()
    #         model_metricas = rep_m.FindByIdAvaliacao(obj.id)

    #         model_metricas.bo_metr5_add_coluna = verificacao_resultado
    #         model_metricas.tx_metr5_saida = str(coluna_adicionada)
    #         # self._log.info(msg=f'faltando: {coluna_adicionada} | model_metricas:{model_metricas} ')

    #         rep_m.Update(model=model_metricas)



    # def _VerificarMetricas_6_CreateFuncioana(self):
    #     pass
