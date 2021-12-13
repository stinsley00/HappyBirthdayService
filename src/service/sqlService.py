import psycopg2
import psycopg2.extras
from src import utils


class PgUtils:
    def __init__(self, conn_str):
        self.conn_str = conn_str
        self.log = utils.get_module_logger(__name__)

    def get_birthday(self, schema, column_list):
        """gets today's birthdays"""
        col_list = ",".join(column_list)
        # print(col_list)
        sql = f"""
                select {col_list}
                from 
                {schema}.person p
                where p.date_of_birth::DATE = now()::DATE; 
        """
        self.log.debug(sql)
        try:
            conn = psycopg2.connect(self.conn_str)
            cur = conn.cursor()
            cur.execute(sql)
            result_value = cur.fetchall()
            conn.commit()
            cur.close()
            # list of [tuple]
            if result_value:
                return result_value
            else:
                return None
        except psycopg2.OperationalError as e:
            self.log.warning(f"Error occured: {e}")
            exit()
        except Exception as e:
            self.log.warning(f"Other Error occured: {e}")
            exit()