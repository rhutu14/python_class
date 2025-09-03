class AI:
    def __init__(self,n,v,o,a):
        self.name=n
        self.version=v
        self.origin=o
        self.accuracy=a
s1=AI("chatgpt","5.o","Open ai","high")
print(s1)
print(type(s1))
print(id(s1))

class laptop:
    def __init__(self,display,RAM,storage,color):
        self.display=display
        self.RAM=RAM
        self.storage=storage
        self.color=color
s2=laptop(15.5,"16GB","512GB","silver")
print(s2)
print(type(s2))
print(id(s2))

class college:
    def __init__(self,a,b,c):
        self.department=a
        self.entrytime=b
        self.location=c
s3=college("maths","10 am","Pune")
print(s3)
print(type(s3))
print(id(s3))

class booking:
    def __init__(self,a,b,c,d):
        self.time=a
        self.seatnumber=b
        self.ticket=c
        self.city=d
s4=booking("10 pm","L18","one","Pune")
print(s4)
print(type(s4))
print(id(s4))

class notebook:
    def __init__(self,a,b,c,d):
        self.size=a
        self.pages=b
        self.type=c
        self.brand=d
s5=notebook("A4",200,"spiral","navneet")
print(s5)
print(type(s5))
print(id(s5))
