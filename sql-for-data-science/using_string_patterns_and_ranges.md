- Retrieving rows using a string pattern

select <columns_name> from <table_name> where <columns_name> like 'R%'

Output:

column
------------
Raul
Rav

- Retrieving rows using a range

select tile , page from Book where pages >= 290 AND pages <=300
select tile , page from Book where pages between 290 AND 300

- Retrieving rows using a set of values

select first_name, last_name from author where country='AU' OR country='BR'