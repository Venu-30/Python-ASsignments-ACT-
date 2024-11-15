import pymongo
#write a code to connect to server
client=pymongo.MongoClient("mongodb://localhost:27017")
#write a code to connect desired database over the mongodb
db=client["ACT_DB"]
#write a code to connect collection or table
collection=db["STUDENT_INFO"]
#create data in the form of dictionary/key:value pair
data=[{"Student_ID":425,"Student_Name":"Vijay","Student_Course":"EIE","Student_No":"6144455880"},
      {"Student_ID":452,"Student_Name":"Vinay","Student_Course":"EEE","Student_No":"6125896310"},
      {"Student_ID": 425, "Student_Name": "Bhaskar", "Student_Course": "ECE", "Student_No": "6144569871"},
      {"Student_ID": 445, "Student_Name": "Jhonny", "Student_Course": "CSE", "Student_No": "6269874531"},
      {"Student_ID": 455, "Student_Name": "Bobby", "Student_Course": "IT", "Student_No": "9876543210"},
      {"Student_ID": 465, "Student_Name": "Nikhil", "Student_Course": "AIML", "Student_No": "9032165487"},
      {"Student_ID": 475, "Student_Name": "DIVIJ", "Student_Course": "MECH", "Student_No": "7032165498"}]
X=collection.insert_many(data)
print("data has been inserted into desired location")
print("Primary Keys:\n",X.inserted_ids)