{{
    config(
        materialized='incremental',
        unique_key="d_fahrzeug_key"
    )
}}

with w_fahrzeug as (
    SELECT staging.fahrzeug.fin, cast(staging.fahrzeug.baujahr as int), staging.fahrzeug.modell, staging.hersteller.hersteller, staging.kfzzuordnung.kfz_kennzeichen 
    FROM staging.fahrzeug
    INNER JOIN staging.hersteller on staging.hersteller.hersteller_code = staging.fahrzeug.hersteller_code
    INNER JOIN staging.kfzzuordnung on staging.kfzzuordnung.fin = staging.fahrzeug.fin
)
SELECT ROW_NUMBER() OVER () as d_fahrzeug_key, f.fin, f.baujahr, f.modell, f.hersteller, f.kfz_kennzeichen
FROM w_fahrzeug f