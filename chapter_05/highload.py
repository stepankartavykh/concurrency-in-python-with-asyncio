import asyncio
import asyncpg


def select_query(id_: int) -> str:
    return f"""
        SELECT
        p.product_id,
        p.product_name,
        p.brand_id,
        s.sku_id,
        pc.product_color_name,
        ps.product_size_name
        -- pg_sleep(1)
        FROM product as p
        JOIN sku as s on s.product_id = p.product_id
        JOIN product_color as pc on pc.product_color_id = s.product_color_id
        JOIN product_size as ps on ps.product_size_id = s.product_size_id
        WHERE p.product_id = {id_}
    """


def update_client_account_query(id_: int) -> str:
    return "SELECT * FROM accounts WHERE client = 'bob';"


async def main():
    async with asyncpg.create_pool(host='127.0.0.1',
                                   port=5444,
                                   user='postgres',
                                   password='password',
                                   database='products',
                                   min_size=6,
                                   max_size=6) as pool:
        pass


if __name__ == '__main__':
    asyncio.run(main())
