from services.verificar_alteracao_nomes_colunas_service import VerificarAlteracaoNomesColunasService
from utils.time_util import TimeUtil
from db.repositories.tb_verificar_alteracao_nomes_colunas_repository import TbVerificarAlteracaoNomesColunasRepository
from db.models.models import TbVerificarAltaracaoNomeColunaModel


class ExpVerificarAlteracaoNomesColunasLLama_3_2_1b_service():
    def __init__(self):
        # TO-DO - Configurando
        self._create_table_existente = """
        FALTA ADICIONAR O CREATE TABLE EXISTENTE
        """
        self._create_table_novo = """
        FALTA ADICIONAR O CREATE TABLE NOVO
        """
        self._llm_model_name = "llama3.2:1b"


    # TO-DO
    def run(self):
        time_util = TimeUtil()
        inicio_execucao = time_util.get_time()

        service = VerificarAlteracaoNomesColunasService()
        service.set_llm_model_name(self._llm_model_name)
        service.set_create_table_existente(self._create_table_existente)
        service.set_create_table_novo(self._create_table_novo)
        resultado = service.run_llm()
    
        fim_execucao = time_util.get_time()

        # Persistir
        print(f"""
            inicio_execucao: {inicio_execucao}
            fim_execucao: {fim_execucao}
            llm_model_name: {self._llm_model_name} 
            create_table_existente: {self._create_table_existente}
            create_table_novo: {self._create_table_novo}
            resultado: {resultado}
        """)

        model = TbVerificarAltaracaoNomeColunaModel()
        model.llm_model_name = self._llm_model_name
        model.create_table_existente = self._create_table_existente
        model.create_table_novo = self._create_table_novo
        model.inicio_execucao = inicio_execucao
        model.fim_execucao = fim_execucao
        model.resultado = resultado

        repository = TbVerificarAlteracaoNomesColunasRepository()
        repository.Insert(model=model)

        print(f"#=> {self.__class__.__name__}.run FIM")
