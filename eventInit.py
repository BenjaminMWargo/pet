class event:
    def __init__(self,id,mood,description,action,fitness):
        self.id = id
        self.mood = mood
        self.description = description
        self.action = action
        self.fitness = fitness
    def printEvent(self):
        print("ID:"+str(self.id)+"|Mood:"+str(self.mood)+"|"+self.description+"|Fitness:"+str(self.fitness)) 
def testMethod(p):
    p.stats.hp +=10
    p.stats.happiness += -10
    p.stats.sick += 1
    p.log += "Test passed\n"
    p.stats.boundCheck()
def initEvents():
    x = []
    x.append(event(1,2,"This is a test",testMethod,50))
    return x        