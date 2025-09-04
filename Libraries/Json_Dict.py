json.loads() => Used to convert json data to python dictionary, Output is string
json.load() = > write to a file

--You use json.loads() when your data is already in your python pgm

----Function             Input Type           Typical Use case
-----------------------------------------------------------------------
  json.loads()        JSON string             When you have JSON as a string
  json.load()         File Object             When reading JSON from a file 

# Json  to python object
import json

json_str = '{"name" : "mangala", "role": "consultant"}'

data = json.loads.(json_str)
print(data["name"])    #mangala

# Loading Json as File object

import json

with open('data.json', 'r') as f:
  data = json.load(f)
print(data["name"])






