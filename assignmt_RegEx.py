import re
s = input("enter the EmailId")
m = re.fullmatch("[a-zA-z0-9_.]+[@][a-zA-Z]+[.][a-z]+",s)
if m == None :
    print("enter valid EmailId")
else :
    print("Thank you for entering valid EmailId : ",m)"""

"""s1 = input("enter pancard number")
n = re.fullmatch("[a-zA-Z]{5}[0-9]{4}[a-zA-z]{1}",s1)
if n == None :
    print("enter valid Pan Number")
else:
    print(n)

s2 = input("enter USA number")
p = re.fullmatch("[0-9-()]{12}",s2)
if p == None :
    print("enter the valid number")
else:
    print("number : ",p)