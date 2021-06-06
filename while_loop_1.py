#assignment : 1
"""To print the num from 1 to entered num"""

n = int(input("enter the num"))
i = 1
j = 1
while i<=n:
    print(i)
    i = i+1
    
#assignment : 2    
"to print the table"
while j<=10:
    print(n,"x",j,"=",(j*n))
    j = j+1

#assignment : 3
lower = int(input("enter the lower num"))
upper = int(input("enter the upper num"))
i = lower0
while lower*5<=upper:
    print(lower*5)
    lower = lower+1

#assignment : 4

a=input("Enter ten values : ")
b=a.split()
i=0
while i<=9:
    if int(b[i])%2==0:

      print(b[i])
    i=i+1

#assignment : 5

i=1
count=0
sum=0
while i<=100:
      if i%6==0:
            print(i)
            count=count+1
            sum= sum+i
      i=i+1

print("count:",count)
print("sum:",sum)

#assignment : 6

i=1
sum=0
while i<=100:
      if i%9==0:
            print(i)
            sum=sum+i
      i=i+1
print("sum:",sum)

#assignment-7


a=input("enter name and five subjects marks:")
b=a.split()
print(b)
print("student name:",b[0])
i=1
sum= 0
while i<=5:
      print(int(b[i]))
      sum=sum+(int(b[i]))
      i=i+1
print("sum:",sum)
avg=sum/5
print(avg)
print("A+" if avg>=90 else "A" if avg<90 and avg>=80 else ("B" if avg<80 and avg>=70 else C))


#assignment-8

i=1
count=0
sum=0
while i<=100:
      if i%2==1 and i%5==0:
            print(i)
            count=count+1
            sum=sum+i
      i=i+1
print("count:",count)
print("sum:",sum)