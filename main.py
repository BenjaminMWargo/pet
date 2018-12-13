import eventInit
import platform, re, os, random
from fuzzy import *

class pet:
    def __init__(self):
        self.name = ""
        self.stats = stats()
        self.events = eventInit.initEvents()
        self.log = ""
        self.mood = 0
        self.prevEvent = None
    def printStats(self):
        print("Age = " + str(self.stats.age) + "\nHP = " + str(self.stats.hp) +"\nHappiness = "+str(self.stats.happiness)+"\nHunger = "+str(self.stats.hunger)+"\nMood:"+str(moodDict[self.mood]))
        if (self.stats.sick>4):
            print("%s is very sick" % self.name)
        elif (self.stats.sick>1):
            print("%s is sick" % self.name)
        if (self.stats.sick>0):
            print("%s is slightly sick" % self.name)
    def setName(self,n):
        self.name = n
    def updateMood(self):
        #Health Check
        if (mFuzzyCheck(mIsCritical(self))):
            
            #Happiness Check
            #Is Sad
            if (mFuzzyCheck(mIsSad(self))):               
                if (mFuzzyCheck(mIsVeryHungry(self))):
                    self.mood = 1
                elif(mFuzzyCheck(mIsHungry(self))):
                    self.mood = 2
                elif(mFuzzyCheck(mIsNormalHunger(self))):
                    self.mood = 3
                elif(mFuzzyCheck(mIsFull(self))):
                    self.mood = 3
                elif(mFuzzyCheck(mIsVeryFull(self))):
                    self.mood = 4
            #Is Indifferent
            elif(mFuzzyCheck(mIsIndifferent(self))):
                if (mFuzzyCheck(mIsVeryHungry(self))):
                    self.mood = 2
                elif(mFuzzyCheck(mIsHungry(self))):
                    self.mood = 2
                elif(mFuzzyCheck(mIsNormalHunger(self))):
                    self.mood = 3
                elif(mFuzzyCheck(mIsFull(self))):
                    self.mood = 3
                elif(mFuzzyCheck(mIsVeryFull(self))):
                    self.mood = 2
            #Is Happy
            elif(mFuzzyCheck(mIsHappy(self))):
                if (mFuzzyCheck(mIsVeryHungry(self))):
                    self.mood = 4
                elif(mFuzzyCheck(mIsHungry(self))):
                    self.mood = 6
                elif(mFuzzyCheck(mIsNormalHunger(self))):
                    self.mood = 6
                elif(mFuzzyCheck(mIsFull(self))):
                    self.mood = 5
                elif(mFuzzyCheck(mIsVeryFull(self))):
                    self.mood = 6

        elif(mFuzzyCheck(mIsHurt(self))):
            
             #Happiness Check
             #Is Sad
            if (mFuzzyCheck(mIsSad(self))):
                if (mFuzzyCheck(mIsVeryHungry(self))):
                    self.mood = 2
                elif(mFuzzyCheck(mIsHungry(self))):
                    self.mood = 9
                elif(mFuzzyCheck(mIsNormalHunger(self))):
                    self.mood = 3
                elif(mFuzzyCheck(mIsFull(self))):
                    self.mood = 3
                elif(mFuzzyCheck(mIsVeryFull(self))):
                    self.mood = 10
            #Is Indifferent
            elif(mFuzzyCheck(mIsIndifferent(self))):
                if (mFuzzyCheck(mIsVeryHungry(self))):
                    self.mood = 4
                elif(mFuzzyCheck(mIsHungry(self))):
                    self.mood = 9
                elif(mFuzzyCheck(mIsNormalHunger(self))):
                    self.mood = 0
                elif(mFuzzyCheck(mIsFull(self))):
                    self.mood = 5
                elif(mFuzzyCheck(mIsVeryFull(self))):
                    self.mood = 10
            #Is Happy
            elif(mFuzzyCheck(mIsHappy(self))):
                if (mFuzzyCheck(mIsVeryHungry(self))):
                    self.mood = 5
                elif(mFuzzyCheck(mIsHungry(self))):
                    self.mood = 0
                elif(mFuzzyCheck(mIsNormalHunger(self))):
                    self.mood = 0
                elif(mFuzzyCheck(mIsFull(self))):
                    self.mood = 5
                elif(mFuzzyCheck(mIsVeryFull(self))):
                    self.mood = 10

        elif(mFuzzyCheck(mIsHealthy(self))):
            
             #Happiness Check
             #Is Sad
            if (mFuzzyCheck(mIsSad(self))):
                if (mFuzzyCheck(mIsVeryHungry(self))):
                    self.mood = 4
                elif(mFuzzyCheck(mIsHungry(self))):
                    self.mood = 9
                elif(mFuzzyCheck(mIsNormalHunger(self))):
                    self.mood = 3
                elif(mFuzzyCheck(mIsFull(self))):
                    self.mood = 3
                elif(mFuzzyCheck(mIsVeryFull(self))):
                    self.mood = 10
            #Is Indifferent
            elif(mFuzzyCheck(mIsIndifferent(self))):
                if (mFuzzyCheck(mIsVeryHungry(self))):
                    self.mood = 4
                elif(mFuzzyCheck(mIsHungry(self))):
                    self.mood = 0
                elif(mFuzzyCheck(mIsNormalHunger(self))):
                    self.mood = 0
                elif(mFuzzyCheck(mIsFull(self))):
                    self.mood = 8
                elif(mFuzzyCheck(mIsVeryFull(self))):
                    self.mood = 8
            #Is Happy
            elif(mFuzzyCheck(mIsHappy(self))):
                if (mFuzzyCheck(mIsVeryHungry(self))):
                    self.mood = 5
                elif(mFuzzyCheck(mIsHungry(self))):
                    self.mood = 0
                elif(mFuzzyCheck(mIsNormalHunger(self))):
                    self.mood = 8
                elif(mFuzzyCheck(mIsFull(self))):
                    self.mood = 8
                elif(mFuzzyCheck(mIsVeryFull(self))):
                    self.mood = 10
        else:
            x.mood = 0
    def upkeep(self):
        if(mFuzzyCheck(mIsVeryHungry(self))):
            #Take damage and lose happiness if starving
            self.stats.hp -=10
            self.stats.happiness -=10
        elif(self.stats.sick>0):
            #Don't heal and happiness lowers if sick
            self.stats.happiness -=10
            self.stats.sick -=1
        else:
            self.stats.hp += 10
            self.stats.sick= 0
        self.stats.age+= 1
        self.stats.hunger -=10
        self.stats.boundCheck()
    def isPetDead(self):
        return (True if (self.stats.hp <= 0) else False)
    def condition(self,i):
        if ((i =="h") or (mFuzzyCheck(mIsVeryHungry(self)) and i=="n") or (mFuzzyCheck(mIsVeryFull(self) and i=="f"))):
            #hit punishment.Also happens for ignoring a starving pet or feeding an extremely full pet
            self.events[self.prevEvent].fitness = self.events[self.prevEvent].fitness * .5
        elif ((i=="s") or (mFuzzyCheck(mIsHungry(self)) and i=="n")):
            #scold punishment, or ignoring a slightly hungry pet
            self.events[self.prevEvent].fitness = self.events[self.prevEvent].fitness * .75
        elif (i=="f"):
            self.events[self.prevEvent].fitness = self.events[self.prevEvent].fitness * 1.25
        elif ((i=="p") and self.mood ==10):
            pass
        elif ((i=="p")):
            self.events[self.prevEvent].fitness = self.events[self.prevEvent].fitness * 1.25
        #Prevent negative fitness
        if (self.events[self.prevEvent].fitness <= 5):
            self.events[self.prevEvent].fitness = 5
        if (self.events[self.prevEvent].fitness >= 95):
            self.events[self.prevEvent].fitness = 95
        
    def inputAction(self,i):
        if ((i =="h") or (mFuzzyCheck(mIsVeryHungry(self)) and i=="n") or (mFuzzyCheck(mIsVeryFull(self) and i=="f"))):
            #hit punishment.Also happens for ignoring a starving pet or feeding an extremely full pet
            self.stats.hp -=20
            self.stats.happiness -=40
        elif ((i=="s") or (mFuzzyCheck(mIsHungry(self)) and i=="n")):
            #scold punishment, or ignoring a slightly hungry pet
            self.stats.happiness -=20
        elif ((i=="f")):
            self.stats.hunger +=50
            self.stats.happiness +=10
        elif ((i=="p") and self.mood ==10):
            #Won't play if sleepy
            self.log += "%s is too tired to play\n" % self.name
            pass
        elif ((i=="p")):
            self.stats.happiness +=20
    def eventSelection(self):
        #Get a list of eventIDs that match the current mood
        matchedEvents = {}
        for a in self.events:
            if (self.events[a].mood == x.mood) or (self.events[a].mood == -1):
                matchedEvents[a]=self.events[a].fitness
                self.events[a].printEvent()
        #Fitness proportional
        max = sum(matchedEvents.values())
        pick = random.uniform(0,max)
        current = 0
        for key,value in matchedEvents.items():
            current += value
            if current > pick:
                self.prevEvent = key
                print(key)
                return

class stats:
    def __init__(self):
        self.hp = 100       #Range 0 - 100
        self.happiness = 50 #Range 0 to 100
        self.hunger = 0     #Range -100 to 100
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
        if(self.hunger < -100):
            self.hunger = -100
        if(self.hunger > 100):
            self.hunger = 100
def initPet():
    x = pet()
    x.setName(input("Enter a name for your pet:"))
    return x
def clear():
    if (platform.system() == "Windows"):
        os.system('cls')
    else:
        os.system('clear')
#=========INIT===============
moodDict = {
    -1:"All",       #used for events that apply to all
    0:"Normal",     #Not hurt,Not Hungry,Not sad
    1:"Dispair",    #Critical,sad and very hungry/very full
    2:"Miserable",  #Critical,sad and hungry
    3:"Depressed",  #Not Critical, Not happy, Hungry
    4:"Starving",   #Not Critical, Not unhappy, Very Hungry
    5:"Hopeful",
    6:"Uncomfortable",
    7:"Hungry",
    8:"Energetic",
    9:"Down",
    10:"Sleepy"}
regex = re.compile('(^\w)*([hsnfp])(?!\w)')
#=========MAIN===============
x = initPet()
clear()
x.printStats()
print("=================================")
while (not x.isPetDead()):
    y = input("Enter an action (H:Hit,S:Scold,N:Nothing ,F:Feed ,P:Play):").lower()
    while not regex.match(y):
        print("Bad input, try again")
        y = input("Enter an action (H:Hit,S:Scold,N:Nothing ,F:Feed ,P:Play):").lower()
    #clear()
    #Get user action
    #Influence previous events based on action
    x.log = ""
    if not (x.prevEvent == None):
        x.condition(y)
    #Adjust stats based on action
    x.inputAction(y)
    #Upkeep
    x.upkeep()
    #update mood
    x.updateMood()
    #Find next event based on stats
    x.eventSelection()
    #Do event

    #Update stats based on event

    #Update mood based on new stats

    #Print out stats
    x.printStats()
    #Print out log
    print("=================================")
    print(x.log)
    print("=================================")
#========
#Pet died
print("=================================")
print("%s has died at age %i and felt %s at death." % (x.name,x.stats.age,moodDict[x.mood].lower()))    
input("Press any key to quit")    