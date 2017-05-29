# -*- coding: utf-8 -*-
from functools import lru_cache, wraps

import pymysql

DEBUG = False

def _print(message):
    """

    :param message:
    :return:
    """
    if message and DEBUG:
        _print(message)

def retry(count=5, exc_type=Exception):
    """ Retry Decorator

    :param count:
    :param exc_type:
    :return:
    """
    def decorator(func):
        @wraps(func)
        def result(*args, **kwargs):
            for _ in range(count):
                try:
                    return func(*args, **kwargs)
                except exc_type:
                    pass
                raise Exception

        return result

    return decorator

# @lru_cache()
def get_db_connection():
    """ A Utility to return the DB Connection

    :return:
    """
    from app.views import DB_HOST, DB_USER, DB_PWD, DB_NAME

    @lru_cache()
    def connection(DB_HOST, DB_USER, DB_PWD, DB_NAME):
        return pymysql.connect(host=DB_HOST,
                               user=DB_USER,
                               password=DB_PWD,
                               db=DB_NAME,
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)

    return connection(DB_HOST, DB_USER, DB_PWD, DB_NAME)


def insert_into_ltp_table(inv_time, data_dict):
    """Inserts the Date into the LTP Table

    :param time:
    :param data_dict:
    :return:
    """
    # Structure of the dict
    # {
    #     "tradeable": False,
    #     "mode": self.MODE_LTP,
    #     "instrument_token": instrument_token,
    #     "last_price": self._unpack_int(packet, 4, 8) / divisor
    # }

    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO zerodhastreamquotes_modeltp (InstrumentToken, Tradeable, Timestamp, LastTradedPrice, Mode) VALUES (%s, %s, %s, %s,%s)"
            cursor.execute(sql, (
            data_dict.get('instrument_token'), data_dict.get('tradeable'), inv_time, data_dict.get('last_price'),
            data_dict.get('mode')))
        # connection is not autocommit by default. So we do an explicit commit here
        connection.commit()
        _print("Inserted %s into LTP Table" % data_dict)
    except Exception as connexc:
        _print("Connection Error %s" % str(connexc) )
    finally:
        connection.close()


def fetch_ltp_results():
    """

    :return:
    """
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * from zerodhastreamquotes_modeltp"
            cursor.execute(sql)
            return cursor.fetchall()
    finally:
        connection.close()


class QueueFullException(Exception):
    pass

if __name__ == '__main__':
    _print(insert_into_ltp_table('11111', {}))