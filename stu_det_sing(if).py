s1 = str(input("name,m1,m2,m3,attendence"))
print(s1)
s = s1.split()
avg = (int(s[1])+int(s[2])+int(s[3]))/3
print("average",avg)
att = int(s[4])
print("attendence : ",att)
"""average"""
a = "A+" if avg >= 80 else "A" if avg >= 60 else "C"
print("grade",a)
"""attedence"""
print(att+2,avg+2) if att>=85 else print(att+1,avg+1) if (att >= 60 and att <80) else print(avg,att)
