from Assignment1 import human
class Emp(human) :
    def emply(self):
        desg = input("enter designation")
        exp = input("enter expierence")
        sal = input("enter salary")
        hike =  "10000" if desg.lower()  >= "PM"  else "8000" if desg.lower()  >= "TL" else "5000"
        print("HIkE : ",hike)
        totsal = int(sal)+int(hike)
        print("total salary ",totsal )

obje = Emp()
obje.input()
obje.emply()