from pymongo import MongoClient
MongoURI = ''
conn = MongoClient(MongoURI)

DB = conn['Task-Mangement']

taskCollection = DB['tasks']
userCollection = DB['user']