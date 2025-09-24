#Slice list into 3 equal chunks and reverse each chunk

s1 = [11, 45, 8, 23, 14, 12, 78, 45, 89]
# Calculate chunk size
chunk_size = len(s1) // 3
# Slice into 3 chunks
chunks = [s1[i:i + chunk_size] for i in range(0, len(s1), chunk_size)]
chunks.reverse()
print(chunks)

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
    
