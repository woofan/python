#!python3
#-*-coding:utf-8-*-
from pymongo import MongoClient

class Mongo(object):
    """docstring for Mongodb."""
    def __init__(self,db_name,collection_name):
        self.url = 'mongodb://localhost'
        self.db_name = db_name
        self.collection_name = collection_name
        self.username = ''
        self.password = ''
        self.client = MongoClient(self.url)
        self.client_col = self.client[self.db_name][self.collection_name]


    def close(self):
        self.client.close()

    def saveToMongodb(self,info):
        try:
            self.client_col.save(info)
        except Exception as e:
            print (e)
            print('保存进数据库失败')
            return False
        return True

    def getDBInfo(self):
        cursor = self.client_col.find()
        return cursor

    def findOneBook(self,bookid):
        return self.client_col.find_one({'bookid':bookid})


#与数据库建立连接
def getClient(url='mongodb://localhost'):
    try:
        client = MongoClient(url)
        return client
    except Exception as e:
        print (e)
        print('连接指定集合失败！')
        return False

#断开连接
def closeClient(client):
    client.close()

#该函数接受希望保存进数据库的数据集（字典形式的）和一个name做该文档的_id。保存方式为save，意味着每次都会覆盖同意id的数据
def saveToMongodb(info,mycollection):
    try:
        mycollection.save(info)
    except Exception as e:
        print (e)
        print('保存进数据库失败')
        return False
    return True

#该函数返回指定数据库、集合的所有文档的游标
def getDBInfo(myclient,db,collection_name):
    mydb = myclient[db]
    mycollection = mydb[collection_name]
    cursor = mycollection.find()
    return cursor

#--------------------------------------------------------
if __name__=='__main__':
    c = getBDInfo('test1','books3')
    for x in range(0,3):
        if c[x]:
            print(c[x])
