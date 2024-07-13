1. What type of inheritance is illustrated in the following Python code?

class A():
    pass
class B(A):
    pass
class C(B):
    pass
	
Explanation: In multi-level inheritance, a subclass derives from another class which itself is derived from another class.	

Single level inheritance

Explanation: In single-level inheritance, there is a single subclass which inherits from a single superclass. So the class definition of the subclass will be: class B(A): where A is the superclass.

---
class A:
     def __init__(self):
         self.__i = 1
         self.j = 5
 
     def display(self):
         print(self.__i, self.j)
class B(A):
     def __init__(self):
         super().__init__()
         self.__i = 2
         self.j = 7  
c = B()
c.display()


(1,7)
Answer: c
Explanation: Any change made in variable i isn’t reflected as it is the private member of the superclass.

Explanation: If the value of a private variable in a superclass is changed in the subclass, the change isn’t reflected.


