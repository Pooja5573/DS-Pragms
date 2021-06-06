#copy
import csv
with open("abc.csv","r") as f1 :
    objr = csv.reader(f1)
    l1 = list(objr)

with open("copy.csv","w",newline="") as f2 :
    objw = csv.writer(f2)
    objw.writerows(l1)

# ******************** merging ******************************
import csv
with open("stu1.csv","w",newline="") as f:
    objw1 = csv.writer(f)
    objw1.writerow(["Rollno","Name"])
    objw1.writerow(["04","MMM"])
    f.seek(0)
with open("stu1.csv","r") as f:
    obj1 = csv.reader(f)
    list1 = []
    for i in obj1:
        list1.append(i)
    print(list1)

import csv
with open("stu2.csv","w",newline="") as f:
    objw1 = csv.writer(f)
    objw1.writerow(["Rollno","Name"])
    objw1.writerow(["05","NNN"])
    f.seek(0)
with open("stu2.csv","r") as f:
    obj1 = csv.reader(f)
    list2 = []
    for i in obj1:
        list2.append(i)
    print(list2)

import csv
with open("stu3.csv","w",newline="") as f:
    obj2 = csv.writer(f)
    obj2.writerow(["Rollno","Name"])
    obj2.writerow(["06","OOO"])
    f.seek(0)
with open("stu3.csv","r") as f:
    objr = csv.reader(f)
    list3 = []
    for i in objr:
        list3.append(i)
    print(list3)

with open("stu.csv","w+",newline="") as f1:
    objw = csv.writer(f1)
    objw.writerows(list1)
    objw.writerows(list2)
    objw.writerows(list3)
    #f.seek(0)
    objr = csv.reader(f1)
    list4 = []
    for i in objr:
        list4.append(i)
        print(list4)

#*************  Appending the student details **************************
import csv
f1 = open("abc.csv","w")
objw = csv.writer(f1)
objw.writerow(["Rollno","Name","M1","M2","M3"])

while True :
    Rollno = input("Enter student Rollno ")
    Name = input("Enter student Name")
    M1 = int(input("Enter marks1"))
    M2 = int(input("Enter marks2"))
    M3 = int(input("Enter marks3"))
    objw.writerow([Rollno,Name,M1,M2,M3])
    ch = input("Do you want to continue " )
    if ch.lower != "yes":
        break

import csv
with open("abc.csv","r") as f:
    objr = csv.reader(f)
    list1 = []
    for i in objr:
        list1.append(i)
    print(list1)
    list2= []
    for i in list1:
        if i[0] == "Rollno":
            i.append("Tot")
            i.append("Avg")
            i.append("Grade")
            list2.append(i)
        else:
            tot = int(i[2])+int(i[3])+int(i[4])
            i.append(tot)
            print(tot)
            avg = tot/3
            i.append(avg)
            print(avg)
            grade = "A+"    if avg>=90  else "B+" if (avg>75 and avg<50) else "C"
            i.append(grade)
            print(grade)
            list2.append(i)
        print(list2)

import csv
with open("stu_append.csv","w+",newline="") as f:
    objw=csv.writer(f)
    objw.writerows(list2)
    f.seek(0)
    objr=csv.reader(f)
    for i in objr:
        print(i)