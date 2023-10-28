#Remove the duplicate and preserver the order
nums = [0,0,0,1,1,2,3,3,4,5]
res = []
for n in nums:
    if n not in res:
        res.append(n)
print(res)        

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

#Slice list into 3 equal chunks and reverse each chunk

s1 = [11, 45, 8, 23, 14, 12, 78, 45, 89]

size = len(s1)//3

for n in range(0,len(s1),size):
    temp = s1[n:n+size]
    temp.reverse()
    print(temp)

#Replace list’s item with new value if found
list1 = [5, 10, 15, 20, 25, 50, 20]
index = list1.index(20)
list1[index] =200
print(list1)    

#Remove all occurrences of a specific item  20 from a list.
list1 = [5, 20, 15, 20, 25, 50, 20]
while 20 in list1:
     list1.remove(20)
print(list1)    
    
