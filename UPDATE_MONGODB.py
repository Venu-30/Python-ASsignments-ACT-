import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017")
db=client["ACT_DB"]
collection=db["STUDENT_INFO"]
query={"Student_ID":425}
new_values={"$set":{"Student_Name":"Vinayak"}}
collection.update_one(query,new_values)
for i in collection.find():
    print("students Details are:\n",i)