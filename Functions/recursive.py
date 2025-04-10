Recursive Function : A function calls by itself is called recursive
#This is a recursive function. It calculates the sum of all numbers from 1 to num.

def sum(num):
    if 1 == num:
       return 1
    else:
        return num + sum(num -1) #sum(num-1) is called again and again 5+4+3+2 => 15
print(sum(5))   

#How does recursion work here?
Let's see how sum(5) gets evaluated:

sum(5) → 5 + sum(4)

sum(4) → 4 + sum(3)

sum(3) → 3 + sum(2)

sum(2) → 2 + sum(1)

sum(1) → returns 1 (base case)

Now plug values back in:

sum(2) = 2 + 1 = 3

sum(3) = 3 + 3 = 6

sum(4) = 4 + 6 = 10

sum(5) = 5 + 10 = 15

✅ Output:
15
In Simple Words:
This function adds:


5 + 4 + 3 + 2 + 1 = 15
