#Create a function to find the length of longest word in sentence
def longest(sen):
    words = sen.split()
    max_length = 0
    longest_word = ""
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            longest_word = word
    return max_length, longest_word

length, word = longest('Hello Pramaan Welcome to NJ')
print(f"The longest word is '{word}' with length {length}.")

#Given the list of names, count the number of names that start with vowel
def count_names_starting_with_vowel(names):
    vowels = ('a', 'e', 'i', 'o', 'u')
    count = 0
    for name in names:
        if name.lower().startswith(vowels):
            count += 1
    return count

print(count_names_starting_with_vowel(['Hello', 'Pramaan', 'Welcome', 'to', 'NJ', 'Alice', 'Eve']))
 



