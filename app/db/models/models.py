from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
# from sqlalchemy.sql.expression import select
# from sqlalchemy import update
# from sqlalchemy import delete
from db.databases import SessionLocal

# from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey, Boolean
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
# from sqlalchemy.sql import func


# Base do ORM do SqlAlchemy
class Base(DeclarativeBase):
    pass


# ================================================================================================
# Tabela de Create Table do CSV
# ================================================================================================
class TbCreateTableByCsvModel(Base):
    '''Model para persistir o Create Table criado a partir do CSV.'''
    __tablename__ = "tb_create_table_by_csv"
    __table_args__ = {'schema': 'siconv_valida'}

    id                      : Mapped[int] = mapped_column(primary_key=True)
    llm_model_name          : Mapped[str] = mapped_column(nullable=True)
    caminho_e_nome_csv      : Mapped[str] = mapped_column(nullable=True)
    nome_tabela_banco       : Mapped[str] = mapped_column(nullable=True)
    inicio_execucao         : Mapped[str] = mapped_column(nullable=True)
    fim_execucao            : Mapped[str] = mapped_column(nullable=True)
    resultado               : Mapped[str] = mapped_column(nullable=True)

    def __repr__(self):
        return f"""
        <TbCreateTableByCsvModel(id={self.id}, 
        llm_model_name={self.llm_model_name}, 
        caminho_e_nome_csv={self.caminho_e_nome_csv}, 
        nome_tabela_banco={self.nome_tabela_banco}
        inicio_execucao={self.inicio_execucao}
        fim_execucao={self.fim_execucao}
        resultado={self.resultado}
        )>"""




    @classmethod
    def Insert(self, model):
        """Método de classe para criar um novo registro"""
        with SessionLocal() as session:
            # _model = TbCreateTableByCsvModel()
            # model = cls(
            #     llm_model_name = model.llm_model_name,
            #     caminho_e_nome_csv = model.caminho_e_nome_csv,
            #     nome_tabela_banco = model.nome_tabela_banco,
            #     inicio_execucao = model.inicio_execucao,
            #     fim_execucao = model.fim_execucao,
            #     resultado = model.resultado
            # )
            session.add(model)
            session.commit()
            return model






    # @classmethod
    # def Insert(cls, db, model
    #     # llm_model_name:str,
    #     # caminho_e_nome_csv:str,
    #     # nome_tabela_banco:str,
    #     # inicio_execucao:str,
    #     # fim_execucao:str,
    #     # resultado:str
    # ):
    #     """Método de classe para criar um novo registro"""
    #     model = cls(
    #         llm_model_name = model.llm_model_name,
    #         caminho_e_nome_csv = model.caminho_e_nome_csv,
    #         nome_tabela_banco = model.nome_tabela_banco,
    #         inicio_execucao = model.inicio_execucao,
    #         fim_execucao = model.fim_execucao,
    #         resultado = model.resultado
    #     )
    #     db.add(model)
    #     db.commit()
    #     db.refresh(model)
    #     return model



    # @classmethod
    # def get_by_id(cls, db, id: int):
    #     """Método de classe para consultar por id"""
    #     return db.query(cls).filter(cls.id == id).first()



    # @classmethod
    # def get_all(cls, db):
    #     """Método de classe para obter todos os registros"""
    #     return db.query(cls).all()



    # @classmethod
    # def update(cls, db, id: int, 
    #     llm_model_name:str,
    #     caminho_e_nome_csv:str,
    #     nome_tabela_banco:str,
    #     inicio_execucao:str,
    #     fim_execucao:str,
    #     resultado:str
    #     ):
    #     """Método de classe para atualizar um registro"""
    #     model = db.query(cls).filter(cls.id == id).first()
    #     if model:
    #         model.llm_model_name = llm_model_name
    #         model.caminho_e_nome_csv = caminho_e_nome_csv
    #         model.nome_tabela_banco = nome_tabela_banco
    #         model.inicio_execucao = inicio_execucao
    #         model.fim_execucao = fim_execucao
    #         model.resultado = resultado
    #         db.commit()  # Commit para salvar as mudanças
    #         db.refresh(model)
    #         return model
    #     return None



# ================================================================================================
# Tabela de Verificar Alteração de Nome da Coluna
# ================================================================================================
# class TbVerificarAltaracaoNomeColuna(Base):
#     '''Model para persistir a Verificação de alteração do nome de coluna da tabela.'''
#     __tablename__ = "tb_verificar_alteracao_nome_coluna"
#     __table_args__ = {'schema': 'siconv_valida'}

#     id                      = Column(Integer,   primary_key=True, index=True)
#     llm_model_name          = Column(Text,      nullable=False)
#     create_table_existente  = Column(Text,      nullable=False)
#     create_table_novo       = Column(Text,      nullable=False)
#     inicio_execucao         = Column(Text,      nullable=False)
#     fim_execucao            = Column(Text,      nullable=False)
#     resultado               = Column(Text,      nullable=False)


#     def __repr__(self):
#         return f"""
#         <TbCreateTableByCsvModel(id={self.id}, 
#         llm_model_name={self.llm_model_name}, 
#         create_table_existente={self.create_table_existente}, 
#         create_table_novo={self.create_table_novo}
#         inicio_execucao={self.inicio_execucao}
#         fim_execucao={self.fim_execucao}
#         resultado={self.resultado}
#         )>"""



#     @classmethod
#     def Insert(cls, db,
#         llm_model_name:str,
#         create_table_existente:str,
#         create_table_novo:str,
#         inicio_execucao:str,
#         fim_execucao:str,
#         resultado:str
#     ):
#         """Método de classe para criar um novo registro"""
#         model = cls(
#             llm_model_name = llm_model_name,
#             create_table_existente = create_table_existente,
#             create_table_novo = create_table_novo,
#             inicio_execucao = inicio_execucao,
#             fim_execucao = fim_execucao,
#             resultado = resultado
#         )
#         db.add(model)
#         db.commit()
#         db.refresh(model)
#         return model



#     @classmethod
#     def get_by_id(cls, db, id: int):
#         """Método de classe para consultar por id"""
#         return db.query(cls).filter(cls.id == id).first()



#     @classmethod
#     def get_all(cls, db):
#         """Método de classe para obter todos os registros"""
#         return db.query(cls).all()



#     @classmethod
#     def update(cls, db, id: int, 
#         llm_model_name:str,
#         create_table_existente:str,
#         create_table_novo:str,
#         inicio_execucao:str,
#         fim_execucao:str,
#         resultado:str
#         ):
#         """Método de classe para atualizar um registro"""
#         model = db.query(cls).filter(cls.id == id).first()
#         if model:
#             model.llm_model_name = llm_model_name
#             model.create_table_existente = create_table_existente
#             model.create_table_novo = create_table_novo
#             model.inicio_execucao = inicio_execucao
#             model.fim_execucao = fim_execucao
#             model.resultado = resultado
#             db.commit()  # Commit para salvar as mudanças
#             db.refresh(model)
#             return model
#         return None




# ================================================================================================
# Tabela de Verificar Adição de Coluna
# ================================================================================================



# ================================================================================================
# Tabela de comparação do create table
# ================================================================================================






# # ================================================================================================
# # RESULTADOS DA EXECUÇÃO
# # ================================================================================================






# class TbComparacaoModel(Base):
#     '''Comparação de tabelas'''
#     __tablename__ = "tb_comparison"
#     __table_args__ = {'schema': 'dm'}

#     id                      = Column(Integer,   primary_key=True, index=True)
#     llm_model               = Column(Text,      nullable=False)
#     file_csv_name           = Column(Text,      nullable=False)
#     tb_name                 = Column(Text,      nullable=False)
#     create_table_from_csv   = Column(Text,      nullable=False)
#     create_table_from_table = Column(Text,      nullable=False)
#     result                  = Column(Text,      nullable=False)
#     exec_start              = Column(Text,      nullable=True)
#     exec_end                = Column(Text,      nullable=True)
#     vlr_avaliacao           = Column(Boolean,   nullable=False, default=False) 


#     def __repr__(self):
#         return f"<TbComparacaoModel(id={self.id}, llm_model={self.llm_model}, file_csv_name={self.file_csv_name}, tb_name={self.tb_name})>"



#     @classmethod
#     def Insert(cls, db,
#                llm_model:str,
#                file_csv_name: str,
#                tb_name: str, 
#                create_table_from_csv: str,
#                create_table_from_table: str, 
#                result: str, 
#                exec_start: str, 
#                exec_end: str, 
#                vlr_avaliacao:bool
#     ):
#         """Método de classe para criar um novo registro"""
#         model = cls(
#             llm_model               = llm_model,
#             file_csv_name           = file_csv_name,
#             tb_name                 = tb_name,
#             create_table_from_csv   = create_table_from_csv,
#             create_table_from_table = create_table_from_table,
#             result                  = result,
#             exec_start              = exec_start, 
#             exec_end                = exec_end,
#             vlr_avaliacao           = vlr_avaliacao 
#         )
#         db.add(model)
#         db.commit()
#         db.refresh(model)
#         return model



#     @classmethod
#     def get_by_id(cls, db, id: int):
#         """Método de classe para consultar por id"""
#         return db.query(cls).filter(cls.id == id).first()



#     @classmethod
#     def get_all(cls, db):
#         """Método de classe para obter todos os registros"""
#         return db.query(cls).all()



#     @classmethod
#     def update(cls, db, id: int, llm_model:str, file_csv_name: str, tb_name: str, create_table_from_csv: str,
#                create_table_from_table: str, result: str):
#         """Método de classe para atualizar um registro"""
#         model = db.query(cls).filter(cls.id == id).first()
#         if model:
#             model.llm_model = llm_model
#             model.file_csv_name = file_csv_name
#             model.tb_name = tb_name
#             model.create_table_from_csv = create_table_from_csv
#             model.create_table_from_table = create_table_from_table
#             model.result = result
#             db.commit()  # Commit para salvar as mudanças
#             db.refresh(model)
#             return model
#         return None



#     @classmethod
#     def delete(cls, db, id: int):
#         """Método de classe para deletar um registro"""
#         model = db.query(cls).filter(cls.id == id).first()
#         if model:
#             db.delete(model)
#             db.commit()
#             return True
#         return False




# # ================================================================================================
# # MODELO PARA ANÁLISE
# # ================================================================================================
# class TbAnaliseComparacaoModel(Base):
#     '''Análise da Comparação tabelas'''
#     __tablename__ = "tb_analise_comparacao"
#     __table_args__ = {'schema': 'analise'}

#     id                          = Column(Integer,   primary_key=True, index=True)
#     llm_model                   = Column(Text,      nullable=False)
#     file_csv_name               = Column(Text,      nullable=False)
#     tb_name                     = Column(Text,      nullable=False)
#     create_table_from_csv       = Column(Text,      nullable=False)
#     create_table_from_table     = Column(Text,      nullable=False)
#     result                      = Column(Text,      nullable=False)
#     exec_start                  = Column(Text,      nullable=True)
#     exec_end                    = Column(Text,      nullable=True)
#     bool_criou_ddl_csv          = Column(Text,      nullable=True)
#     bool_achou                  = Column(Boolean,   nullable=True)
#     bool_explicou               = Column(Boolean,   nullable=True)
#     bool_sql_retornado_resolve  = Column(Boolean,   nullable=True)


#     def __repr__(self):
#         return (
#             f"<TbAnaliseComparacaoModel("
#             f"id={self.id}, "
#             f"llm_model={self.llm_model}, "
#             f"file_csv_name={self.file_csv_name}, "
#             f"tb_name={self.tb_name}, "
#             f"create_table_from_csv={self.create_table_from_csv}, "
#             f"create_table_from_table={self.create_table_from_table}, "
#             f"result={self.result}, "
#             f"exec_start={self.exec_start}, "
#             f"exec_end={self.exec_end}, "
#             f"bool_criou_ddl_csv={self.bool_criou_ddl_csv}, "            
#             f"bool_achou={self.bool_achou}, "
#             f"bool_explicou={self.bool_explicou}, "
#             f"bool_sql_retornado_resolve={self.bool_sql_retornado_resolve}"
#             f")>"
#         )



#     @classmethod
#     def Insert(cls, db,
#         llm_model:str,
#         file_csv_name: str,
#         tb_name: str, 
#         create_table_from_csv: str,
#         create_table_from_table: str, 
#         result: str, 
#         exec_start: str, 
#         exec_end: str,
#         bool_criou_ddl_csv:bool,
#         bool_achou:bool,
#         bool_explicou:bool,
#         bool_sql_retornado_resolve:bool
#     ):
#         """Método de classe para criar um novo registro"""
#         model = cls(
#             llm_model                  = llm_model,
#             file_csv_name              = file_csv_name,
#             tb_name                    = tb_name,
#             create_table_from_csv      = create_table_from_csv,
#             create_table_from_table    = create_table_from_table,
#             result                     = result,
#             exec_start                 = exec_start, 
#             exec_end                   = exec_end,
#             bool_criou_ddl_csv         = bool_criou_ddl_csv,
#             bool_achou                 = bool_achou,
#             bool_explicou              = bool_explicou,
#             bool_sql_retornado_resolve = bool_sql_retornado_resolve
#         )
#         db.add(model)
#         db.commit()
#         db.refresh(model)
#         return model



#     @classmethod
#     def get_by_id(cls, db, id: int):
#         """Método de classe para consultar por id"""
#         return db.query(cls).filter(cls.id == id).first()



#     @classmethod
#     def get_all(cls, db):
#         """Método de classe para obter todos os registros"""
#         return db.query(cls).all()



#     @classmethod
#     def update(cls, db, 
#         id: int, 
#         llm_model:str, 
#         file_csv_name: str, 
#         tb_name: str, 
#         create_table_from_csv: str,
#         create_table_from_table: str, 
#         result: str,
#         bool_criou_ddl_csv:bool,
#         bool_achou:bool, 
#         bool_explicou:bool, 
#         bool_sql_retornado_resolve:bool
#     ):
#         """Método de classe para atualizar um registro"""
#         model = db.query(cls).filter(cls.id == id).first()
#         if model:
#             model.llm_model                  = llm_model
#             model.file_csv_name              = file_csv_name
#             model.tb_name                    = tb_name
#             model.create_table_from_csv      = create_table_from_csv
#             model.create_table_from_table    = create_table_from_table
#             model.result                     = result
#             model.bool_criou_ddl_csv         = bool_criou_ddl_csv
#             model.bool_achou                 = bool_achou
#             model.bool_explicou              = bool_explicou
#             model.bool_sql_retornado_resolve = bool_sql_retornado_resolve
#             db.commit() 
#             db.refresh(model)
#             return model
#         return None



#     @classmethod
#     def delete(cls, db, id: int):
#         """Método de classe para deletar um registro"""
#         model = db.query(cls).filter(cls.id == id).first()
#         if model:
#             db.delete(model)
#             db.commit()
#             return True
#         return False



