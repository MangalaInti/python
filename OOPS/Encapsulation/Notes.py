1. Encapsulation is kind of lock that prevents others from accessing your property.
2. Lock can be put on that data by adding a double underscore in front of it.
    e.g Private, proctected variables
3. Adding a double underscore makes the scope of the attribute as private. 
   Private attributes are those which are accessible only inside the class. 
  This method of restricting access to our data is called Encapsulation.
4. Getter and setter methods are used to access private variables


#All setter methods must accept the value to be updated as a parameter and 
# all getter methods must not have any parameter and they must return the value.
class customer:
    def __init__(self,id,name,age,wallet_balance):
        self.id = id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance
    def set_wallet_balance(self,amount):
        if amount < 1000 and amount >0:
            self.__wallet_balance =  amount
    def get_wallet_balance(self):
        return self.__wallet_balance   
c1 = customer(100,'Pramaan',12,1000)
c1.set_wallet_balance(120)     
print(c1.get_wallet_balance())    


So far you have learnt that:

Encapsulation is preventing access to a data outside the class

Adding a __ (double underscore) in front of an attribute makes it private

Getter and Setter methods should be used to access a private attribute

