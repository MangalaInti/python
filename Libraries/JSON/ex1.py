
# conversion of dict vice versa 
 import json
 data = {"key1" : "value1", "key2" : "value2"}

 res = json.dumps(data)            # convert dict to json string
 parsed = json.loads(res)          # convert json string back to dict 
 # To access any values in python we need to convert to dictionary

print(parsed["key2"])

# Readable format

import json
data = {"key1" : "value1", "key2" : "value2"}
res = json.dumps(data, indent =2 separator = (",", "="))
print(res)

# Sort the json keys and write them to  a file

import json
samplejson = {"id" : 1, "name" : "value1", "age" : 26}

print(" started writing json data into a file")
with open("outfile.json", mode = "w", encoding = "utf8") as f:
  json.dump(outfile, f,indent = 2, sort_keys = "True")

# Conver the following vechile object into json

import json
from json import JSONEncoder

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

class VehicleEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

v1 = Vehicle("Toyota Rav4", "2.5L", 32000)

print("Encode Vehicle Object into JSON")
vehicleJson = json.dumps(v1, indent=4, cls=VehicleEncoder)
print(vehicleJson)
     





