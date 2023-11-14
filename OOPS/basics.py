class mobile:
    pass

mob1 = mobile()  #object
mob2 = mobile()

mob1.price = 2000  # attribute
mob1.brand = 'apple'
print(mob1.price)
print(mob1.brand)

#Sample class with constructor
class mobile:
    def __init__(self,brand,price): #constructor
        print('Inside constructor')
        self.brand = brand
        self.price = price
mob1 = mobile('Apple',2000)
print(mob1.brand, mob1.price)   

# ​​​​​​​Destructor is a special method which will be invoked automatically 
# when the object gets removed from the memory.  
class mobile:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    def __del__(self):
        print('Deleting object')
p1 = mobile('Apple',2000)
p2 = mobile('Samsung',2300)        

del p1 # alternate way of deleting object

# Method in a class
class product:
    def __init__(self):
        print('Inside constructor')
    def purchase(self):
        print('Purchasing a product')
p1 = product()
p1.purchase()
