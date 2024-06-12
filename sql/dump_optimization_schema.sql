create schema optimizations;

CREATE TABLE optimizations.a (
    aid int,
    a_str varchar,
    q json
);

CREATE TABLE optimizations.b (
    bid int,
    b_str varchar,
    val bigint
);

CREATE TABLE optimizations.c (
    cid int,
    c_str varchar,
    val bigint,
    period timestamp with time zone
);

create or replace function get_random_number(from_value bigint, to_value bigint)
returns bigint
language plpgsql
as
$$
begin
    return floor(random() * from_value + to_value);
end;
$$;

create or replace function get_random_timestamp()
returns timestamp
language plpgsql
as
$$
begin
    return timestamp '2014-01-10 20:00:00' +
       random() * (timestamp '2014-01-20 20:00:00' -
                   timestamp '2014-01-10 10:00:00');
end;
$$;

create or replace function get_random_text()
returns varchar
language plpgsql
as
$$
begin

end;
$$;


insert into a
select
    generate_series(100, 1000000),
    concat(get_random_number(1, 30), 'a', get_random_number(90, 100)),
    cast(concat('{"test_val', get_random_number(100, 200), '" : ', get_random_number(300, 500), ' }') as json);


insert into b
select
    generate_series(200000, 400000),
    concat(generate_series(200, 205), 'b_table', generate_series(0, 5)),
    cast(random() * 11235450000000 + 99999999990000000 as bigint);

insert into c
select
    generate_series(0, 10000),
    concat(get_random_number(100, 1000000), 'text', random()::varchar, get_random_number(10, 10000)),
    get_random_number(1, 922337203685477580),
    get_random_timestamp();

create index a_index_a_str_btree on a using btree (a_str);

create index a_index_a_str_heap on a using hash (q);