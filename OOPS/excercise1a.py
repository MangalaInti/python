Implement the Customer class based on the identified class structure and details given below:

    1. Consider all instance variables and methods to be public
    2. Assume that bill_amount is initialized with total bill amount of the customer
    3. Customer is eligible for 5% discount on the bill amount
    4. purchases(): Compute discounted bill amount and pay bill
    5. pays_bill(amount): Display, <customer_name> pays bill amount of Rs. <amount>

Represent few customers, invoke purchases() method and display the details.

class customer:
    def __init__(self,customer_name,bill_amount):
        self.customer_name = customer_name
        self.bill_amount = bill_amount

    def purchases(self):
        self.total_bill_amount = self.bill_amount * 0.5
        return self.total_bill_amount
    def pay_bill(self,amount):
        print(self.customer_name,"have to pay", self.total_bill_amount)

c1 = customer("Rahul", 20000)
c2 = customer("Suraj", 50000)
c3 = customer("Kanak", 80000)            
c1.purchases()
c1.pay_bill(2000)
