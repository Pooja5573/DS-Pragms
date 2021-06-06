#ASSIGNMENT : 1
#to find factorial of given num

n = int(input("enter the num"))
fact = 1
while n>=2 :
    fact = fact*n
    n-=1
print("factorial : ",fact)

##ASSIGNMENT : 2
#to find the fibonacci series

n = int(input("enter the num"))
a = 0
b = 1
c = a+b
while c <= n:
    print("THE FIBONACCI series : ",c)
    a=b
    b=c
    c = a+b

#ASSIGNMENT : 3
#to find marks, avg, tot of 5 - students

i = 1

while i <= 5:
    a = input("enter name and five subjects marks:")
    b = a.split()
    print(b)
    print("student name:", b[0])
    j = 1
    sum = 0
    while j<=5 :
        print(int(b[j]))
        sum = sum + int(b[j])
        j = j+1

    print("sum:", sum)
    avg = sum/5
    print("avg : ",avg)
    print("A+" if avg>=90 else "A" if avg<90 and avg>=80 else ("B" if avg<80 and avg>=70 else "C"))
    i = i+1
