import eventInit

class pet:
    def __init__(self):
        self.name = ""
        self.stats = stats()
        self.events = eventInit.initEvents()
        self.log = ""
        self.mood = "Normal"
    def printStats(self):
        print("HP = " + str(self.stats.hp) +"\nHappiness = "+str(self.stats.happiness)+"\nHunger = "+str(self.stats.hunger))
        if (self.stats.sick>0):
            print("%s is sick" % self.name)
class stats:
    def __init__(self):
        self.hp = 100       #Range 0 - 100
        self.happiness = 50 #Range 0 to 100
        self.hunger = 0     #Range -50 to 50
        self.sick = 0       #Positive int
        self.age = 0        #Positive int
    
    def boundCheck(self):
        #Keeps stats within their bounds
        if (self.hp >100):
            self.hp = 100
        if(self.happiness > 100):
            self.happiness = 100
        if(self.happiness < 0):
            self.happiness = 0
        if(self.hunger < -50):
            self.hunger = -50
        if(self.hunger > 50):
            self.hunger = 50
#=========INIT===============
moodDict = {
    -1:"All",       #used for events that apply to all
    0:"Normal",     #Not hurt,Not Hungry,Not sad
    1:"Dispair",    #Critical,sad and very hungry/very full
    2:"Miserable",  #Critical,sad and hungry
    3:"Depressed",  #Not Critical, Not happy, Hungry
    4:"Starving",   #Not Critical, Not unhappy, Very Hungry
    5:"Hopeful",
    6:"In-Pain",
    7:"Hungry",
    8:"Energetic"
    9:"Down"
        
        }
#=========MAIN===============
x = pet()
x.name = "Tigger"
x.printStats()
x.events[0].action(x)
x.printStats()
print(x.log)