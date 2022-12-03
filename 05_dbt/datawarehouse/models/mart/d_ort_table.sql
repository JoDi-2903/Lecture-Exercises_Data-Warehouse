{{
    config(
        materialized='table',
        unique_key="d_ort_key"
    )
}}

with w_ort as (
    SELECT ROW_NUMBER() OVER (ORDER BY staging.land.land_id) as d_ort_key, staging.ort.ort, staging.land.land 
    FROM staging.ort
    INNER JOIN staging.land on ort.land_id = land.land_id
)
SELECT o.d_ort_key, o.ort, o.land
FROM w_ort o