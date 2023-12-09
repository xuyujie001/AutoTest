#1创建类
#2初始化数据，连接数据库，光标对象
#3创建查询、执行方法
#4关闭对象

import pymysql
from utils.LogUtil import my_log
class Mysql:
    def __init__(self,host,user, password, database, charset="utf8",port=3306,cursor_type=pymysql.cursors.DictCursor):
        self.log =my_log("mysql")
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            charset=charset)
        self.cursor = self.conn.cursor(cursor=cursor_type)

    def fetchone(self,sql,args=None):#单个查询
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def fetchall(self, sql,args=None):#多个查询
        try:
            self.cursor.execute(sql,args)
            return self.cursor.fetchall()
        except Exception as err:
            self.log.error(f"执行出错，错误信息：{err}")

    def exec(self,sql,args=None):#执行
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql)
                self.conn.commit()
        except Exception as  ex:
            self.conn.rollback()
            self.log.error("mysql执行失败")
            self.log.error(ex)
    def __del__(self):#关闭对象
        if self.cursor is not None:#关闭光标对象
            self.cursor.close()
        if self.conn is not None:#关闭连接对象
            self.conn.close()

if __name__ == '__main__':
    mysql = Mysql()