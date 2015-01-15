from __future__ import with_statement

import datetime

__author__ = 'nonex_000'

import sqlite3

class DataBase:

    def __init__(self):
        DATABASE_NAME = "assets/databases/chats.db3"

        self.connection = sqlite3.connect(DATABASE_NAME)

        self.cur = self.connection.cursor()
        
        self.cur.execute("create table if not exists chats ("
                    "date text, message text, name text)")

    def get_date(self):
        return datetime.date.isoformat(datetime.datetime.now().date())

    def get_time(self):
        return datetime.time.isoformat(datetime.datetime.now().time())

    def add_to_db(self, message, database):
        query = u"INSERT INTO chats ( DATE, TIME, MESSAGE, NAME) VALUES ( '{date:s}', '{time:s}', '{message:s}', 'nobody' )" \
            .format(**{"date": self.get_date(), "time": self.get_time(), "message": message})
        print(query)
        self.cur.execute(query)
        self.connection.commit()

    def if_table_exists(self):
        pass

    def close(self):
        self.cur.close()
