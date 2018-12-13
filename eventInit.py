class event:
    def __init__(self,mood,description,action,fitness):
        self.mood = mood
        self.description = description
        self.action = action
        self.fitness = fitness
    def printEvent(self):
        print("|Mood:"+str(self.mood)+"|"+self.description+"|Fitness:"+str(self.fitness)) 
def chaseTailAction(p):
    p.stats.happiness += 10
    p.log += "%s chased it's tale for an hour\n" % p.name
    p.stats.boundCheck()
def napAction(p):
    p.stats.health += 10
    p.log += "%s napped all day\n" % p.name
    p.stats.boundCheck()    
def initEvents():
    x = {0:event(-1,"Chase Tail",chaseTailAction,40),
        1:event(0,"Nap",napAction,30),
        2:event(8,"Chase Tail",chaseTailAction,30)
        
        
        }
    return x        