{{
    config(
        materialized='incremental'
    )
}}

with w_cust as (
    select *
    from {{ source('abu', 'stg_customer_trs') }}
    
    -- filter for an incremental run to get new data
    {% if is_incremental() %}

    -- no filter for incremental/delta load. Filter just for full/initial load

    {% endif %}

)
select c.customerid
     , c.customername
     , c.insertedat
from w_cust c