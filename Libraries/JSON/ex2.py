# Parse the following JSON to get all the values of a key ‘name’ within an array
import json
samplejson = """
[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""

# Parse JSON string into Python list of dictionaries

res = json.loads(samplejson)
print(res)

# Extract all 'name' values
names = [item["name"] for item in res]

print("All 'name' values:", names)

