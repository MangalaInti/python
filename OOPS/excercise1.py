WeCare insurance company wants to calculate premium for vehicles.
Vehicles are of two types – "Two Wheelers" and "Four Wheelers". Each vehicle is identified by vehicle id, type, cost, 
and premium amount.
Premium amount is 2% of the vehicle cost for a two wheeler and 6% for four wheeler. 
Calculate the premium amount and display the vehicle details.
Write a Python program to implement the class chosen with its attributes and methods.
Note:
Display appropriate error message, if the vehicle type is invalid
Perform case sensitive string comparison

                                                                                                        
                                                                                                       
  
  class vechile:
   def __init__(self,id,vechile_type,cost):
       self.id = id
       self.vechile_type = vechile_type
       self.cost = cost
       self.premium_amt = None

   def premium(self):
       if self.vechile_type == 'Two Wheeler':
           self.premium_amt = self.cost * 0.2
       elif self.vechile_type == 'Four Wheeler':
           self.premium_amt = self.cost * 0.6
       else:
           print('Invalid Vechile Type')    

   def display_vechile(self):
       print(f'id:{self.id} Vechile_Type: {self.vechile_type} cost: {self.cost} Premium: {self.premium_amt}')

v1 = vechile(1001,'Two Wheeler',5000)
v1.premium()
v1.display_vechile()





