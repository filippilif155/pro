from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from bson.json_util import dumps
from bson.objectid import ObjectId
import pymongo
import security
import Courses
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["CoursesAPI"]
'''
schem = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": [ "username", "password", "email", "role"],
        "properties": {
          "username": {
             "bsonType": "string",
             "description": "must be a string and is required"
          },
          "password": {
             "bsonType": "string",
             "description": "must be a string and is required"
          },
          "email" : {
              "bsonType": "string",
              "description": "must be a string and is required"

          },
          "role":{
            "bsonType": "int",
            "description": "must be a string and is required"
                  

          }
        }
    }
  }
'''
if not "teachers" in mydb.list_collection_names():
    mycol_teachers = mydb.create_collection("teachers")
    mycol_teachers.create_index("username", unique=True)
else:
    mycol_teachers = mydb["teachers"]

class Teacher(Resource):
    def get(self, username):
        try:
            teacher = list(mycol_teachers.find({"username": username}))
            if teacher:
                return dumps(teacher), 200
            else:
                return None, 404
        except Exception as e:
            return {"error": str(e)}, 400


    def post(self, username): 
        try:
            request_data = request.get_json() 
            new_teacher = {
                "username": request_data["username"],
                "password": request_data["password"],
                #"index": request_data["index"]
            }
            mycol_teachers.insert_one(new_teacher)
            return dumps(new_teacher), 201
        except Exception as e:
            return {"error": str(e)}, 400
