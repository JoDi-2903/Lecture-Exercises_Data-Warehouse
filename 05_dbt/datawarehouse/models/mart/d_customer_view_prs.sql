{{
    config(
        materialized='view'
    )
}}

with w_cust as (
    select *
    from {{ source('abu', 'stg_customer_prs') }}
)
select c.customerid
     , c.customername
     , c.insertedat
from w_cust c