__author__ = 'nonex_000'

from Flask import g

from __future__ import with_statement

import sqlite3

DATABASE_NAME = "/assets/databases/chat.db"

connection = sqlite3.connect(DATABASE_NAME)

cur = connection.cursor()

cur.execute("create table if not exists chats ("
            "date text, message text, name text)")

