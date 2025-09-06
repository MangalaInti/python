# Remove empty elements from the list
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

filtered_list = list(filter(None,list1))
print(filtered_list)

# Remove duplicates from list
list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]

#convert list to set
unique_elements = list(set(list_with_duplicates))
print(unique_elements)

# Remove all the items that occur more than once in a list

list1 = [5, 20, 15, 20, 25, 50, 20]     
freq = {}

#Build frequency dictionary
for item in list1:
    freq[item] = freq.get(item,0) +1

# keep only items with count == 1  
list2=  [x for x in list1 if freq[x] ==1 ] 
print(list2)



***Explanation*****
Start: freq = {} (empty)

First item = 5
freq.get(5, 0) → since 5 is not in freq, it returns 0.
freq[5] = 0 + 1 = 1
Now freq = {5: 1}

Next item = 20
freq.get(20, 0) → returns 0 (not present yet).
freq[20] = 0 + 1 = 1
Now freq = {5: 1, 20: 1}

Next item = 15
freq.get(15, 0) → returns 0.
freq[15] = 0 + 1 = 1
Now freq = {5: 1, 20: 1, 15: 1}

If another 20 comes later:

freq.get(20, 0) → returns 1 (since already exists).

freq[20] = 1 + 1 = 2

So it updates the count automatically.
