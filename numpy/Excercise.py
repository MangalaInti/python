import numpy as np

new_array = np.array([1,2,3,4,5])

float_array = np.array([3.5,2.5,6.7])

string_array = np.array(['oranges', 'mangoes'])

print(type(new_array))

#To get the datatype of an array

print(float_array.dtype)

#Convert float to int array
float_to_int_array = np.array([1.2,3.4,5.6], dtype=np.int32)
print(float_to_int_array)

# Accessing values from arrays
print(float_to_int_array[0:2])

#Boolean list
sample_list = [1,2,3,6,7]
boolean_list = []
for i in sample_list:
    if i>3:
        boolean_list.append('True')
    else:
        boolean_list.append('False')
print(boolean_list)  


#Numpy Matrix and multidimensional arrays

import numpy as np

mat = np.matrix([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(mat.shape)

# Accessing a matrix
print(mat[1,1])

import numpy as np

#numpy methods and operations
#Linespace
array_with_linespace = np.linspace(1,10,5)
print(array_with_linespace)
#Arange
array_with_arange = np.arange(1,10,0.5)
print(array_with_arange)

print(np.zeros((2,3)))
print(np.ones((1,5)))

------------------------------

import numpy as np
list = [[1,2,3],[5,6,7],[3,4,5]]
arr = np.array(list)
print(arr)
shape = arr.shape
print(shape, 'shape') # number of rows and columns
size = arr.size
print(size,'size') # number of elements
dim = arr.ndim # number of opening brackets
print(arr.dtype) # to know datatype
print(dim)

# Array indexing and slicing

print(arr[0,2]) #o/p is  3
