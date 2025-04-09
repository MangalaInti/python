FUNCTION:
A Function is a block code which can be reused, fuction code runs only when function is called. It is optional to pass parameters to the Function.
RETURN VALUES:
The keyword return is used to return back value to the called function. If return keyword is not used in function then it will retrun None

Why use Functions
✔ Reusability – Write once, use anywhere!
✔ Readability – Clean, structured code
✔ Efficiency – Avoid redundancy
---------------------------------------------------------------------------------------------------------------------------------------------
def add(a,b):
    c = a+b # return a+b => 8  otherwise result will give None
result = add(5,3)    
print(result)
----------------------------------------------------------------------------------------------------------------------------------------------
Types of Arguments in Python:

1️⃣ Positional Arguments: Ordered input values
2️⃣ Keyword Arguments: Named parameters for clarity
3️⃣ Default Arguments: Set default values
4️⃣ Variable-Length Arguments (*args, **kwargs): Accept multiple inputs
