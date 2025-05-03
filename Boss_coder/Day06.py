#Given list of numbers find sum and average using built in functions
def calculate(list1):
   total = sum(list1)
   average = total/len(list1)
   return total, average
print(calculate([1,2,3,4,5]))  

#Given the list of words, find the word with maximum length  and its length
#Method 1

def words_longest_len(words):
    max_word = ''
    max_word_len = 0
    for word in words:
        if len(word) > max_word_len:
            max_word_len = len(word)
            max_word = word
    return max_word, max_word_len

print(words_longest_len(['apple', 'orange', 'greenapple', 'jack']))

#Method2
def find_longest_word(words):
    if not words:
        return None, 0  # Handle empty list
    longest = max(words, key=len)
    return longest, len(longest)

# Example usage
words = ["apple", "banana", "cherry", "watermelon"]
print(find_longest_word(words))

# pgm to count the occurences of each element in a given list
def occurence(list1):
      count_dict ={}
      for element in list1:
          if element in count_dict:
               count_dict[element] = count_dict[element] +1
          else:
               count_dict[element] = 1
      return count_dict              
print(occurence([1,1,2,3,4,3,5]))

#write a function that takes a list of strings and returns list sorted by the length of the strings
def sorted_length_strings(strings):
    
   return sorted(strings, key = len)
print(sorted_length_strings(['Jack','Matt','Pramaan','Joe']))    

# Check if the given list is sorted 
def Check_sorted(list1):
    list2 = sorted(list1)
    return list1 == list2
   
print(Check_sorted(['Jack','Matt','Pramaan','Joe']))    

#Implement a function that takes two lists and returns their union(all unique elements from both lists)

def union(list1, list2):
    list3 = list(set(list1 + list2))
    return list3
print(union([1,2,3,4],[3,2,1,5]))
    
    


   

