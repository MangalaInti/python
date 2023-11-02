#Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

my_dict = {keys[i]: values[i] for i in range(len(keys))}
print(my_dict)
#Alternate way to above problem

result_dict = {i: j for i, j in zip(keys, values)}

print(result_dict)

#Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = {**dict1, **dict2}
print(dict3)

#Alternate way

dict1.update(dict2)
print(dict1)
#Create a dictionary by extracting the keys from a given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

dict1 = {k: sample_dict[k] for k in keys}
print(dict1)
