#Remove the duplicate and preserver the order
nums = [0,0,0,1,1,2,3,3,4,5]
res = []
for n in nums:
    if n not in res:
        res.append(n)
print(res)   

# Method2
 x = dict1.fromkeys(nums)
 print(x)

#method3
# Remove duplicates from list
list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]

#convert list to set
unique_elements = list(set(list_with_duplicates))
print(unique_elements)

# sample indexing
str = 'apple' #5
for i in range(len(str)):
    print(str[i])

#Count the occurrence of each element from a list
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

cnt_dict = {}
for element in sample_list:
    if element in cnt_dict:
        cnt_dict[element] = cnt_dict[element] +1
    else:
        cnt_dict[element] =1
     
print(cnt_dict)          

    
