s = input("enter name of the student and marks of three subjects")
print(s)
s1 = s.split()
print("name of the student is : ",s1[0])
print("marks1",s1[1])
print("marks2",s1[2])
print("marks3",s1[3])
avg = (int(s1[1])+int(s1[2])+int(s1[3]))/3
print("average marks : ",avg)
if avg>80 :
    print("grade : A+")
elif avg>60 :
    print("grade : A")
elif avg>50 :
    print("grade : B")
else :
    print("grade : C")
tot = int(s1[1])+int(s1[2])+int(s1[3])
print("Total marks scored : ",tot)