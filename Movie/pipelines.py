# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import MySQLdb
from MySQLdb import cursors
from twisted.enterprise import adbapi
# from scrapy import log

class MoviePipeline(object):
    def __init__(self):
        self.file = codecs.open('movies.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line.decode("unicode_escape"))
        return item

class MovieMySQLPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool("MySQLdb",

                                            host="localhost",
                                            db="tongle",
                                            user="root",
                                            passwd="",
                                            cursorclass=MySQLdb.cursors.DictCursor,
                                            charset="utf8",
                                            use_unicode=True
                                            )

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        # query.addErrback(self.handle_error)
        return item

    def _conditional_insert(self, tb, item):
        print  '------'
        # 删除所有数据
        # tb.execute("DELETE FROM TABLE_NAME ")

        # 插入数据，prince_link[0]取出list列表中的数据
        # for i in range(0, 45):
            # print item['movie_title'][i].encode("utf-8"), '......'
        M_title = 0
        director = 0
        actors = 0
        rate = 0
        region = 0
        region = 0
        date = 0
        duration = 0
        ticket = 0
        if len(item['movie_title']):
            M_title = item['movie_title'][0]
        else:
            print '...'
        if len(item['movie_director']):
            director = item['movie_director'][0]
        else:
            print '...'
        if len(item['movie_actors']):
            actors = item['movie_actors'][0]
        else:
            print '...'
        if len(item['movie_rate']):
            rate = item['movie_rate'][0]
        else:
            print '...'
        if len(item['movie_region']):
            region = item['movie_region'][0]
        else:
            print '...'
        if len(item['movie_date']):
            date = item['movie_date'][0]
        else:
            print '...'
        if len(item['movie_duration']):
            duration = item['movie_duration'][0]
        else:
            print '...'
        if len(item['movie_ticket']):
            ticket = item['movie_ticket'][0]
        else:
            print '...'

        tb.execute("INSERT INTO  tongle.Movies(movie_title, movie_director, movie_actors, movie_rate, movie_region, movie_date, movie_duration, movie_ticket) VALUES ('%s', '%s', '%s','%s', '%s', '%s','%s', '%s')" % (
            M_title,
             director,
             actors,
             rate,
             region,
             date,
             duration,
             ticket ))

