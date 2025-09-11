# print characters that occur the most
str1 = 'programming'
dict1 = {}

for char in str1:
  if char in dict1:
    dict1[char] = dict1[char] +1
else:
  dict1[char] =1
print(dict1)

max_value = max(dict1.values())

max_chars = [k for k, v in dict1.items() if max_value == v]
print(max_chars)
