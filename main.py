import eventInit

class pet:
    def __init__(self):
        self.name = ""
        self.stats = stats()
        self.events = eventInit.initEvents()
        self.log = ""
        self.mood = "Normal"
class stats:
    def __init__(self):
        self.hp = 100       #Range 0 - 100
        self.happiness = 50 #Range 0 to 100
        self.hunger = 0     #Range -50 to 50
        self.sick = 0       #Positive int
        self.age = 0        #Positive int
    def printStats(self):
        print("HP = " + str(self.hp) +"\nHappiness = "+str(self.happiness)+"\nHunger = "+str(self.hunger))
        if (self.sick>0):
        print("Your pet is sick")
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
x = pet()
x.stats.printStats()
x.events[0].action(x)
x.stats.printStats()
print(x.log)