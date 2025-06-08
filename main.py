import os

#ᗧ pacman, ᗣ ghost

#------------------- variables-----------------------

map = [
["__","__","__","__","__","__","__","__","__","__","__","__","__","__","__","__"],
["| ","ᗧ ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","| "],
["| ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","| "],
["| ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","| "],
["| ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","| "],
["| ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","| "],
["| ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","| "],
["| ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","| "],
["| ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","| "],
["| ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","| "],
["| ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","| "],
["| ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","| "],
["| ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","| "],
["| ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","| "],
["| ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","| "],
["__","__","__","__","__","__","__","__","__","__","__","__","__","__","__","__"]
]

coordX=1
coordY=1
R = 16

gameOn = True

#--------------------- functions----------------------

def printMap():
 os.system("clear")
 for y in range(R): 
  for x in range(R):
   print(map[y][x], end=' ')
  else:
   print(" ")
 else:
   print(" ")  

#-------start of code / alsys run when started---------

printMap()

#--------------------- inputs-----------------------

while gameOn == True:
 print("Make your move :", end=" ")
 move = input()

#-------------------- move right -----------------------
 
 if move == 'd' or move == 'D':
  if map[coordY][coordX + 1] == "| " or map[coordY][coordX + 1] == "__":
    printMap()
  else: 
   temp = map[coordY][coordX + 1] 
   map[coordY][coordX + 1] = map[coordY][coordX]
   map[coordY][coordX] = temp
   coordX = coordX + 1
   printMap()
#-------------------move left----------------------------
 
 elif move == 'a' or move == 'A':
  if map[coordY][coordX - 1] == "| " or map[coordY][coordX - 1] == "__":
    printMap(); 
  else: 
   temp = map[coordY][coordX-1]
   map[coordY][coordX-1]= map[coordY][coordX]
   map[coordY][coordX] = temp
   coordX = coordX - 1
   printMap()

#-------------------move up----------------------------
 
 elif move == 'w' or move == 'W':
  if map[coordY-1][coordX] == "| " or map[coordY-1][coordX] == "__":
   printMap()
  else: 
   temp = map[coordY-1][coordX]
   map[coordY-1][coordX]= map[coordY][coordX]
   map[coordY][coordX] = temp
   coordY = coordY - 1
   printMap() 
 

#-------------------move down----------------------------
 
 elif move == 's' or move == 'S':
  if map[coordY+1][coordX] == "| " or map[coordY+1][coordX] == "__":
   printMap()
  else: 
   temp = map[coordY+1][coordX]
   map[coordY+1][coordX]= map[coordY][coordX]
   map[coordY][coordX] = temp
   coordY = coordY + 1
   printMap()


#--------------------exit-------------------------------
 
 elif move == 'exit':
  gameOn = False
  os.system("clear")

#--------------------- invalid statement-----------------
 
 else:
  printMap()
  print("invalid input")
  
