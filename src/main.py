import psycopg2

from src import utils
from src.config import Config
from src.service import emailService
from src.service import sqlService

# init
config = Config()
log = utils.get_module_logger(__name__)

if __name__ == '__main__':
    # for demonstration purposes.  SSL + Secrets manager irl
    try:
        connStr = config.CONN_STR.format("localhost", "postgres", "postgres", config.PG_PASSWD, "5432")
        sqlService = sqlService.PgUtils(connStr)
        birthdayList = sqlService.get_birthday("public", config.DB_COLS)

        if birthdayList:
            # for each birthday we need to send a happy birthday message.
            for item in birthdayList:
                log.info(f"name is: {item[0]} and email is: {item[1]}")
                emailService.config_and_send_mail(item[0], "Happy birthday!!!", "We hope you have a great birthday!", item[1])
    except ConnectionError as e:
        log.warning(e)

