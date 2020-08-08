# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class MyspiderPipeline:
    def __init__(self):
        # connection database
        self.connect = pymysql.connect(host='localhost', user='root', passwd='123', db='hitsz')
        # get cursor
        self.cursor = self.connect.cursor()
        print("连接数据库成功")
    def process_item(self, item, spider):
        # sql语句
        insert_sql = "insert into news(id,url,title,date) VALUES (null,%s,%s,%s)"
        # 执行插入数据到数据库操作
        self.cursor.execute(insert_sql,(item['url'],item['title'],item['date']))
        # 提交，不进行提交无法保存到数据库
        self.connect.commit()
    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.connect.close()
