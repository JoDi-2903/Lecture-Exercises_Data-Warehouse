-- drop schema abu cascade;
create schema abu;

create table abu.stg_customer_prs (customerid integer, customername varchar(100), insertedat timestamp);
create table abu.stg_customer_trs (customerid integer, customername varchar(100), insertedat timestamp);

