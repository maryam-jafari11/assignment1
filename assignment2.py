sid1 = int(input("Enter sid1: "))
sid2 = int(input("Enter sid2: "))
sid3 = int(input("Enter sid3: "))


check1 = sid2 + sid3
if check1 >= sid1:
    result = "These three sides can be a triangle"
else:
    result = "These three sides can not be a triangle"


check2 = sid1 + sid3
if check2 >= sid2:
    result = "These three sides can be a triangle"
else:
    result = "These three sides can not be a triangle"

check3 = sid1 + sid2
if check3 >= sid3:
     result = "These three sides can be a triangle"
else:
    result = "These three sides can not be a triangle"

        

print(result)