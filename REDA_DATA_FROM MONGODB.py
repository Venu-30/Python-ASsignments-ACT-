import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017")
db=client["ACT_DB"]
collection=db["STUDENT_INFO"]
for i in collection.find():
    print("Student_details:\n",i)