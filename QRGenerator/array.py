import json
x = {
    "name" : "ankit",
    "age" : 17, 
    "city" : "new york",
    "married" : True,
    "divorce" : False,
    "children" : ("ankit","virat"),

    "cars" : [
        {"model" : "ferrari","brand" : "mustang"},
        {"model" : "jaguar","brand" : "hyundai"}
    ]
    }
print(json.dumps(x, indent = 4,sort_keys=True))






















