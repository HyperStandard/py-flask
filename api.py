from asyncio import Lock
from flask import render_template

__author__ = 'nonex_000'

class PyFlaskApi:
    def GetData(data):
        return "got data" + data

    def get_data(data):
        return "data got " + data

    def get_user(user):
        return "user got " + user

    def get_page(page):
        return render_template("")

    def get_chat(self):
        lock = Lock()
        with lock:
            lock.acquire()


