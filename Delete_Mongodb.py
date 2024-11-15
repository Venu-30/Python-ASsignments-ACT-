import pymongo


client=pymongo.MongoClient("mongodb://localhost:27017")
db=client["ACT_DB"]
collection=db["STUDENT_INFO"]
query={"Student_ID":445}
collection.delete_one(query)
print("Your document deleted successfully:\n")
