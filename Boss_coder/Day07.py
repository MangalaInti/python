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
