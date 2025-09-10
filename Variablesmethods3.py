class Notebook:
    cname="Workbook"   # class variable
    def __init__(self,a,b,c):    #local variables
        self.size=a      #instance variables
        self.pages=b
        self.brand=c

    def setSize(self,ns):    #instance methods
        self.size=ns


    def getPages(self):
        return self.pages
    
    @classmethod               #class method
    def getCname(cls):
        return cls.cname
    
    @staticmethod              ##static method for local variables
    def multiply(old,new):
        book=old+new
        return book
        

s1=Notebook("A4",200,"navneet")

Notebook.getCname()
print(Notebook.getCname())

s1.setSize("A5")
print(s1.size)

Notebook.cname="Handbook"    ###class name is preffered always
print(Notebook.cname)

print(Notebook.multiply(200,100))

