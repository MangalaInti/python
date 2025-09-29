Lambda function is an anonymous function i.e without any name. Function can have any number of parameters in one statment
syntax : lambda argruments : expression

#Multiply with a number
val = lambda i: i*2
print(val(25))

#Multiply 3 arguments
val = lambda x,y,z : x*y*z
print(val(20,2,1))

# Maximum of two numbers using lambda
res = lambda x,y : x if (x >y)  else y
print(res(50,100)) 

# square of number using lambda
val = lambda i : i*i
print(val(9))

**Map funcion
Map function takes two argments
map(function, iterable) 
   - Function will be applied to each item in iterable
   - Iterable is like list, tuple etc

#Square of each item
numbers = [1,2,3,4]
res = list(map(lambda x: x**2, numbers))
print(res)

#custom function
def capitalize(word):
  return word.upper()
words = ['hello', 'world']

res = map(capitalize, words)
print(list(res))



