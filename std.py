from Assignment1 import human
class student(human) :
    def stu(self):
        cls = input("enter class of the student")
        eng = input("enter english marks")
        sci = input("enter science marks")
        mat = input("enter maths marks")
        tot = int(eng)+int(sci)+int(mat)
        print("Total : ",tot)
        avg = tot/3
        a = "A+" if avg >= 80 else "A" if avg >= 60 else "C"
        print("grade", a)

objs = student()
objs.input()
objs.stu()