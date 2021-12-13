import unittest

import psycopg2
import testing.postgresql
from src.service import sqlService
from src.config import Config
from textwrap import dedent

config = Config()

def handler(postgresql):
    """inserts some data for testing purposes"""
    conn = psycopg2.connect(**postgresql.dsn())
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE if not exists public.person (
                date_of_birth date NULL, --IRL this would likely be epoch time
                person_name varchar NULL,
                person_email varchar NULL, 
                id uuid not NULL);""")
    cursor.execute(dedent("""INSERT INTO public.person (date_of_birth, person_name, person_email, id)
                   VALUES(now()::Date, 'local smokey', 'lsmokey@example.com',gen_random_uuid());"""))
    cursor.execute("""INSERT INTO public.person (date_of_birth, person_name, person_email, id)
                   VALUES('1983-01-12'::Date, 'makers mark', 'mmark@example.com',gen_random_uuid())""")
    cursor.execute("""INSERT INTO public.person (date_of_birth, person_name, person_email, id)
                   VALUES(now()::Date, 'wild turkey', '101@example.com',gen_random_uuid())""")

    cursor.close()
    conn.commit()
    conn.close()


# Generate Postgresql class which shares the generated database
Postgresql = testing.postgresql.PostgresqlFactory(cache_initialized_db=True, on_initialized=handler)


class TestDB(unittest.TestCase):
    def setUp(self):
        self.postgresql = Postgresql()

    def tearDown(self):
        self.postgresql.stop()
        # clear cache in the shared module
        Postgresql.clear_cache()

    def test_query(self):
        print(self.postgresql.dsn())

        columns = ['person_name', 'person_email', 'date_of_birth']
        conn = config.CONN_STR.format(self.postgresql.dsn()['host'], self.postgresql.dsn()['database'],self.postgresql.dsn()['user'],
                               None, self.postgresql.dsn()['port'])
        sql = sqlService.PgUtils(conn)
        sql_result = sql.get_birthday(schema='public', column_list=columns)
        print(sql_result)
        assert sql_result
