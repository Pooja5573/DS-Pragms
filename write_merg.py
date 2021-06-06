"""merging of three files"""

with open("xyz2.txt","r+") as f1:
    d3 = f1.read()
    f1.write(d3)
    print(d3)

with open("xyz.txt","r+") as f2:
    d1 = f2.read()
    f2.write(d1)
    print(d1)

with open("xyz1.txt","r+") as f3:
    d2 = f3.read()
    f3.write(d2)
    print(d2)

"""replacing"""
with open("abc.txt","r+") as f4:
    d = f4.read()
    print(d)
    f4.write("i love java")

    s1 = d.split( )
    print(s1)
    s2 = s1[2].replace('java','python')
    print(s2)