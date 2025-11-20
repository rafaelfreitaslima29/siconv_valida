from utils.time_util import TimeUtil
from services.verificar_adicao_colunas_service import VerificarAdicaoColunasService
from db.models.models import TbVerificarAdicaoColunaModel
from db.repositories.tb_verificar_adicao_colunas_repository import TbVerificarAdicaoColunasRepository



class ExpVerificarAdicaoColunasLLama_3_2_1b_service():
    def __init__(self):
        self._llm_model_name="llama3.2:1b"

        self._create_table_existente = """
CREATE TABLE pcr_siconv.tb_convenios (
	id serial4 NOT NULL,
	nr_convenio varchar NOT NULL,
	id_proposta varchar NOT NULL,
	dia_assin int4 NULL,
	mes_assin int4 NULL,
	ano_assin int4 NULL,
	data_assin_conv date NULL,
	situ_convenio varchar NULL,
	subsitu_convenio varchar NULL,
	situ_publicacao varchar NULL,
	instrumento_ativo varchar NULL,
	ind_opera_obtv varchar NULL,
	nr_processo varchar NULL,
	ug_emitente varchar NULL,
	data_publ_conv date NULL,
	data_inic_vigencia_conv date NULL,
	data_fim_vigencia_conv date NULL,
	dias_presta_contas int4 NULL,
	data_limite_presta_contas date NULL,
	ind_assinado varchar NULL,
	qtde_ta int4 NULL,
	qtde_prorroga int4 NULL,
	vlr_global_conv numeric(13, 2) NULL,
	vlr_repasse_conv numeric(13, 2) NULL,
	vlr_contrapartida_conv numeric(13, 2) NULL,
	vlr_empenhado_conv numeric(13, 2) NULL,
	vlr_desembolsado_conv numeric(13, 2) NULL,
	vlr_saldo_reman_tesouro numeric(13, 2) NULL,
	vlr_saldo_reman_convenente numeric(13, 2) NULL,
	vlr_rendimento_aplicacao numeric(13, 2) NULL,
	vlr_ingresso_contrapartida numeric(13, 2) NULL,
	vlr_saldo_conta numeric(13, 2) NULL,
	dthora_insert timestamp NULL,
	dthora_update timestamp NULL,
	motivo_suspensao varchar NULL,
	ind_foto varchar NULL,
	data_fim_vigencia_conv_orig date NULL,
	vlr_global_conv_orig numeric(13, 2) NULL,
	data_suspensiva date NULL,
	data_retirada_suspensiva date NULL,
	dias_clausula_suspensiva int4 NULL
);
        """

# DIFERENÇAS: Adição de:
# situ_contratacao varchar NULL,
# qtde_convenios int4 NULL,

        self._create_table_novo = """
CREATE TABLE pcr_siconv.tb_convenios (
	id serial4 NOT NULL,
	nr_convenio varchar NOT NULL,
	id_proposta varchar NOT NULL,
	dia_assin int4 NULL,
	mes_assin int4 NULL,
	ano_assin int4 NULL,
	data_assin_conv date NULL,
	situ_convenio varchar NULL,
	subsitu_convenio varchar NULL,
	situ_publicacao varchar NULL,
	instrumento_ativo varchar NULL,
	ind_opera_obtv varchar NULL,
	nr_processo varchar NULL,
	ug_emitente varchar NULL,
	data_publ_conv date NULL,
	data_inic_vigencia_conv date NULL,
	data_fim_vigencia_conv date NULL,
	dias_presta_contas int4 NULL,
	data_limite_presta_contas date NULL,
	situ_contratacao varchar NULL,
	ind_assinado varchar NULL,
	qtde_convenios int4 NULL,
	qtde_ta int4 NULL,
	qtde_prorroga int4 NULL,
	vlr_global_conv numeric(13, 2) NULL,
	vlr_repasse_conv numeric(13, 2) NULL,
	vlr_contrapartida_conv numeric(13, 2) NULL,
	vlr_empenhado_conv numeric(13, 2) NULL,
	vlr_desembolsado_conv numeric(13, 2) NULL,
	vlr_saldo_reman_tesouro numeric(13, 2) NULL,
	vlr_saldo_reman_convenente numeric(13, 2) NULL,
	vlr_rendimento_aplicacao numeric(13, 2) NULL,
	vlr_ingresso_contrapartida numeric(13, 2) NULL,
	vlr_saldo_conta numeric(13, 2) NULL,
	dthora_insert timestamp NULL,
	dthora_update timestamp NULL,
	motivo_suspensao varchar NULL,
	ind_foto varchar NULL,
	data_fim_vigencia_conv_orig date NULL,
	vlr_global_conv_orig numeric(13, 2) NULL,
	data_suspensiva date NULL,
	data_retirada_suspensiva date NULL,
	dias_clausula_suspensiva int4 NULL
);
        """



    def run(self):
        time_util = TimeUtil()
        inicio_execucao = time_util.get_time()

        service = VerificarAdicaoColunasService()
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

        model = TbVerificarAdicaoColunaModel()
        model.llm_model_name = self._llm_model_name
        model.create_table_existente = self._create_table_existente
        model.create_table_novo = self._create_table_novo
        model.inicio_execucao = inicio_execucao
        model.fim_execucao = fim_execucao
        model.resultado = resultado

        repository = TbVerificarAdicaoColunasRepository()
        repository.Insert(model=model)

        print(f"#=> {self.__class__.__name__}.run FIM")
