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


