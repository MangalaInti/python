class student:
    def __init__(self,student_id = None,marks= None,age = None, course_id = None, fees = None):
        self.student_id = student_id
        self.__marks = marks
        self.__age = age
        self.__course_id = course_id
        self.__fees = fees
        
    def set_student_id(self,student_id):
        self.__student_id = student_id
    def get_student_id(self):
        return self.__student_id

    def set_marks(self,marks):
        self.__marks = marks
    def get_marks(self):
        return self.__marks

    def set_age(self,age):
      self.__age=age
    def get_age(self):
      return self.__age

    def set_course_id(self,course_id):
      self.__course_id=course_id
    def get_course_id(self):
      return self.__course_id
    
    def set_fees(self,fees):
      self.__fees=fees
    def get_fees(self):
      return self.__fees    

    def validate_marks(self):
        if self.__marks >= 0 and self.__marks <= 100:
            return True
        else:
            return False  
    def validate_age(self):
        if self.__age > 20:
            return True
        else:
            return False
    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
          if self.__marks>=65:
             return True
          else:
             return False
        else:
         return False
    def choose_course(self,course_id):
       if self.__course_id>=1001 and self.__course_id<=1002:
       if self.__marks>85 and self.validate_age():
        self.amount=self.__fees*0.75
print('Total fees amount for Student Id: ',self.__student_id,'course Id: ',self.__course_id,'is',self.amount)

S1=Student()
S1.set_student_id(2000)
S1.set_marks(86)
S1.set_age(21)
S1.set_course_id(1002)
S1.set_fees(15500.0)
print(S1.check_qualification())
S1.choose_course(S1.get_course_id())
S1.validate_marks()
S1.validate_age()



