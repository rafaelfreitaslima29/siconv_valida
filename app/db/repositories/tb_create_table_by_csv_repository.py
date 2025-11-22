# from db.databases import get_db
from db.models.models import TbCreateTableByCsvModel


class TbCreateTableByCsvRepository():
    def __init__(self):
        pass


    # =================================================================================
    # INSERT
    # =================================================================================
    def Insert(self, model:TbCreateTableByCsvModel=None):
        """Insere o model"""
        
        # Se o model está vazio 
        if model is None:
            return
        
        return model.Insert(model=model )



    def SelectAll(self):
        model = TbCreateTableByCsvModel()
        return model.SelectAll()
    

    
    def SelectById(self, id:int):
        model = TbCreateTableByCsvModel()
        return model.SelectById(id=id)