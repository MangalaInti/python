#Write  a function that finds the most frequent element in a list
def most_frequent(mylist):
    frequency = {}
    
    # Count the frequency of each element
    for element in mylist:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    
    most_frequent = None
    max_count = 0
    
    # Find the element with the highest frequency
    for item, count in frequency.items():
        if count > max_count:
            most_frequent = item
            max_count = count
    
    # Return the most frequent element and its count
    return most_frequent, max_count

# Example usage
my_list = [1, 2, 3, 2, 3, 3, 4, 5, 6, 2, 3]
result = most_frequent(my_list)
print(f"The most frequent element is: {result[0]} with a frequency of {result[1]}")

#Find the dictionary with the highest value for a specific key
dict1 = {'a': 1, 'b': 5, 'c': 8, 'd': 2}

max_key = max(dict1, key =dict1.get)
#To key value pair
max_item = {max_key:dict1[max_key]}
print(max_key)
print(max_item)

#Write a pgm that counts the number of occurences of each character in a 
# given string using a dictionary   

input_str = "Hello world!"
char_count = {}

for char in input_str:
    if char in char_count:
        char_count[char] = char_count[char] +1
    else:
        char_count[char] = 1
print(char_count)  

#Given two sets, find union, Difference between them, intersection
set1 = {1,2,3,4}
set2 = {3,4,5,6}

#Union
union_set = set1 | set2
print(union_set)
#Intersection
Intersection_set = set1 & set2
print(Intersection_set)
#Difference (elements present in set1 not in set2)
Difference_set1 = set1 - set2
print(Difference_set1)
Difference_set2 = set2 - set1
print(Difference_set2)

| → Union

& → Intersection

- → Difference

 #Create a function that takes a list of dictionaries and sorts them based on a speficied key
def sort_dict_by_keys(data,sort_key):
    return sorted(data, key = lambda x: x[sort_key])

list1 = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}, {"name": "joe", "age": 35},
     {"name": "Jill", "age": 32}]

sorted_list1 = sort_dict_by_keys(list1, 'age')
print(sorted_list1)

#Write a pgm that finds the average value of all the elements in alist of dictionaries

list1 = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}, 
         {"name": "joe", "age": 35}, {"name": "Jill", "age": 32}]

# Extract ages and compute average
avg = sum(d['age'] for d in list1) / len(list1)
print(f"Average age: {avg}")

This version uses a generator expression inside sum() to avoid creating an intermediate list (list2), which is more memory-efficient and concise

#Implement a function that takes a list of strings  and returns a set of unique characters present in all strings

def unique_character_lst_strings(lst1):
    unique_character = []
    
    for word in lst1:
        for letter in word:
            if letter not in unique_character:
                unique_character.append(letter)
    return unique_character

# Now outside the function
lst1 = ['mangoes', 'apples', 'kiwi']
res = unique_character_lst_strings(lst1)
print(res)








