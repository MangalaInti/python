
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


