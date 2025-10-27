import pandas as pd
import numpy as np
import math


class CSVUtil():
    def __init__(self):
        pd.set_option('display.max_columns' , None)
        pd.set_option('display.max_rows'    , None)
        pd.set_option('display.max_colwidth', None)
        self._caminho_e_nome_csv = None



    def set_caminho_e_nome_csv(self, caminho_e_nome_csv):
        self._caminho_e_nome_csv = caminho_e_nome_csv



    def get_cabecalho(self):
        if self._caminho_e_nome_csv == None:
            return
        
        df = pd.read_csv(filepath_or_buffer=self._caminho_e_nome_csv, delimiter=';')
        cabecalho = df.columns.tolist()
        return cabecalho



    def get_linha(self, row_numero:int=0, delimiter:str=';'):
        df = pd.read_csv(self._caminho_e_nome_csv, delimiter=delimiter)
        linha = df.iloc[[row_numero]].to_dict(orient='records')[0]
       
        # Trata NaN para None e converte NumPy -> Python nativo
        linha_tratadas = []
        for v in linha.values():
            # Se for NumPy tipo
            if isinstance(v, np.generic):
                v = v.item()
            # Se for NaN (float) -> None
            if isinstance(v, float) and math.isnan(v):
                v = None
            linha_tratadas.append(v)

        return linha_tratadas


