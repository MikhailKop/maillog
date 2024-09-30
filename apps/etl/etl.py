import fcntl
import logging

import psycopg2
from config import settings
from extract import MaillogExtractor
from load import MaillogLoader
from transform import TransformData
from utils import setup_logging

setup_logging()


def acquire_lock(file_path):
    """Acquire a file lock to ensure a single instance of the script runs."""
    lock_file = open(file_path, "w")
    try:
        fcntl.lockf(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
        return lock_file
    except IOError:
        raise RuntimeError("Another instance is already running.")


def etl():
    extractor = MaillogExtractor()
    loader = MaillogLoader()

    try:
        logging.info("Starting ETL process.")
        data = extractor.read_file()
        log_data, message_data = TransformData(data).transform()
        loader.load(log_data, message_data)
        logging.info("ETL process completed successfully.")
    except (psycopg2.DatabaseError, psycopg2.OperationalError) as pg_error:
        logging.error(f"PostgreSQL error: {pg_error}")
    except KeyboardInterrupt:
        logging.info("ETL process interrupted by user.")
    except Exception as e:
        logging.error(f"Error: {e}")


if __name__ == "__main__":
    setup_logging()
    try:
        lock_file = acquire_lock(settings.lock_file)
        etl()
    except RuntimeError as e:
        logging.error(e)
