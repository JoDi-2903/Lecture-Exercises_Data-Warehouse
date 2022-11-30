insert into abu.stg_customer_prs values (1, 'Cust1_change', to_date('02.02.2020', 'DD.MM.YYYY'));
insert into abu.stg_customer_prs values (3, 'Cust3', to_date('02.02.2020', 'DD.MM.YYYY'));

truncate table abu.stg_customer_trs;
insert into abu.stg_customer_trs values (1, 'Cust1_change', to_date('02.02.2020', 'DD.MM.YYYY'));
insert into abu.stg_customer_trs values (3, 'Cust3', to_date('02.02.2020', 'DD.MM.YYYY'));
