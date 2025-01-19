create table first (
    field int
);

create table second (
    field int
);

select
    *
from test.first
left join test.second on first.field = second.field;

select
    generate_series(100, 1000000);
     ,
    concat(get_random_number(1, 30), 'a', get_random_number(90, 100)),
    cast(concat('{"test_val', get_random_number(100, 200), '" : ', get_random_number(300, 500), ' }') as json);

create or replace function test.get_random_number(from_value bigint, to_value bigint)
returns bigint
language plpgsql
as
$$
begin
    return floor(random() * from_value + to_value);
end;
$$;

create or replace function get_random_timestamp(from_date timestamp, to_date timestamp)
returns timestamp
language plpgsql
as
$$
begin
    return timestamp '2014-01-10 20:00:00' +
       random() * (timestamp '2014-01-20 20:00:00' - timestamp '2014-01-10 10:00:00');
end;
$$;

create schema test;
create table test.transactions (
    id serial,
    amount bigint,
    trans_date timestamp
);


insert into transactions (amount, trans_date)
SELECT get_random_number(1, 100) * generate_series(100, 1000000),
       timestamp '2014-01-20 20:00:00' + generate_series(50, 100) * random() * interval '1 day';


select random() * (timestamp '2014-01-20 20:00:00' - timestamp '2014-01-10 10:00:00');

insert into transactions (amount, trans_date)
select timestamp '2014-01-20 20:00:00' + interval '1 day' * generate_series(1, 100);

insert into transactions (amount, trans_date)
select generate_series(1, 10000000) * floor(random() * get_random_number(100000, 100000000)),
       timestamp '2014-01-20 20:00:00' + random() * interval '1 mons 10 days' * generate_series(-1000, 10000);

update transactions
set trans_date = '2018-12-20 20:00:00'
-- from (values (timestamp '2014-01-20 20:00:00' + interval '1 day' * generate_series(1, 100))) as temp(d)
where trans_date is null;

update transactions
set amount = get_random_number(10000, 10000000)
where amount is null;

explain analyse
update transactions
set trans_date = trans_date + random() * interval '1 mons 10 days';




with main_data as (
    select
        *,
        row_number() over (partition by temp.rank_number order by temp.trans_date desc) as numb
    from (select *,
                 rank() over (order by date(trans_date)) as rank_number
          from transactions
          order by trans_date) as temp
)
select
    date(trans_date),
    id,
    amount
from main_data
where main_data.numb = 1
limit 10 offset 50;

WITH RankedTransactions AS (
    SELECT
        trans_date,
        id,
        amount,
        ROW_NUMBER() OVER (PARTITION BY DATE(trans_date) ORDER BY trans_date DESC) AS row_num
    FROM transactions
)
SELECT
    date(trans_date),
    id,
    amount
FROM RankedTransactions
WHERE row_num = 1
limit 10 offset 50;


WITH RankedTransactions AS (
    SELECT
        trans_date,
        id,
        amount,
        DATE_TRUNC('day', trans_date) AS trans_day
    FROM transactions
)
SELECT
    trans_date,
    id,
    amount
FROM RankedTransactions
WHERE trans_day = (
    SELECT trans_day
    FROM RankedTransactions
    WHERE amount = (
        SELECT MAX(amount)
        FROM RankedTransactions s
        WHERE s.trans_day = RankedTransactions.trans_day
    )
)
ORDER BY trans_date DESC;


create index on transactions(trans_date);