# Replace all occurence of 20 with 200
list1 = [5, 10, 15, 20, 25, 50, 20]
list1 = list(map(lambda x: 200 if x == 20 else x, list1))
print(list1)
#Method II
list1 = [5, 10, 15, 20, 25, 50, 20]

for i in range(len(list1)):
    if list1[i] == 20:
        list1[i] = 200

print(list1)

#Write function to flatten the nested list
def flatten_nested_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            # recursive call to the same function
            result.extend(flatten_nested_list(item))
        else:
            result.append(item)
    return result


nested_list = [1, [2, [3, 4], 5], 6]
print(flatten_nested_list(nested_list))

# Given two lists, write a function to find the common elements
def common_elements(lst1, lst2):
 set1 = set(list1)
 set2 = set(list2)   
 return list(set1.intersection(set2))

list1 = [10,20,30,40]
list2 = [20,40,60,80]  
print(common_elements(list1,list2))  



