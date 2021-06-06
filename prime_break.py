#find prime num using while break
num = int(input("enter the num"))


i = 1
c = 0
while True:
    if num%i == 0:

        c = c+1
    i = i+1
    break
if (c == 2):
    print("prime")
else:
    print("not prime")

#assignment : 2
#print the "*" in triangle form
"""num = int(input("enter the number"))
i = 1
while i <= num:
    j = 1
    while j <= i:
        print("*",end=" ")
        j = j+1
    print()
    i = i+1"""
