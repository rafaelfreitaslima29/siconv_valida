TRUNCATE TABLE experimento.tb_metricas RESTART IDENTITY RESTRICT;




select
--	t1.id,
--	id_tb_avaliacao,
--	ta.id,
--	ta.llm_model,
--	create_table_from_csv,
--	tx_metr2_criou_ddl_csv_col_faltantes,
	--
	ta.llm_model,
	bo_metr1_criou_ddl_csv_todas_col,
	tx_metr3_criou_ddl_csv_col_extras,
	bo_metr4_nome_col_alterado,
	tx_metr4_saida_col_verif_ms_col_sql,
	bo_metr5_add_coluna,
	tx_metr5_saida,
	resultado,
	---
	bo_metr6_sql_resolve ,
	ta.*
from
	experimento.tb_metricas t1
left join experimento.tb_avaliacao ta on t1.id_tb_avaliacao = ta.id
--where ta.llm_model = 'llama3.2:3b'
order by ta.id

;



with 
base as (
	select
		t1.id,
		id_tb_avaliacao,
		ta.id,
		ta.llm_model,
		create_table_from_csv,
		bo_metr1_criou_ddl_csv_todas_col,
		tx_metr2_criou_ddl_csv_col_faltantes,
		tx_metr3_criou_ddl_csv_col_extras,
		bo_metr4_nome_col_alterado,
		bo_metr5_add_coluna,
		bo_metr6_sql_resolve
	from experimento.tb_metricas t1
	left join experimento.tb_avaliacao ta 
		on t1.id_tb_avaliacao = ta.id
	order by t1.id_tb_avaliacao
)
select 
	llm_model,
	sum(bo_metr1_criou_ddl_csv_todas_col::INT) as soma_csv_suc,
--	sum(tx_metr2_criou_ddl_csv_col_faltantes::INT) as soma_criados_sucesso,
--	sum(tx_metr3_criou_ddl_csv_col_extras::INT) as soma_tx_metr3_criou_ddl_csv_col_extras,
	sum(bo_metr4_nome_col_alterado::INT) as soma_bo_metr4_nome_col_alterado,
	sum(bo_metr5_add_coluna::INT) as soma_bo_metr5_add_coluna,
	sum(bo_metr6_sql_resolve::INT) as soma_cbo_metr6_sql_resolve
--* 
from base
group by llm_model
;




