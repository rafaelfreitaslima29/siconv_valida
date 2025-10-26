CREATE SCHEMA experimento;

-- ================================================================================================
-- EXPERIMENTO
-- ================================================================================================
-- create para o experimento
CREATE TABLE experimento.convenios (
	nr_convenio varchar not null,
	id_proposta varchar not null,
	dia int4 null,
	mes int4 null,
	ano int4 null,
	DIA_ASSIN_CONV date null, 	
	SIT_CONVENIO varchar null,
	SUBSITUACAO_CONV varchar null,
	SITUACAO_PUBLICACAO varchar null,
	instrumento_ativo varchar null,
	ind_opera_obtv varchar null,
	--nr_processo varchar null, -- retirada dessa coluna
	ug_emitente varchar null,
	DIA_PUBL_CONV date null,
	DIA_INIC_VIGENC_CONV date null,
	DIA_FIM_VIGENC_CONV date null,  
	DIA_FIM_VIGENC_ORIGINAL_CONV date null,
	DIAS_PREST_CONTAS int4 null,
	DIA_LIMITE_PREST_CONTAS date null, 
	data_suspensiva date null,
	data_retirada_suspensiva date null,
	dias_clausula_suspensiva int4 null,
	SIT_CONTRATACAO varchar null, -- diferença no nome "SITUACAO_CONTRATACAO"
	ind_assinado varchar null,
	motivo_suspensao varchar null,
	ind_foto varchar null,
	qtde_convenios int4 null,
	QTD_TA int4 null,
	QTD_PRORROGA int4 null,
	VL_GLOBAL_CONV numeric(13, 2) null,
	VL_REPASSE_CONV numeric(13, 2) null,
	VL_CONTRAPARTIDA_CONV numeric(13, 2) null,
	VL_EMPENHADO_CONV numeric(13, 2) null,
	VL_DESEMBOLSADO_CONV numeric(13, 2) null,
	VL_SALDO_REMAN_TESOURO numeric(13, 2) null,
	VL_SALDO_REMAN_CONVENENTE numeric(13, 2) null,
	VL_RENDIMENTO_APLICACAO numeric(13, 2) null,
	VL_INGRESSO_CONTRAPARTIDA numeric(13, 2) null,
	VL_SALDO_CONTA numeric(13, 2) null,
	VALOR_GLOBAL_ORIGINAL_CONV numeric(13, 2) null
);




-- create completo
-- CREATE TABLE experimento.convenios (
-- 	nr_convenio varchar not null,
-- 	id_proposta varchar not null,
-- 	dia int4 null,
-- 	mes int4 null,
-- 	ano int4 null,
-- 	DIA_ASSIN_CONV date null, 	
-- 	SIT_CONVENIO varchar null,
-- 	SUBSITUACAO_CONV varchar null,
-- 	SITUACAO_PUBLICACAO varchar null,
-- 	instrumento_ativo varchar null,
-- 	ind_opera_obtv varchar null,
-- 	nr_processo varchar null,
-- 	ug_emitente varchar null,
-- 	DIA_PUBL_CONV date null,
-- 	DIA_INIC_VIGENC_CONV date null,
-- 	DIA_FIM_VIGENC_CONV date null,  
-- 	DIA_FIM_VIGENC_ORIGINAL_CONV date null,
-- 	DIAS_PREST_CONTAS int4 null,
-- 	DIA_LIMITE_PREST_CONTAS date null, 
-- 	data_suspensiva date null,
-- 	data_retirada_suspensiva date null,
-- 	dias_clausula_suspensiva int4 null,
-- 	SITUACAO_CONTRATACAO varchar null,
-- 	ind_assinado varchar null,
-- 	motivo_suspensao varchar null,
-- 	ind_foto varchar null,
-- 	qtde_convenios int4 null,
-- 	QTD_TA int4 null,
-- 	QTD_PRORROGA int4 null,
-- 	VL_GLOBAL_CONV numeric(13, 2) null,
-- 	VL_REPASSE_CONV numeric(13, 2) null,
-- 	VL_CONTRAPARTIDA_CONV numeric(13, 2) null,
-- 	VL_EMPENHADO_CONV numeric(13, 2) null,
-- 	VL_DESEMBOLSADO_CONV numeric(13, 2) null,
-- 	VL_SALDO_REMAN_TESOURO numeric(13, 2) null,
-- 	VL_SALDO_REMAN_CONVENENTE numeric(13, 2) null,
-- 	VL_RENDIMENTO_APLICACAO numeric(13, 2) null,
-- 	VL_INGRESSO_CONTRAPARTIDA numeric(13, 2) null,
-- 	VL_SALDO_CONTA numeric(13, 2) null,
-- 	VALOR_GLOBAL_ORIGINAL_CONV numeric(13, 2) null
-- );


-- ================================================================================================
-- APLICAÇÃO
-- ================================================================================================
CREATE SCHEMA dm;
CREATE SCHEMA pcr_siconv;


CREATE TABLE dm.tb_comparison(
    id SERIAL PRIMARY KEY,
    file_csv_name TEXT NOT NULL,
    tb_name TEXT NOT NULL,
    create_table_from_csv TEXT NOT NULL,
    create_table_from_table TEXT NOT NULL,
    result TEXT NOT NULL,
    exec_start TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    exec_end TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW()
);



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





CREATE TABLE pcr_siconv.tb_acomp_obras_contratos_medicoes_modulo_empresas (
	id_proposta varchar NULL,
	id_contrato_medicao_acompanhamento_obra varchar NULL,
	id_medicao_acompanhamento_obra varchar NULL,
	data_inicio_obra_contrato_acompanhamento_obra date NULL,
	cnpj_fornecedor_contrato_acompanhamento_obra varchar NULL,
	numero_medicao_acompanhamento_obra varchar NULL,
	nr_ultima_medicao_acompanhamento_obra varchar NULL,
	situacao_medicao_acompanhamento_obra varchar NULL,
	data_inicio_medicao_objeto_acompanhamento_obra date NULL,
	data_fim_medicao_objeto_acompanhamento_obra date NULL,
	qtd_dias_sem_medicao_acompanhamento_obra int4 NULL,
	dthora_insert timestamp NULL,
	dthora_update timestamp NULL
);



CREATE TABLE pcr_siconv.tb_acomp_obras_valores_itens_medicao_modulo_empresas (
	id_submeta_vrpl varchar NULL,
	id_contrato_medicao_acompanhamento_obra varchar NULL,
	valor_execucao_fisica_acumulada_total_acompanhamento_obra numeric NULL,
	valor_execucao_fisica_acumulada_concedente_acompanhamento_obra numeric NULL,
	valor_execucao_fisica_acumulada_convenente_acompanhamento_obra numeric NULL,
	valor_execucao_fisica_acumulada_empresa_acompanhamento_obra numeric NULL,
	dthora_insert timestamp NULL,
	dthora_update timestamp NULL
);



CREATE TABLE pcr_siconv.tb_bancos (
	id serial4 NOT NULL,
	codigo bpchar(3) NOT NULL,
	nome varchar(255) NOT NULL,
	created_at timestamp(0) NULL,
	updated_at timestamp(0) NULL,
	CONSTRAINT tb_bancos_pkey PRIMARY KEY (id),
	CONSTRAINT tb_bancos_un UNIQUE (codigo)
);



CREATE TABLE pcr_siconv.tb_contrato_cipi (
	nr_contrato varchar NULL,
	data_inicio_vigencia_contrato date NULL,
	data_fim_vigencia_contrato date NULL,
	data_assinatura_contrato date NULL,
	data_publicacao_contrato date NULL,
	objeto_contrato varchar NULL,
	nr_processo_licitacao varchar NULL,
	receita_despesa varchar NULL,
	cod_orgao varchar NULL,
	desc_orgao varchar NULL,
	id_fornecedor_contrato varchar NULL,
	nome_fornecedor_contrato varchar NULL,
	tipo_aquisicao_contrato varchar NULL,
	nr_licitacao varchar NULL,
	valor_global_contrato numeric NULL,
	valor_acumulado numeric NULL,
	id_projeto_investimento varchar NULL,
	link_transparencia varchar NULL,
	modalidade_licitacao varchar NULL,
	situacao varchar NULL,
	sistema_origem varchar NULL,
	dthora_insert timestamp NULL,
	dthora_update timestamp NULL
);



CREATE TABLE pcr_siconv.tb_contratos (
	id_licitacao varchar NULL,
	nr_contrato varchar NULL,
	data_publicacao_contrato date NULL,
	data_assinatura_contrato date NULL,
	data_inicio_vigencia_contrato date NULL,
	data_fim_vigencia_contrato date NULL,
	objeto_contrato varchar NULL,
	tipo_aquisicao_contrato varchar NULL,
	valor_global_contrato numeric NULL,
	id_fornecedor_contrato varchar NULL,
	nome_fornecedor_contrato varchar NULL,
	dthora_insert timestamp NULL,
	dthora_update timestamp NULL
);




CREATE TABLE pcr_siconv.tb_desembolsos (
	id serial4 NOT NULL,
	id_desembolso varchar NULL,
	nr_convenio varchar NULL,
	dt_ult_desembolso date NULL,
	qtd_dias_sem_desembolso int4 NULL,
	data_desembolso date NULL,
	ano_desembolso varchar NULL,
	mes_desembolso varchar NULL,
	nr_siafi varchar NULL,
	ug_emitente_dh varchar NULL,
	observacao_dh varchar NULL,
	vl_desembolsado numeric(13, 2) DEFAULT 0 NULL,
	dthora_insert timestamp DEFAULT now() NULL,
	CONSTRAINT tb_desembolsos_pkey PRIMARY KEY (id),
	CONSTRAINT tb_desembolsos_ukey UNIQUE (id_desembolso, nr_convenio, data_desembolso, ano_desembolso, mes_desembolso, nr_siafi, ug_emitente_dh, vl_desembolsado)
);



CREATE TABLE pcr_siconv.tb_emendas_com_proposta (
	id bigserial NOT NULL,
	num_emenda varchar NOT NULL,
	cod_programa_emenda varchar NOT NULL,
	cnpj_beneficiario_emenda varchar NOT NULL,
	id_proposta varchar NOT NULL,
	qualif_proponente varchar NULL,
	nome_parlamentar varchar NULL,
	tipo_parlamentar varchar NULL,
	orcamento_impositivo varchar NULL,
	vlr_repasse_emenda_na_proposta varchar NULL,
	vlr_repasse_emenda_na_assinatura varchar NULL,
	dthora_insert timestamp DEFAULT now() NULL,
	dthora_update timestamp NULL,
	dthora_processa timestamp NULL
);


CREATE TABLE pcr_siconv.tb_emendas_sem_proposta (
	id bigserial NOT NULL,
	num_emenda varchar NOT NULL,
	cod_programa_emenda varchar NOT NULL,
	cnpj_beneficiario_emenda varchar NOT NULL,
	nome_parlamentar varchar NULL,
	tipo_parlamentar varchar NULL,
	orcamento_impositivo varchar NULL,
	vlr_repasse_emenda_na_proposta text NULL,
	dthora_insert timestamp DEFAULT now() NULL,
	dthora_update timestamp NULL,
	dthora_processa timestamp NULL
);



CREATE TABLE pcr_siconv.tb_historico_situacao (
	id serial4 NOT NULL,
	id_proposta varchar NOT NULL,
	dthora_hist_situ timestamp NOT NULL,
	hist_situ varchar NOT NULL,
	dias_hist_situ int4 NOT NULL,
	cod_hist_situ varchar NOT NULL,
	dthora_insert timestamp NULL,
	dthora_update timestamp NULL
);



CREATE TABLE pcr_siconv.tb_licitacoes (
	id_licitacao text NULL,
	nr_convenio text NULL,
	nr_licitacao text NULL,
	modalidade_licitacao text NULL,
	tp_processo_compra text NULL,
	tipo_licitacao text NULL,
	nr_processo_licitacao text NULL,
	data_publicacao_licitacao date NULL,
	data_abertura_licitacao date NULL,
	data_encerramento_licitacao date NULL,
	data_homologacao_licitacao date NULL,
	status_licitacao text NULL,
	situacao_aceite_processo_execu text NULL,
	sistema_origem text NULL,
	situacao_sistema text NULL,
	valor_licitacao text NULL,
	dthora_insert timestamp NULL,
	dthora_update timestamp NULL
);



CREATE TABLE pcr_siconv.tb_obtv_convenentes (
	id bigserial NOT NULL,
	nr_mov_fin varchar NOT NULL,
	id_favorecido_obtv_conv varchar NULL,
	nm_favorecido_obtv_conv varchar NULL,
	tp_aquisicao varchar NULL,
	vlr_pago_obtv_conv numeric(13, 2) NULL,
	dthora_insert timestamp NULL,
	dthora_update timestamp NULL
);



CREATE TABLE pcr_siconv.tb_orgao_sup (
	id serial4 NOT NULL,
	orgao_cod varchar NULL,
	orgao_nome varchar NULL,
	orgao_tipo bpchar(3) NULL,
	dt_insert date NULL
);




CREATE TABLE pcr_siconv.tb_plano_aplicacao_detalhado (
	id_proposta varchar NULL,
	sigla varchar NULL,
	municipio varchar NULL,
	natureza_aquisicao varchar NULL,
	descricao_item varchar NULL,
	cep_item varchar NULL,
	endereco_item varchar NULL,
	tipo_despesa_item varchar NULL,
	natureza_despesa varchar NULL,
	sit_item varchar NULL,
	cod_natureza_despesa varchar NULL,
	qtd_item float8 NULL,
	valor_unitario_item numeric NULL,
	valor_total_item numeric NULL,
	id_item_pad varchar NULL,
	dthora_insert timestamp NULL,
	dthora_update timestamp NULL
);



CREATE TABLE pcr_siconv.tb_portal_consulta_convenios_receita (
	nr_convenio varchar NOT NULL,
	url_dir_gdrive varchar NULL,
	datahora_modif_gdrive timestamptz NULL,
	link_transferegov varchar NULL
);




CREATE TABLE pcr_siconv.tb_prazo_intervalo (
	id serial4 NOT NULL,
	prazo_descr varchar NULL,
	prazo_dias_ini int4 NULL,
	prazo_dias_fim int4 NULL,
	prazo_ativo int4 NULL
);


CREATE TABLE pcr_siconv.tb_programa_proposta (
	id bigserial NOT NULL,
	id_programa varchar NULL,
	id_proposta varchar NULL
);



CREATE TABLE pcr_siconv.tb_programas (
	id serial4 NOT NULL,
	orgao_sup_cod varchar NOT NULL,
	orgao_sup_descr varchar NULL,
	prog_id varchar NULL,
	prog_cod varchar NOT NULL,
	prog_nome varchar NULL,
	prog_situacao varchar NULL,
	disponibiliza_data date NULL,
	disponibiliza_ano varchar NULL,
	data_ini_receb_prop date NULL,
	data_fim_receb_prop date NULL,
	data_ini_emenda_parlam date NULL,
	data_fim_emenda_parlam date NULL,
	data_ini_benef_esp date NULL,
	data_fim_benef_esp date NULL,
	modalidade varchar NOT NULL,
	nat_juridica varchar NOT NULL,
	unid_fed varchar NOT NULL,
	acao_orcam varchar NULL,
	dthora_insert timestamp NULL,
	dthora_update timestamp NULL,
	subtipo_programa_nome varchar NULL,
	subtipo_programa_desc varchar NULL,
	prog_nome_fts tsvector NULL
);



CREATE TABLE pcr_siconv.tb_proponentes_identif (
	identif_proponente bpchar(14) NULL
);



CREATE TABLE pcr_siconv.tb_propostas (
	id serial4 NOT NULL,
	id_proposta varchar NOT NULL,
	uf_proponente varchar NULL,
	munic_proponente varchar NULL,
	cod_munic_ibge varchar NULL,
	cod_orgao_sup varchar NULL,
	desc_orgao_sup varchar NULL,
	nat_juridica varchar NULL,
	nr_proposta varchar NULL,
	dia_prop int4 NULL,
	mes_prop int4 NULL,
	ano_prop int4 NULL,
	data_proposta date NULL,
	cod_orgao varchar NULL,
	desc_orgao varchar NULL,
	modalidade varchar NULL,
	identif_proponente varchar NULL,
	nm_proponente varchar NULL,
	cep_proponente varchar NULL,
	endereco_proponente varchar NULL,
	bairro_proponente varchar NULL,
	nm_banco varchar NULL,
	situ_conta varchar NULL,
	situ_proj_basico varchar NULL,
	situ_proposta varchar NULL,
	data_inic_vigencia_proposta date NULL,
	data_fim_vigencia_proposta date NULL,
	objeto_proposta varchar NULL,
	vlr_global_prop numeric(13, 2) NULL,
	vlr_repasse_prop numeric(13, 2) NULL,
	vlr_contrapartida_prop numeric(13, 2) NULL,
	dthora_insert timestamp NULL,
	dthora_update timestamp NULL,
	item_investimento varchar NULL,
	enviada_mandataria varchar NULL,
	nome_subtipo_proposta varchar NULL,
	desc_subtipo_proposta varchar NULL,
	cd_agencia varchar NULL,
	cd_conta varchar NULL
);



CREATE TABLE pcr_siconv.tb_pagamentos (
	id bigserial NOT NULL,
	nr_mov_fin varchar NOT NULL,
	nr_convenio varchar NULL,
	id_fornecedor varchar NULL,
	nm_fornecedor varchar NULL,
	tp_mov_fin varchar NULL,
	data_pagto date NULL,
	nr_dl varchar NULL,
	desc_dl varchar NULL,
	vlr_pago numeric(12, 2) NULL,
	dthora_insert timestamp NULL,
	dthora_update timestamp NULL
);

