# How do you remove duplicates from list, while preserving the order
my_list = [1,5,2,1,8,5,3,2]
new_list = list(dict.fromkeys(my_list))
print(new_list)

#How to reverse  a list in place
my_list = [1,2,3,4,5]
my_list.reverse()
print(my_list)
