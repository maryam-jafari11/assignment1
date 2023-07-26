name = input("enter your name: ")
lastname = input("enter your last name: ")
score1 = int(input("enter your score1 score: "))
score2 = int(input("enter your score2 score: "))
score3 = int(input("enter your score3 score: "))


avg = (score1 + score2 + score3) / 3

if avg >=17:
    result = "greate"

if 12 <= avg < 17:
    result = "normal"

if avg < 12:
    result = "fail"      


print(result)
