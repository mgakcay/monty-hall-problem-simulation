import random


doYouWantToChanceYourDoor = True
howManyGames = 250


class Door():
    
    def __init__(self,goat=True,selected=False):
        self.goat = goat      
        self.selected = selected
        

    def returnInside(self):
        if(self.goat == True):
            text = "goat"
        else:
            text = "car"
            
        return text        
        
    def __repr__(self):
        return self.returnInside()
        
    def __str__(self):
        return self.returnInside()
        
   


def playAGame(doYouWantToChanceYourDoor):
    
    #Create 3 doors
    doors = []
    indexOftheDoorWithCar = random.randint(0,2)
    
    for j in range(0,3):
        
        goat = True
        if (j == indexOftheDoorWithCar):
            goat = False
            
        doors.append(Door(goat))
        
        
    #Choice a door
    indexOfYourFirstChoice = random.randint(0,2)
    doors[indexOfYourFirstChoice].selected = True
    
    
    #Remove a door
    for j in range(0,3):
        
        if (doors[j].goat == True and doors[j].selected == False ):
            doors.pop(j)
            break
        
        
    
    
    #Chance or not chance your door
    indexOfYourDoor = 0    
    
    if (doYouWantToChanceYourDoor == True):
        #Chance your door
        for j in range(0,2):
            
            if(doors[j].selected == True):
                doors[j].selected == False
            else:
                doors[j].selected == True
                indexOfYourDoor = j
    else:
        #Do not chance your door
        for j in range(0,2):
            if(doors[j].selected == True):
               indexOfYourDoor = j
            
            
                
          
    #Open your door  
    yourReward = ""

    if (doors[indexOfYourDoor].goat == False):
        yourReward = "car"
    else:  
        yourReward = "goat"
        
    return yourReward
   

    
def startSimulation(howManyIteration,doYouWantToChanceYourDoor):
        
    listOfItemsYouWon = []
    for i in range(0,howManyIteration):
        rewardItem = playAGame(doYouWantToChanceYourDoor)
        listOfItemsYouWon.append(rewardItem)
        
        
        print("-> Game: "  +  str(i+1))
        print("-> Reward: "  + rewardItem)

        print("------------")
    return listOfItemsYouWon



def analyzeSimulationResults(listOfItemsYouWon):
    
    print("********* RESULTS *********")
    print("A total of " + str(howManyGames) + " games were played in this simulation.")
    
    countOfGoat = 0
    countOfCar = 0
    
    for item in listOfItemsYouWon:
        if (item == "goat"):
            countOfGoat += 1
        else:
            countOfCar += 1
    
    print("*******")
    print("simulation won " + str(countOfGoat) + " goats in total")
    print("simulation won " + str(countOfCar) + " cars in total")
    print("*******")
            

    print("Goat win rate: " + str((countOfGoat/howManyGames)) )
    print("Car win rate: " + str((countOfCar/howManyGames)) )

    

        
listOfItemsYouWon = startSimulation(howManyGames,doYouWantToChanceYourDoor)
analyzeSimulationResults(listOfItemsYouWon)    

    
    
    
    
    
    