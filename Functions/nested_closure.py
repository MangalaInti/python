#Nested function is function inside another function
def outer_sum(a,b):
    def inner_sum():
        return a+b
    return inner_sum()
print(outer_sum(5,3))

# We need to have return keyword for inner_sum to return the value to outer function
