# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class QuotetoscrapePipeline(object):

        # def __init__(self):
        #         self.createConnection()
        #         self.createTable()

        # def createConnection(self):
        #         self.conn = sqlite3.connect('Quotes.db')
        #         self.curr = self.conn.cursor()

        # def createTable(self):
        #         self.curr.execute("""DROP TABLE IF EXISTS quotesTable  """)
        #         self.curr.execute(""" create table quotesTable(
        #                 Title text,
        #                 Author text,
        #                 Tags text
        #         ) """)

        def process_item(self, item, spider):

                # self.StoreDB(item)
                # print("Pipeline")
                return item

        # def StoreDB(self, item):
        #         self.curr.execute(""" insert into quotesTable values (?, ?, ?)""" ,(
        #                 item['Title'] [0],
        #                 item['Author'] [0],
        #                 item['Tags'] [0]
        #         ))
        #         self.conn.commit()