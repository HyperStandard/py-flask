from __future__ import with_statement

import datetime

__author__ = 'nonex_000'

import sqlite3


class DataBase:
    def __init__(self):
        DATABASE_NAME = "assets/databases/chats.db3"

        # self.connection = sqlite3.connect(DATABASE_NAME)
        self.connection = sqlite3.connect(':memory:')

        self.cur = self.connection.cursor()

        self.cur.execute("CREATE TABLE IF NOT EXISTS chats ("
                         "date TEXT, time TEXT, message TEXT, name TEXT)")

    @staticmethod
    def _get_date():
        return datetime.date.isoformat(datetime.datetime.now().date())

    @staticmethod
    def _get_time():
        return datetime.time.isoformat(datetime.datetime.now().time())

    def _total_messages(self):
        # return the total number of messages in the database
        return self.cur.execute("SELECT count(message) FROM chats").fetchone()[0]
        #fetchone returns a tuple, then use array accessor to get first
        #aka only value

    def add_to_db(self, message, database):
        query = u"INSERT INTO chats ( date, time, message, name ) VALUES ( '{date:s}', '{time:s}', '{message:s}', 'nobody' )" \
            .format(**{"date": self._get_date(), "time": self._get_time(), "message": message})
        print(query)
        self.cur.execute(query)
        self.connection.commit()

    def get_from_db(self, start, end):
        # prevent accessing items that don't exist
        max_message = self._total_messages()

        # get the total number of messages to return
        number_of_messages = (min(end, max_message) - start)

        # get the chats in the selected range
        query = "SELECT message FROM chats LIMIT {limit:d} OFFSET {offset:d}" \
            .format(**{"limit": number_of_messages, "offset": start})

        results = self.cur.execute(query).fetchall()
        result_string = ""
        for result in results:
            result_string += ("<br>" + result[0])
        return result_string


    def if_table_exists(self):
        pass

    def close(self):
        self.cur.close()
