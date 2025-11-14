from db.models.models import TbVerificarAltaracaoNomeColunaModel


class TbVerificarAlteracaoNomesColunasRepository():
    def __init__(self):
        pass


    # =================================================================================
    # INSERT
    # =================================================================================
    def Insert(self, model:TbVerificarAltaracaoNomeColunaModel=None):
        """Insere o model"""
        
        # Se o model está vazio 
        if model is None:
            return
        
        return model.Insert(model=model )



