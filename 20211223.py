# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pymongo

client=pymongo.MongoClient("10.0.4.76",27017)

db=client.mydb #選擇買DB資料庫

collection = db.student #選擇stucent
for i in range(0,10000000):
   std=collection.insert_one({ "name":'林均苔', "by":'臭狗'})
print(std)
sum=0
for i in collection.find():
    print(i)
    sum+=1
    
print(sum)#顯示幾筆資料