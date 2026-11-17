import json
from pprint import pprint 

#f = open("Woche6/jsonFile01.json")
##
#json.load(f)
#json.close(f)


def load_json_from_path(path):
    with open(path) as f:
        return json.load(f)
   

obj1 = load_json_from_path("jsonFile01.json")
obj2 = load_json_from_path("jsonFile02.json")
obj3 = load_json_from_path("jsonFile03.json")

pprint(obj1)


if obj1 == obj2:
    equal = True
else:
    equal = False 


print (f"obj1 and obj2 are equal: {equal}")

if obj1 == obj3:
    equal = True
else:
    equal = False 


print (f"obj1 and obj3 are equal: {equal}")