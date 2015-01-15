from __future__ import with_statement

import datetime

__author__ = 'nonex_000'

import sqlite3

DATABASE_NAME = "assets/databases/chats.db3"

connection = sqlite3.connect(DATABASE_NAME)

cur = connection.cursor()

cur.execute("create table if not exists chats ("
            "date text, message text, name text)")

def get_date():
    return datetime.date.isoformat(datetime.datetime.now().date())

def get_time():
    return datetime.time.isoformat(datetime.datetime.now().time())

def add_to_db(message, database):
    cur.execute("INSERT INTO chats ( DATE, TIME, MESSAGE, NAME) VALUES ( " + get_date() + ", " + get_time() + ", " + message + "nobody)")


def if_table_exists():
    pass

