# Convert python dictionary to json 
import json
food_rating = {"organic_dog_food" : 2, "human_food" : 10}
print(json.dumps(food_ratings))

O/P = > '{"organic_dog_food" : 2, "human_food" : 10}'
.dumps = >  will convert python dict to json object
.dumps =>  when you use .dumps you will python string in return 

--When you convert a dictionary to JSON, the dictionary keys will always be string in JSON

numbers = {1: 'True', 2 : 'False'}
print(json.dumps(numbers))
O/P = > '{"1" : true, "2" : false}'

--Working variables in Dictionary
 dog_id = 1
 dog_name = "Frieda"
 dog_registry = {dog_id: {"name": dog_name}}
 json.dumps(dog_registry)
o/p = > '{"1": {"name": "Frieda"}}'

--Passing additional arguments
import json
toy_conditions = {"chew bone": 7, "ball": 3, "sock": -1}
result = json.dumps(toy_conditions, sort_keys = True)
print(result)

resule = > import json

toy_conditions = {"chew bone": 7, "ball": 3, "sock": -1}
print(result)

o/p = > result = json.dumps(toy_conditions, sort_keys = True)

--Saving the json result to .json file
json.dumps  => "Dump to string"  i.e output Returns A String
json.dum =>  "Dump to a File"

import json

dog_data = {
    "name": "Frieda",
    "is_dog": True,
    "hobbies": ["eating", "sleeping", "barking"],
    "age": 8,
    "address": {
        "work": None,
        "home": ("Berlin", "Germany"),
    },
    "friends": [
        {
            "name": "Philipp",
            "hobbies": ["eating", "sleeping", "reading"],
        },
        {
            "name": "Mitch",
            "hobbies": ["running", "snacking"],
        },
    ],
}

# Full file path
file_path = r"C:\Users\manga\Documents\Mangala\Python\Python_code\output.json"

# Write JSON to file
with open(file_path, mode="w", encoding="utf8") as f:
    json.dump(dog_data, f, indent=2)




