# -*- coding: utf-8 -*-
__author__ = 'changwei'

from os import path
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
import sqlite3


class NoteBookPipeline(object):
    def __init__(self):
        self.conn = None
        self.filename = 'note.db'
        dispatcher.connect(self.initialize, signals.engine_started)
        dispatcher.connect(self.finalize, signals.engine_stopped)

    def process_item(self, item, spider):
        self.conn.execute('insert into fjsen values(?,?,?,?,?,?)', (None, item['model'][0], item['price'][0], item['sales'][0], item['dealer'][0], item['pic'][0]))
        return item

    def initialize(self):
        if path.exists(self.filename):
            self.conn = sqlite3.connect(self.filename)
        else:
            self.conn = self.create_table(self.filename)

    def finalize(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn = None

    @staticmethod
    def create_table(filename):
        conn = sqlite3.connect(filename)
        conn.execute("""create table fjsen(id integer primary key autoincrement, model text, price text, sales text, dealer text, pic text)""")
        conn.commit()
        return conn
