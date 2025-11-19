from services.create_table_by_csv_service import CreateTableByCsvService
from utils.time_util import TimeUtil
from db.repositories.tb_create_table_by_csv_repository import TbCreateTableByCsvRepository
from db.models.models import TbCreateTableByCsvModel


class ExpCreateTableByCsvGpt5_1_Service():
    def __init__(self):
        self._caminho_e_nome_csv="files/descompactados/siconv_convenio.csv"
        self._nome_tabela_banco="tb_convenios"
        self._llm_model_name="gpt-5.1"

    def run(self):
        time_util = TimeUtil()
        inicio_execucao = time_util.get_time()

        service = CreateTableByCsvService()
        service.set_caminho_e_nome_csv(self._caminho_e_nome_csv)
        service.set_llm_model_name(self._llm_model_name)
        service.set_nome_tabela_banco(self._nome_tabela_banco)
        resultado = service.run_llm()

        fim_execucao = time_util.get_time()

        # Persistir
        print(f"""
            inicio_execucao: {inicio_execucao}
            fim_execucao: {fim_execucao}
            llm_model_name: {self._llm_model_name} 
            caminho_e_nome_csv: {self._caminho_e_nome_csv}
            nome_tabela_banco: {self._nome_tabela_banco}
            resultado: {resultado}
        """)

        model = TbCreateTableByCsvModel()
        model.llm_model_name = self._llm_model_name
        model.caminho_e_nome_csv = self._caminho_e_nome_csv
        model.nome_tabela_banco = self._nome_tabela_banco
        model.inicio_execucao = inicio_execucao
        model.fim_execucao = fim_execucao
        model.resultado = resultado

        repository = TbCreateTableByCsvRepository()
        repository.Insert(model=model)

        print(f"#=> {self.__class__.__name__}.run FIM")