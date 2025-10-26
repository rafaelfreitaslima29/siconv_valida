CREATE SCHEMA experimento; 

-- experimento.convenios definition

-- Drop table

-- DROP TABLE experimento.convenios;

CREATE TABLE experimento.convenios (
	nr_convenio varchar NOT NULL,
	id_proposta varchar NOT NULL,
	dia int4 NULL,
	mes int4 NULL,
	ano int4 NULL,
	dia_assin_conv date NULL,
	sit_convenio varchar NULL,
	subsituacao_conv varchar NULL,
	situacao_publicacao varchar NULL,
	instrumento_ativo varchar NULL,
	ind_opera_obtv varchar NULL,
	ug_emitente varchar NULL,
	dia_publ_conv date NULL,
	dia_inic_vigenc_conv date NULL,
	dia_fim_vigenc_conv date NULL,
	dia_fim_vigenc_original_conv date NULL,
	dias_prest_contas int4 NULL,
	dia_limite_prest_contas date NULL,
	data_suspensiva date NULL,
	data_retirada_suspensiva date NULL,
	dias_clausula_suspensiva int4 NULL,
	sit_contratacao varchar NULL,
	ind_assinado varchar NULL,
	motivo_suspensao varchar NULL,
	ind_foto varchar NULL,
	qtde_convenios int4 NULL,
	qtd_ta int4 NULL,
	qtd_prorroga int4 NULL,
	vl_global_conv numeric(13, 2) NULL,
	vl_repasse_conv numeric(13, 2) NULL,
	vl_contrapartida_conv numeric(13, 2) NULL,
	vl_empenhado_conv numeric(13, 2) NULL,
	vl_desembolsado_conv numeric(13, 2) NULL,
	vl_saldo_reman_tesouro numeric(13, 2) NULL,
	vl_saldo_reman_convenente numeric(13, 2) NULL,
	vl_rendimento_aplicacao numeric(13, 2) NULL,
	vl_ingresso_contrapartida numeric(13, 2) NULL,
	vl_saldo_conta numeric(13, 2) NULL,
	valor_global_original_conv numeric(13, 2) NULL
);


-- experimento.tb_avaliacao definition

-- Drop table

-- DROP TABLE experimento.tb_avaliacao;

CREATE TABLE experimento.tb_avaliacao (
	id serial4 NOT NULL,
	llm_model text NOT NULL,
	file_csv_name text NOT NULL,
	tb_name text NOT NULL,
	create_table_from_csv text NOT NULL,
	create_table_from_table text NOT NULL,
	resultado text NOT NULL,
	exec_start text NULL,
	exec_end text NULL,
	CONSTRAINT tb_avaliacao_pkey PRIMARY KEY (id)
);
CREATE INDEX ix_experimento_tb_avaliacao_id ON experimento.tb_avaliacao USING btree (id);


-- experimento.tb_metricas definition

-- Drop table

-- DROP TABLE experimento.tb_metricas;

CREATE TABLE experimento.tb_metricas (
	id serial4 NOT NULL,
	id_tb_avaliacao int4 NULL,
	bo_metr1_criou_ddl_csv_todas_col bool NULL,
	tx_metr2_criou_ddl_csv_col_faltantes varchar NULL,
	tx_metr3_criou_ddl_csv_col_extras varchar NULL,
	bo_metr4_nome_col_alterado bool NULL,
	tx_metr4_saida_col_verif_ms_col_sql varchar NULL,
	bo_metr5_add_coluna bool NULL,
	tx_metr5_saida varchar NULL,
	bo_metr6_sql_resolve bool NULL,
	CONSTRAINT tb_metricas_pkey PRIMARY KEY (id)
);