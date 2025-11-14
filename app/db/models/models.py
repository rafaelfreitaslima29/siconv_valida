from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from db.databases import SessionLocal

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
            session.add(model)
            session.commit()
            return model


# ================================================================================================
# Tabela de Verificar Alteração de Nome da Coluna
# ================================================================================================
class TbVerificarAltaracaoNomeColunaModel(Base):
    '''Model para persistir a Verificação de alteração do nome de coluna da tabela.'''
    __tablename__ = "tb_verificar_alteracao_nome_coluna"
    __table_args__ = {'schema': 'siconv_valida'}

    id                      : Mapped[int] = mapped_column(primary_key=True)
    llm_model_name          : Mapped[str] = mapped_column(nullable=True)
    create_table_existente  : Mapped[str] = mapped_column(nullable=True)
    create_table_novo       : Mapped[str] = mapped_column(nullable=True)
    inicio_execucao         : Mapped[str] = mapped_column(nullable=True)
    fim_execucao            : Mapped[str] = mapped_column(nullable=True)
    resultado               : Mapped[str] = mapped_column(nullable=True)


    def __repr__(self):
        return f"""
        <TbCreateTableByCsvModel(id={self.id}, 
        llm_model_name={self.llm_model_name}, 
        create_table_existente={self.create_table_existente}, 
        create_table_novo={self.create_table_novo}
        inicio_execucao={self.inicio_execucao}
        fim_execucao={self.fim_execucao}
        resultado={self.resultado}
        )>"""



    @classmethod
    def Insert(self, model):
        """Método de classe para criar um novo registro"""
        with SessionLocal() as session:
            session.add(model)
            session.commit()
            return model




# ================================================================================================
# Tabela de Verificar Adição de Coluna
# ================================================================================================



# ================================================================================================
# Tabela de comparação do create table
# ================================================================================================






# # ================================================================================================
# # RESULTADOS DA EXECUÇÃO
# # ================================================================================================




