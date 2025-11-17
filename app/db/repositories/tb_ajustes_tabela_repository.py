from db.models.models import TbAjustestabelaModel



class TbAjustesTabelaRepository():
    def __init__(self):
        pass


    # =================================================================================
    # INSERT
    # =================================================================================
    def Insert(self, model:TbAjustestabelaModel=None):
        """Insere o model"""
        
        # Se o model está vazio 
        if model is None:
            return
        
        return model.Insert(model=model )



