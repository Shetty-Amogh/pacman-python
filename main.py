import os

#ᗧ pacman, ᗣ ghost

#------------------- variables-----------------------

map = [
["__","__","__","__","__","__","__","__","__","__","__","__","__","__","__","__"],
["| ","ᗧ ",". ",". ",". ",". ",". ",". ",". ",". ",". ",". ",". ",". ","\u001b[31mᗣ \u001b[0m"," |"],
["| ",". ","| ","__","__","__","__","__",". ",". ",". ",". ",". ",". ",". "," |"],
["| ",". ",". ",". ",". ",". ",". ",". ",". ",". ",". ",". ",". ","__","__"," |"],
["| ",". ","| ","__","__","| ",". ",". ",". ","__","__",". ",". ","| ",". "," |"],
["| ",". ",". ",". ",". ","| ",". ",". ",". ",". "," .",". ","__","| ",". "," |"],
["| ",". ",". ",". ",". ",". ","\u001b[34mᗣ \u001b[0m",". ",". ",". "," .",". ",". ",". ",". "," |"],
["| ","__","__",". ",". ",". ",". ","| ",". ","__",". ",". ",". ",". ",". "," |"],
["| ",". ",". ","__",". ",". ",". ","| ",". ",". ",". ",". ",". ",". ",". "," |"],
["| ",". ",". ",". ","| ",". ",". ","__","| ",". ",". ",". ",". ",". ",". "," |"],
["| ",". ","__",". ","| ","__",". ",". ","__","__","__","__",". ","| ",". "," |"],
["| ",". ","| ",". ",". ",". ",". ",". ",". ",". ",". ",". ",". ","| ",". "," |"],
["| ",". ","| ",". ",". ",". ",". ",". ",". ",". ",". ",". ",". ","| ",". "," |"],
["| ",". ","| ","__","__","__",". ","__","__","__","__",". ",". ","| ",". "," |"],
["| ",". ",". ",". ",". ",". ",". ",". ",". ",". ",". ",". ","| ",". ","\u001b[33mᗣ \u001b[0m"," |"],
["__","__","__","__","__","__","__","__","__","__","__","__","__","__","__","__"]
]

coordX=1
coordY=1
tempX=0
tempY=0
g1X = 14
g1Y = 1
g2X = 14
g2Y = 14
g3X= 6
g3Y= 6
R = 16
counter=0

gameOn = True
gameLost = False
validMove = True
#--------------------- functions----------------------

def printMap():
 os.system("clear")
 print("Score [Moves] : ", end="")
 print(counter)
 for y in range(R): 
  for x in range(R):
   print(map[y][x], end=' ')
  else:
   print(" ")
 else:
   print(" ")  
    
def ghostBrain(Gx, Gy):
  global tempX
  global tempY
  global gameOn
  global gameLost

  distX = coordX - Gx
  distY = coordY - Gy
  if distX == 0 and distY == 0:
    gameLost = True
    gameOn = False
  else:
   if abs(distX) > abs(distY):
     if distY > 0 and map[Gy+1][Gx] != "| " and map[Gy+1][Gx] != "__" and map[Gy+1][Gx] != " |":
       temp = map[Gy+1][Gx] 
       map[Gy+1][Gx] = map[Gy][Gx]
       map[Gy][Gx] = temp
       Gy = Gy + 1
     elif distY <0 and map[Gy-1][Gx] != "| " and map[Gy-1][Gx] != "__" and map[Gy-1][Gx] != " |":
       temp = map[Gy-1][Gx] 
       map[Gy-1][Gx] = map[Gy][Gx]
       map[Gy][Gx] = temp
       Gy = Gy-1
     else:
       if distX >0 and map[Gy][Gx+1] != "| " and map[Gy][Gx+1] != "__" and map[Gy][Gx+1] != " |":
         temp = map[Gy][Gx+1] 
         map[Gy][Gx+1] = map[Gy][Gx]
         map[Gy][Gx] = temp
         Gx = Gx + 1
       elif distX <0 and map[Gy][Gx-1] != "| " and map[Gy][Gx-1] != "__" and map[Gy][Gx-1] != " |":
         temp = map[Gy][Gx-1] 
         map[Gy][Gx-1] = map[Gy][Gx]
         map[Gy][Gx] = temp
         Gx = Gx -1
       elif distX ==0:
        gameOn = False
        gameLost = True
 
   else:
     if distX > 0 and map[Gy][Gx+1] != "| " and map[Gy][Gx+1] != "__" and map[Gy][Gx+1] != " |":
       temp = map[Gy][Gx+1] 
       map[Gy][Gx+1] = map[Gy][Gx]
       map[Gy][Gx] = temp
       Gx = Gx + 1
     elif distX <0 and map[Gy][Gx-1] != "| " and map[Gy][Gx-1] != "__" and map[Gy][Gx-1] != " |":
       temp = map[Gy][Gx-1] 
       map[Gy][Gx-1] = map[Gy][Gx]
       map[Gy][Gx] = temp
       Gx = Gx-1
     else:
       if distY >0 and map[Gy+1][Gx] != "| " and map[Gy+1][Gx] != "__" and map[Gy+1][Gx] != " |":
        temp = map[Gy+1][Gx] 
        map[Gy+1][Gx] = map[Gy][Gx]
        map[Gy][Gx] = temp
        Gy = Gy + 1
       elif distY <0 and map[Gy-1][Gx] != "| " and map[Gy-1][Gx] != "__" and map[Gy-1][Gx] != " |":
        temp = map[Gy-1][Gx] 
        map[Gy-1][Gx] = map[Gy][Gx]
        map[Gy][Gx] = temp
        Gy = Gy -1
       elif distY==0:
        gameOn = False
        gameLost = True
   tempX = Gx
   tempY = Gy

#-------start of code / alsys run when started---------

printMap()

#--------------------- inputs-----------------------

while gameOn == True:
 print("Make your move :", end=" ")
 move = input()

#-------------------- move right -----------------------
 
 if move == 'd' or move == 'D':
  if map[coordY][coordX + 1] == "| " or map[coordY][coordX + 1] == "__" and map[coordY][coordX+1] != " |":
    validMove = False
  elif map[coordY][coordX + 1] == "ᗣ " :
    gameLost=True
    gameOn= False
    break
  else: 
   temp = map[coordY][coordX + 1] 
   map[coordY][coordX + 1] = map[coordY][coordX]
   map[coordY][coordX] = temp
   coordX = coordX + 1
   counter = counter+1
   
#-------------------move left----------------------------
 
 elif move == 'a' or move == 'A':
  if map[coordY][coordX - 1] == "| " or map[coordY][coordX - 1] == "__" and map[coordY][coordX-1] != " |":
    validMove = False
  elif map[coordY][coordX + 1] == "ᗣ " :
    gameLost=True
    gameOn= False
    break
  else: 
   temp = map[coordY][coordX-1]
   map[coordY][coordX-1]= map[coordY][coordX]
   map[coordY][coordX] = temp
   coordX = coordX - 1
   counter = counter+1
   

#-------------------move up----------------------------
 
 elif move == 'w' or move == 'W':
  if map[coordY-1][coordX] == "| " or map[coordY-1][coordX] == "__" and map[coordY-1][coordX] != " |":
   validMove = False
  elif map[coordY][coordX + 1] == "ᗣ " :
    gameLost=True
    gameOn= False
    break
  else: 
   temp = map[coordY-1][coordX]
   map[coordY-1][coordX]= map[coordY][coordX]
   map[coordY][coordX] = temp
   coordY = coordY - 1
   counter = counter+1
   
 

#-------------------move down----------------------------
 
 elif move == 's' or move == 'S':
  if map[coordY+1][coordX] == "| " or map[coordY+1][coordX] == "__" and map[coordY+1][coordX] != " |":
   validMove = False
  elif map[coordY][coordX + 1] == "ᗣ " :
    gameLost=True
    gameOn= False
    break
  else: 
   temp = map[coordY+1][coordX]
   map[coordY+1][coordX]= map[coordY][coordX]
   map[coordY][coordX] = temp
   coordY = coordY + 1
   counter = counter+1
   


#--------------------exit----------------------------------
 
 elif move == 'exit':
  gameOn = False
  os.system("clear")
  break

#--------------------- invalid statement-----------------
 
 else:
  printMap()
  print("invalid input")
  validMove = False
#-------------------------------ghsot and calc------------
 if gameOn == True and gameLost == False:
  #------------------- ghost 1 brain -------------------
  
  ghostBrain(g1X,g1Y)
  if gameLost == True and gameOn == False:
    break
  else:
   print("attacked1")
   g1Y = tempY
   g1X= tempX
  ghostBrain(g2X,g2Y)
  if gameLost == True and gameOn == False:
    break
  else:
   g2Y = tempY
   g2X = tempX
   print("attacked2",tempX,tempY,g2X,g2Y)
  ghostBrain(g3X,g3Y)
  if gameLost == True and gameOn == False:
    break
  else:
   g3Y = tempY
   g3X = tempX
  printMap()
  if validMove == False:
   print("Invalid move")
   validMove = True
  
 else: 
    printMap()
    break
 print(gameOn,gameLost)
 
if gameLost == True:
  printMap()
  print ("Game over")