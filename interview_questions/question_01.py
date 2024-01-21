# Find common letter between two strings:
def common_letter(str1,str2):
#Convert them to set to remove duplicates    
    s1 = set(str1)
    s2 = set(str2)
    # & in set will give common letters
    lst = s1 & s2
    print(list(lst))

common_letter('naina','reene')

# Count the frequency of words appearing in a string
str1 = 'sheena loves eating apple and mango.Her sister also loves eating mango and apple'
str2 = str1.split(' ')
d = {}
for i in str2:
    if i in d.keys():
       d[i]= d[i] +1
    else:
        d[i]= 1
print(d)    

#Convert list to a dictionary
keys = [1,2,3]
values= ['one','Two','Three']
result = dict(zip(keys,values))
print(result)

    


