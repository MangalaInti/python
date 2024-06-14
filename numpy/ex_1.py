#Create a NumPy array containing random integers between 0 and 9 with shape `(3, 3)

import numpy as np
random_array  = np.random.randint(0,9,size = (3,3))
print(random_array)

#Add 5 to each element of the array `[1, 2, 3, 4, 5]
import numpy as np
list = [1, 2, 3, 4, 5]
arr = np.array(list)
new_arr  = arr+5
print(new_arr)
