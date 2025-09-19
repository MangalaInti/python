--Sort() method is in-place sort, it modifies the orginal list directly. It doesn't return newlist

lst = ['zebra','ballon','apple','snake']
lst.sort()
print(lst)

--Sorted() function creates a new  sorted list, leaving the orginal list unchanged.

lst = ['zebra','ballon','apple','snake']
lst1 = sorted(lst)
print(lst1)

--Custom sorting with Key
Both sort() and sorted() accept an optional key argument. Key is a function that is called on each element
of the list before comparision is made.
use the key arguments to customize the sortng logic based on specific attribute or transformation of the elements

--syntax
your_list.sort(key =your_custom_function)

sorted_list = sorted(your_list, key = your_custom_function)

# sort the string based on length lowest

words = ['apple','banana','kiwi','grape']
sorted_words = sorted(words, key =len)
print(sorted_words)

#sort based on length highest
sorted_words = sorted(words, key =len, reverse=True)

# Sort by Lastname
names = ['John smith','Jane Doe','Alice Johnson']

sorted_names = sorted(names, key =lambda name: name.split()[-1])
print(sorted_names)

# Sort Dictionary by value

score = {'Alice':88, 'Bob':95, 'Charlie':78}

sorted_score = sorted(score, key=lambda item: item[1])
print(sorted_score)

# case in-sensitive sort
words = ['Apple','banana','Kiwi','grape']

words_sorted = sorted(words, key = lambda s: s.lower())
print(words_sorted)

