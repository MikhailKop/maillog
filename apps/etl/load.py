import logging
from contextlib import contextmanager

import psycopg2
from backoff_decorator import backoff
from config import settings
from psycopg2.extras import DictCursor


@contextmanager
def postgres_conn_context(dsl):
    """Context manager for PostgreSQL connection"""
    conn = psycopg2.connect(**dsl, cursor_factory=DictCursor)
    try:
        yield conn
    except psycopg2.Error as e:
        conn.rollback()
        raise e
    else:
        conn.commit()
    finally:
        conn.close()


class MaillogLoader:
    def __init__(self):
        self.dsl = self._get_dsn()

    def _get_dsn(self):
        return {
            "dbname": settings.db_name,
            "user": settings.db_user,
            "password": settings.db_password,
            "host": settings.db_host,
            "port": settings.db_port,
        }

    @backoff(
        start_sleep_time=0.1,
        factor=2,
        border_sleep_time=10,
        exceptions=(psycopg2.OperationalError,),
    )
    def load(self, log_data: list, message_data: list):
        with postgres_conn_context(self.dsl) as conn:
            with conn.cursor() as cursor:

                args = ','.join(cursor.mogrify("(%s,%s,%s,%s)",
                                (row.created, row.int_id, row.str_,
                                 row.address)).decode('utf-8')
                                for row in log_data)

                cursor.execute(f'INSERT INTO log (\
                                 created, int_id, str, address)\
                                 VALUES {(args)}')
                logging.info('Loading data into table "log" completed.')

                args = ','.join(cursor.mogrify("(%s,%s,%s,%s)",
                                (row.created, row.id, row.int_id, row.str_)).
                                decode('utf-8') for row in message_data)

                cursor.execute(f'INSERT INTO message (created, id, int_id, str)\
                                 VALUES {(args)} ON CONFLICT (id) DO NOTHING')
                logging.info('Loading data into table "message" completed.')
