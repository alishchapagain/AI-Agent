"""
info={
    "name" : "Note Mandir",
    "subject" : ["Physics","Chemistry","Computer"],
    "topics" : ("dict", "sets"),
    "age" : 25,
    "is_adult" : False,
    "followers" : 1.7
}

print(info)
print(type(info))

#info["name"]="Alish" - Changing the value
print(info)

#creating null dictionary
null_dict = {}
null_dict["name"] = "Hitesh xyz"
print(null_dict)

"""

#Nested Dictionary
Student={
    "Name" : "Alish",
    "Subject" :{ #another dictionaty
        "Math": 45,
        "OOP" : 50,
        "MP" : 45,
    }
}

print(Student)
print(Student["Subject"])
# print(Student["Subject"]["Math"]) #printing marks of math

#method of dictionary
print(Student.keys())

print(Student.values())

print(list(Student.values())) #print values as a list

print(Student.items())

print(Student.get("Name"))

"""
print(Student.get("Name")) and print(Student["Name"]) are same but if
we use method then we won't get error if the key is not found in the dictionaty,
if we use print method then it will throw error if key not found
"""

Student.update({"city": "Belbari"})
print(Student)