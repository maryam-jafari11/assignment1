op = input("please select your operation(+ , - , * , / , sin , cos , tan , cot , ! , sqrt ): ")



import math

if op == "+":
    num1 = int(input("enter num1: "))
    num2 = int(input("enter num2: "))
    result = num1 + num2

if op == "-":
    num1 = int(input("enter num1: "))
    num2 = int(input("enter num2: "))
    result = num1 - num2

if op == "*":
    num1 = int(input("enter num1: "))
    num2 = int(input("enter num2: "))
    result = num1 * num2

if op == "/":
    num1 = int(input("enter num1: "))
    num2 = int(input("enter num2: "))
    if num2 == 0:
        result = "undefined"
    else:
        result = num1 / num2
        

if op == "sin":
    num1 = int(input("enter your number: "))
    result = math.sin(num1)


if op == "cos":
    num1 = int(input("enter your number: "))
    result = math.cos(num1)
 
if op == "tan":
    num1 = int(input("enter your number: "))
    result = math.tan(num1)

if op == "cot":
    num1 = int(input("enter your number: "))
    x = math.tan(num1)

    if x == 0:
        result = "undefined"
    else:
        result = 1 / math.tan(num1)

if op == "!":
    num1 = int(input("enter your number: "))
    result = math.factorial(num1) 

if op == "sqrt":
   num1 = int(input("enter your number: ")) 
   result = math.sqrt(num1) 



print(result)                  

