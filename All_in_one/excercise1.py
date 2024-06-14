#split a string
s = 'Hi there Sam!'
d = s.split()
print(d)

#Given two variables use .format() to print the string
planet = 'Earth'
diameter = 12747
print("The diameter of {} is {} kilometers.".format(planet,diameter))
print(f'The diameter of {planet} is {diameter} kilometers.')

#Create a function that grabs email website domain from string
# for e.g passing email.domain.com would return domain.com

def emailget(email):
    return email.split('@')[-1]
res = emailget('email@domain.com')    
print(res)

#Create function that return True if the word 'dog' contained in string
def finddog(string):
    if 'dog' in string.lower():
        return True
    else:
        return False
finddog('Is there a dog there')  

#Create function to count the number of times word 'dog' occurs in string
def countdog(st):
    count = 0
    for word in st.lower().split():
        if word == 'dog':
            count = count+1
        return count
countdog('This dog runs faster than the other dog dude!')    

#Use lambda exp and filter() to filter out the words from the list don't start with letter 's'
seq = ['soup','dog','salad','cat','great']
res = list(filter(lambda word: word[0] =='s', seq))
print(res)

""" You are driving a little too fast, and a police officer stops you. Write a function
  to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
  If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
  and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
  cases. """ 
  def caught_speeding(speed, is_birthday):
    
    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed
    
    if speeding > 80:
        return 'Big Ticket'
    elif speeding > 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'

caught_speeding(81,True)
caught_speeding(81,False)    

#List of elements identical
my_list = [1,1,1,1,1]
all_identical = len(set(my_list)) == 1
print(all_identical)
OR
my_list = [1, 1, 1, 1]

all_identical = my_list.count(my_list[0]) == len(my_list)
print(all_identical)  # Output: True

# Loop Over Multiple Sequences
first_names = ['mangala','Pramaan','Prabhu']
last_names = ['inti','inti','mushini']

for first, last in zip(first_names,last_names):
    print(first,last)
#Difference between two lists
lst1 = [9,3,6,7,8,4]
lst2 = [9,3,7,5,2,1]

diff = set(lst1).difference(set(lst2))
print(list(diff))    

#Indices Using Len & Range Functions
names = ['john','eric','matt']

for n in range(len(names)):
    print(n, names[n])

names = ['John', 'Art', 'Messi']
for i in range(len(names)):
if names[i] == 'Messi':
print(f'The index of the name {names[i]} is {i}')
break
Output:
The index of the name Messi is 2

