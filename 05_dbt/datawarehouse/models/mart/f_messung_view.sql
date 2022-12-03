{{
    config(
        materialized='view'
    )
}}

with w_messung as (
    SELECT  staging.d_kunde_snapshot.d_kunde_key as d_kunde_key,
            staging.d_ort_table.d_ort_key as d_ort_messung_key,
	        staging.d_fahrzeug_incremental.d_fahrzeug_key as d_fahrzeug_key,
            staging.messung.erstellt_am as messung_eingetroffen,
            cast(payload ->> 'zeit' as timestamp) as messung_erzeugt, 
            cast(payload ->> 'geschwindigkeit' as int) as geschwindigkeit
    FROM staging.messung
    INNER JOIN staging.fahrzeug on staging.fahrzeug.fin = (staging.messung.payload ->> 'fin')
	INNER JOIN staging.d_fahrzeug_incremental on staging.d_fahrzeug_incremental.fin = cast(staging.messung.payload ->> 'fin' as char(17))
	INNER JOIN staging.d_kunde_snapshot on staging.d_kunde_snapshot.kunde_id = staging.fahrzeug.kunde_id
    INNER JOIN staging.ort on cast(payload ->> 'ort' as int) = staging.ort.ort_id
    INNER JOIN staging.d_ort_table on staging.d_ort_table.ort = staging.ort.ort
)
SELECT m.d_kunde_key, m.d_ort_messung_key, m.d_fahrzeug_key, m.messung_eingetroffen, m.messung_erzeugt, m.geschwindigkeit
FROM w_messung m