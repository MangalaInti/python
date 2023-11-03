#Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

print(min(sample_dict.keys()))

#Rename key of a dictionary
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sample_dict['location'] = sample_dict.pop['city']
print(sample_dict)

#Check if a value exists in a dictionary
sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
    print('200 present in dict')

    
