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
