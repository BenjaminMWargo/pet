import eventInit
import platform, re, os
from fuzzy import *

class pet:
    def __init__(self):
        self.name = ""
        self.stats = stats()
        self.events = eventInit.initEvents()
        self.log = ""
        self.mood = 0
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
                    self.mood = 1
                elif(mFuzzyCheck(mIsFull(self))):
                    self.mood = 5
                elif(mFuzzyCheck(mIsVeryFull(self))):
                    self.mood = 10
            #Is Happy
            elif(mFuzzyCheck(mIsHappy(self))):
                if (mFuzzyCheck(mIsVeryHungry(self))):
                    self.mood = 5
                elif(mFuzzyCheck(mIsHungry(self))):
                    self.mood = 1
                elif(mFuzzyCheck(mIsNormalHunger(self))):
                    self.mood = 1
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
                    self.mood = 1
                elif(mFuzzyCheck(mIsNormalHunger(self))):
                    self.mood = 1
                elif(mFuzzyCheck(mIsFull(self))):
                    self.mood = 8
                elif(mFuzzyCheck(mIsVeryFull(self))):
                    self.mood = 8
            #Is Happy
            elif(mFuzzyCheck(mIsHappy(self))):
                if (mFuzzyCheck(mIsVeryHungry(self))):
                    self.mood = 5
                elif(mFuzzyCheck(mIsHungry(self))):
                    self.mood = 1
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
        self.stats.age+= 1
        self.log = ""
        self.stats.boundCheck()
    def isPetDead(self):
        return (True if (self.stats.hp <= 0) else False)
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
    clear()
    #Get user action
    x.stats.hp -= 10
    #Influence events based on action

    #Adjust stats based on action
    x.stats.age += 1
    #Upkeep

    #Find next event based on stats

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