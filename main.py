import os

#------------------- variables-----------------------

map = [["P","-","-","-"],["-","-","-","-"],["-","-","-","-"],["-","-","-","-"]]

coordX=0
coordY=0
R = 4

gameOn = True

#--------------------- functions----------------------

def printMap():
 os.system("clear")
 for y in range(R): 
  for x in range(R):
   print(map[x][y], end=' ')
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

#-------------------- move down -----------------------
 
 if move == 's' or move == 'S':
  temp = map[coordX][coordY + 1] 
  map[coordX][coordY + 1] = map[coordX][coordY]
  map[coordX][coordY] = temp
  coordY = coordY + 1
  printMap()
  
#-------------------move up----------------------------
 
 elif move == 'w' or move == 'W':
  
   temp = map[coordX][coordY-1]
   map[coordX][coordY-1]= map[coordX][coordY]
   map[coordX][coordY] = temp
   coordY = coordY - 1
   printMap()
  

#-------------------move left----------------------------
 
 elif move == 'a' or move == 'A':
  temp = map[coordX-1][coordY]
  map[coordX-1][coordY]= map[coordX][coordY]
  map[coordX][coordY] = temp
  coordX = coordX - 1
  printMap()

 

#-------------------move right----------------------------
 
 elif move == 'd' or move == 'D':
  temp = map[coordX+1][coordY]
  map[coordX+1][coordY]= map[coordX][coordY]
  map[coordX][coordY] = temp
  coordX = coordX + 1
  printMap()


#--------------------exit-------------------------------
 
 elif move == 'exit':
  gameOn = False
  os.system("clear")

#--------------------- invalid statement-----------------
 
 else:
  printMap()
  print("invalid input")
  
