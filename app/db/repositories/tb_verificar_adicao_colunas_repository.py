from db.models.models import TbVerificarAdicaoColunaModel


class TbVerificarAdicaoColunasRepository():
    def __init__(self):
        pass


    # =================================================================================
    # INSERT
    # =================================================================================
    def Insert(self, model:TbVerificarAdicaoColunaModel=None):
        """Insere o model"""
        
        # Se o model está vazio 
        if model is None:
            return
        
        return model.Insert(model=model )



