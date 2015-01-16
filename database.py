from __future__ import with_statement

import datetime

__author__ = 'nonex_000'

import sqlite3


class DataBase:
    def __init__(self):
        DATABASE_NAME = "assets/databases/chats.db3"

        self.connection = sqlite3.connect(DATABASE_NAME)

        self.cur = self.connection.cursor()

        self.cur.execute("CREATE TABLE IF NOT EXISTS chats ("
                         "date TEXT, message TEXT, name TEXT)")

    @staticmethod
    def _get_date():
        return datetime.date.isoformat(datetime.datetime.now().date())

    @staticmethod
    def _get_time():
        return datetime.time.isoformat(datetime.datetime.now().time())

    def add_to_db(self, message, database):
        query = u"INSERT INTO chats ( DATE, TIME, MESSAGE, NAME) VALUES ( '{date:s}', '{time:s}', '{message:s}', 'nobody' )" \
            .format(**{"date": self._get_date(), "time": self._get_time(), "message": message})
        print(query)
        self.cur.execute(query)
        self.connection.commit()

    def get_from_db(self):
        pass

    def if_table_exists(self):
        pass

    def close(self):
        self.cur.close()
