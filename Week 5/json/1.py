'''
Exercises to parse json data in python
'''
import json


with open("E:\Project PP2\Week 5\json\sample-data.json") as jsonFile:
    sampleData = json.load(jsonFile)
    jsonFile.close()



print("Interface Status")
print("=" * 84)
print("DN", " " * 49, "Description", " " * 11, "Speed", " " * 4, "MTU")
print("-" * 50, " ", "-" * 20, " " * 2, "-" * 6, " " * 2, "-" * 6) 

count = 0 
for i in sampleData["imdata"]: 
    if count == 3:
        break
    print(i["l1PhysIf"]["attributes"]["dn"], " " * 30,i["l1PhysIf"]["attributes"]["speed"], " " * 3, i["l1PhysIf"]["attributes"]["mtu"])
    count += 1
