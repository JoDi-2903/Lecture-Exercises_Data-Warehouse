{{
    config(
        materialized='table'
    )
}}

with w_ort as (
    SELECT staging.ort.ort, staging.land.land, staging.ort.ort_id FROM staging.ort 
    INNER JOIN staging.land on ort.land_id = land.land_id
)

select ROW_NUMBER () OVER (ORDER BY ort_id) as d_ort_key, o.ort, o.land
from w_ort o