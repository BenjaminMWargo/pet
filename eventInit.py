import random
class event:
    def __init__(self,mood,description,action,fitness):
        self.mood = mood
        self.description = description
        self.action = action
        self.fitness = fitness
    def printEvent(self):
        print("|Mood:"+str(self.mood)+"|"+self.description+"|Fitness:"+str(self.fitness)) 
def eventCounter():
    x = 0
    while True:
        yield x
        x += 1
def chaseTailAction(p):
    p.stats.happiness += 10
    p.stats.hunger -=10
    p.log += "%s chased it's tail for an hour.\n" % p.name
    p.stats.boundCheck()
def napAction(p):
    p.stats.hp += 5
    p.log += "%s napped all day.\n" % p.name
    p.stats.boundCheck()
def biteAction(p):
    p.stats.happiness-=10
    p.log += "%s bit your arm.\n" % p.name
    p.stats.boundCheck()
def throwUpAction(p):
    p.stats.hp -= 10
    p.stats.sick += 2
    p.log += "%s threw up on your bed.\n" % p.name
    p.stats.boundCheck()
def playOutsideAction(p):
    p.log += "%s played outside all day.\n" % p.name
    pick = random.uniform(0,100)
    if (pick>95):
        p.log += "It rained while %s played.\n" % p.name
        p.log += "%s was struck by lightning!\n" % p.name
        p.stats.hp -= 80
        p.stats.happiness -=50
    elif (pick>75):
        p.log += "It rained while %s played.\n" % p.name
        p.log += "%s got sick from the rain\n" % p.name
        p.stats.sick += 5
        p.stats.happiness +=10
    else: 
        p.stats.happiness +=40
    p.stats.hunger -= 10
def cuddleAction(p):
    p.log += "%s cuddles up next to you.\n" % p.name
    p.stats.happiness +=10
    p.stats.hp +=10
def unmotivatedAction(p):
    p.log += "%s is too unmotivated to do anything else.\n" % p.name
def fightAction(p):
    p.log += "%s got in a fight with other pets.\n" % p.name
    pick = random.uniform(0,100)
    if pick> 50:
        p.log += "%s got badly hurt in the fight.\n" % p.name
        p.stats.hp -=40
    else:
        p.log += "%s seems mostly unharmed.\n" % p.name
        p.stats.hp -=10
    p.stats.hunger -= 10
def playInTrafficAction(p):
    p.log += "%s played in on-comming traffic.\n" % p.name
    pick = random.uniform(0,100)
    if (pick>75):
        p.log += "%s was hit by a car!\n" % p.name
        p.stats.hp -= 50
    else:
        p.log += "%s didn't get hurt but liked it a lot.\n" % p.name
        p.stats.happiness =+50
    p.stats.hunger -= 10

def initEvents():
    gen = eventCounter()
    
    x = {next(gen):event(-1,"Chase Tail",chaseTailAction,20),
        next(gen):event(-1,"Nap",napAction,30),
        next(gen):event(-1,"Bites",biteAction,5),
        next(gen):event(-1,"Throw up",throwUpAction,5),
        next(gen):event(0,"Nap",napAction,30),
        next(gen):event(0,"Playoutside",playOutsideAction,20),
        next(gen):event(0,"Cuddle",cuddleAction,20),
        next(gen):event(1,"Unmotivated",unmotivatedAction,50),
        next(gen):event(1,"Bites",biteAction,80),
        next(gen):event(2,"Unmotivated",unmotivatedAction,70),
        next(gen):event(2,"Bites",biteAction,40),
        next(gen):event(3,"Nap",napAction,60),
        next(gen):event(3,"Unmotivated",unmotivatedAction,50),
        next(gen):event(3,"Bites",biteAction,30),
        next(gen):event(4,"Fight",fightAction,75),
        next(gen):event(4,"Unmotivated",unmotivatedAction,40),
        next(gen):event(4,"Bites",biteAction,80),
        next(gen):event(5,"Playoutside",playOutsideAction,20),
        next(gen):event(5,"Cuddle",cuddleAction,40),
        next(gen):event(6,"Throwup",throwUpAction,15),
        next(gen):event(6,"Cuddle",cuddleAction,20),
        next(gen):event(7,"Bites",biteAction,80),
        next(gen):event(7,"Fight",fightAction,50),
        next(gen):event(8,"Playoutside",playOutsideAction,80),
        next(gen):event(8,"Cuddle",cuddleAction,50),
        next(gen):event(8,"Chase Tail",chaseTailAction,30),
        next(gen):event(8,"Play in Traffic",playInTrafficAction,20),
        next(gen):event(9,"Nap",napAction,60),
        next(gen):event(9,"Unmotivated",unmotivatedAction,50),
        next(gen):event(10,"Nap",napAction,80),
        next(gen):event(10,"Unmotivated",unmotivatedAction,20),
        next(gen):event(10,"Throwup",throwUpAction,30),
        next(gen):event(10,"Cuddle",cuddleAction,30)


        }
    return x        