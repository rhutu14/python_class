class Player:
    def __init__(self,jn,n,r,w,tname):
        self.jerseynumber=jn
        self.name=n
        self.runs=r
        self.wickets=w
        self.teamname=tname


    def setName(self,nn):
        self.name=nn

    def setJerseynumber(self,njn):
        self.jerseynumber=njn


    def setWickets(self,nw):
        self.wickets=nw

    def setRuns(self,nr):
        self.runs=nr

    def setTeamname(self,ntn):
        self.teamname=ntn


    def getName(self):
        return self.name
    
    def getJerseynumber(self):
        return self.jerseynumber
    
    def getRuns(self):
        return self.runs
    
    def getWickets(self):
        return self.wickets
    
    def getTeamname(self):
        return self.teamname

s1=Player(7,"Dhoni",100,5,"Chennia")

print(s1.name)
s1.setName("Mahendra Singh Dhoni")
print(s1.name)

print(s1.jerseynumber)
s1.setJerseynumber("07")
print(s1.jerseynumber)

print(s1.wickets)
s1.setWickets(10)
print(s1.wickets)


print(s1.runs)
s1.setRuns(200)
print(s1.runs)

print(s1.teamname)
s1.setTeamname("Chennai Super King")
print(s1.teamname)


print(s1.getName())

print(s1.getJerseynumber())

print(s1.getRuns())

print(s1.getWickets())

print(s1.getTeamname())


