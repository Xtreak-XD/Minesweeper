#Miguel Avila, Nicolas Fajet, Katherine Lorenzo
#2/8/2024
#Minesweeper Game
#This code was also helped by various online sources and videos that were used as reference to understand different sections, if code was 
#somewhat copied from the user it will be stated. ChatGPT was used in fair use as stated in the AP Computer Science Principles Student 
#Handouts, in some part to help Debug the program.
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random 
import time

#Brings up an empty window
window = tk.Tk()
window.title("Minesweeper")
buttons = [] #Creates empty lists for future use
pField = []
gameOver = False #gameOver variable that will detect when game is beat
gameArea = Frame(window)
gameArea.grid(row = 1, 
              column = 0,
              pady = 0) #Places the gameArea Frame into the 1st row
startTime = 0
elapsedTime = 0

#Clears the game screen when restarting game
def clearGame():
    global gameArea, custom, startTime, gameOver
    gameOver = False
    for boxes in custom.winfo_children(): #Checks all the entry boxes in the custom grid
        boxes.destroy() #Destroys them all 
    for w in gameArea.winfo_children(): #Obtains all the grids 
        if type(w) != tk.Menu:#Makes sure it only deletes the grids of minesweeper
            w.destroy() #Destroy them all
    placeBombs(rVal,cVal) #restarts the game
    gameMenu()
    startTime = time.time() #Restarts the timer back
    Timer()
    
def placeBombs(rows,cols):  
    global buttons, pField, flags, gameCounter, bomb
    bomb = (rows*cols)//6  
    flags = bomb
    pField=[] #Recalls the pField list for better code runtime
    for x in range(0, rows): #Parts of this section were influenced by chatGPT
        pField.append([])
        for y in range(0, cols):
            pField[x].append(0) #Sets the bombs into the list 
    bombP=random.sample(range(rows*cols), bomb) #Randomizes the bombs ensuring that they are not overlapping each other
    for pos in bombP:
        x, y=divmod(pos,cols) #returns the quotient and remainder
        pField[x][y] = -1 #Marks each spot on the list that is a bomb as -1
    play(rows,cols) #Transfer the rows and columns into the play function
    
def Timer(): #starts the timer at the top right of the screen
    global startTime, gameOver, timerBox, elapsedTime
    if gameOver:
        return
    elapsedTime = int(time.time() - startTime) #Makes it so only the second gets counted and no decimals
    timerBox.config(text = "Time: " + str(elapsedTime) + " S")
    window.after(1000, Timer) #The timer is only called every 1000 milliseconds so that it updates every second 
 
#Check if the user has won   
def win():
    global elapsedTime, gameOver, buttons, pField, rows, columns
    gameWon = True 
    for x in range(0, rVal):
        for y in range(0, cVal):
            if pField[x][y] != -1 and buttons[x][y]["state"] != "disabled": #Checks to see if all the non bomb squares have been deactivated
                 gameWon = False
    if gameWon: #When statement doesn't change it means the user has won
        gameOver = True
        winMsg = tk.messagebox.askretrycancel("You win!!!!",        #Makes a pop up screen that tells the user has won in a given amount of time
                    "Congratulations you have won the game in " + str(elapsedTime) + "seconds :)\n (Press retry to restart with same grid size)")
        if winMsg == True:
            clearGame() #Resets game when user clicks retry
    
#Game over condition.
def endGame():
    global pField, buttons, gameOver, rVal, cVal
    gameOver = True  
    for i in range(0,rVal):    #When user clicks a bomb all the other bombs will appear on screen
        for j in range(0,cVal):
            if pField[i][j]==-1:
                buttons[i][j].config(text="B", #They will have the letter B and will eb turned red and will pop out
                                     bg="red",
                                     disabledforeground="black", 
                                     relief = RIDGE)
    loseMsg=tk.messagebox.askretrycancel("GameOver",
                    "You lost the game in " + str(elapsedTime) + " seconds :(\n (Press retry to restart with same grid size)") #Tells the user they have lost and tells the amount of time it took
    if loseMsg == True:
        clearGame()
        
#Generate the custom menu
def customMenu():
    global custom, Box, Box2, btn, entryR, entryC
    custom = Frame(window)
    custom.grid(row=0,
                column=0) 
    Box=Label(custom, 
              text = "How many rows would you like: ") #Asks the user for how many rows and columns they wants
    Box.grid(row = 0, 
             column = 0)
    entryR = tk.Entry(custom) #This is an input box that obtains the number the user puts
    entryR.grid(row = 0,
                 column = 1)
    Box2=Label(custom,
              text = "How many columns would you like: ")
    Box2.grid(row = 1,
              column = 0)
    entryC = tk.Entry(custom)
    entryC.grid(row = 1,
                 column = 1)
    btn = Button(custom,
                 text = "Continue",
                 command = lambda: customSize(entryR, entryC)) #lambda command waits until button is pressed to activate command
    btn.grid(row = 2,
             column = 0,
             columnspan = 2) #columnspan makes the button take over 2 columns and be in the middle
    
#Detects for whether the user has inputted over 25 and asks them to retype it
def customSize(r,c):
    global rows,columns,bombs, entryR, entryC, rVal, cVal, startTime
    rVal=int(r.get()) #Turns the entry input into an integer
    cVal=int(c.get()) #rVal holds number of rows and cVal holds number of columns
    if rVal>25 or cVal>25: #This is why rVal and cVal need to be in integer form
        if rVal>25: #Checks that the number of columns and rows fall under a limit of 25
            Box=Label(custom, 
                      text = "Please enter a number less than 25: ",
                      fg="red") #Makes it so the user can see what its asking
            Box.grid(row = 0, 
                     column = 0)
            entryR= tk.Entry(custom) #Places the input box back
            entryR.grid(row=0,
                        column=1)
            r.delete(0, END) #Clears all characters in the box
        if cVal>25:
            Box2=Label(custom,
                       text = "Please enter a number less than 25: ",
                       fg="red")
            Box2.grid(row=1,
                      column=0)
            entryC=tk.Entry(custom)
            entryC.grid(row=1,
                        column=1)
            c.delete(0, END)
    rVal=int(entryR.get())
    cVal=int(entryC.get())
    clearGame() 
    startTime = time.time()  #Starts the timer but from our current epoch
    Timer()
    
def play(rows,columns):#Sets up the grid 
    global  gameArea, pField, buttons, button
    buttons = [] #Recalls the buttons grid
    for x in range(0, rows): #This sections was references from vakus from a Code Review post in 2022
        buttons.append([]) #Adds the buttons into the list for each ow
        for y in range (0, columns):
            gameButton=(Button(gameArea, text= " ", 
                                 width = 2,
                                 command=lambda x=x, y=y: click(x,y), #when the button is pressed the function click is called to determine number of bombs
                                 bg = "pink",
                                 borderwidth = 5,
                                 relief = GROOVE))            
            gameButton.bind("<Button-3>", lambda e, x=x, y=y: rightClick(x, y)) #Makes the right click bind place flags (question marks)
            gameButton.grid(row=x+1, 
                            column=y, 
                            sticky=N+W+S+E)
            buttons[x].append(gameButton) #Adds all the buttons into a list
            adjMineNum = 0                    
            if pField[x][y] != -1: #Adds a value to each button that is determined by how many bombs are around it
                adjMineNum = 0
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if 0 <= x + i < rVal and 0 <= y + j < cVal and pField[x + i][y + j] == -1:
                            adjMineNum += 1
                            pField[x][y] = adjMineNum
                            
#Function that opens all adjacent grids if they are 0
def revealAdjBlock(x, y): 
    global pField, buttons, rows, columns 
    color = getButtonColor(pField[x][y])
    if buttons[x][y]["state"] == "disabled": 
        return
    if pField[x][y] != 0:
        buttons[x][y].config(text = pField[x][y]) #If the buttonAdjacent doesn't equal 0 then it will just be updated to bombs around it
    else: 
        buttons[x][y].config(text = "0")
    buttons[x][y].config(bg = color,
                         fg="white", 
                         relief=SUNKEN, 
                         state="disabled")  
    if pField[x][y] == 0: #Logic that detects for bombs around the square 
        for i in [-1, 0, 1]: 
            for j in [-1, 0, 1]:
                if 0 <= x + i < rVal and 0 <= y + j < cVal and pField[x+i][y+j] >= 0: #If no bombs and its within the bound of 
                    revealAdjBlock(x+i, y+j)                                          #it will reveal the button
                    
#Function that determines the button's color based on how many bombs are around it
def getButtonColor(mineNum):
    if mineNum == 1:
        return "#4cb9fa"
    elif mineNum == 2:
        return "#a1eca7"
    elif mineNum == 3:
        return "#c4342d"
    elif mineNum == 4:
        return "#512888"
    elif mineNum == 5:
        return "#e8b923"
    elif mineNum >= 6:
        return "#f08b35"
    else:
        return "grey"  # Default color if mineNum is not in the specified range
    
def gameMenu():
    global gameArea, flags, flagBox, timerBox
    topFrame = Frame(window)
    topFrame.grid(row = 0, 
                  column = 0,
                  pady = 0) 
    
    flagBox = Label(topFrame, 
                  text = "Flags: " + str(flags), 
                  bg = "pink", 
                  relief = RIDGE,
                  justify = "center",
                  height = 2,
                  width = 7,
                  pady = 0) 
    flagBox.grid(row=0, 
                 column=0,
                 pady = 0)
    
    timerBox = Label(window,
                     text = "Time: --- S",
                     bg = "pink",
                     relief = RIDGE,
                     justify = "center",
                     height = 2,
                     width = 10,
                     pady = 0)
    timerBox.grid(row = 0,
                  column = 0,
                  sticky = E,
                  pady = 0) #Sticky positions this to right

    rLabel = Button(window, 
                    text = "Restart", 
                    command = lambda: [clearGame(), customMenu()], #When restart button is pressed both the clearGame and customMenu function are called
                    bg = "pink",
                    relief = RIDGE,
                    height = 2,
                    width = 7,
                    pady = 0)
    rLabel.grid(row = 0,
                column = 0,
                sticky = W,
                pady = 0) #Sticky positions this on the left
    
#Function that allows for right click to place a flag
def rightClick(x, y):
    global buttons, gameOver, flags, flagBox
    if gameOver:
        return
    if buttons[x][y]["text"] == " " and flags > 0: #If there is no flag in the button and flags are available a ? will be put
        buttons[x][y].config(text="?",
                             bg = "#702963",
                             state = "disabled",
                             relief = RAISED)
        flags -= 1
        flagBox.config(text="Flags: " + str(flags)) #Updates counter
    elif buttons[x][y]["text"] == "?": #If there is a ? on the button it will remove it and pu it back to original 
        buttons[x][y].config(text=" ",
                             bg = "pink",
                             state = "normal",
                             relief = GROOVE)
        flags += 1
        flagBox.config(text="Flags: " + str(flags)) #Updates counter
        
#Create a click on function that detects when a button is clicked on and reveal whether its a bomb or not
def click(x,y):                                                    #x=Rows, y=Columns
    global pField, buttons, gameCounter, color
    if buttons[x][y]["state"] == "disabled": #Cehcks if the button is disable in order to not intrude with code
        return
    if pField[x][y] == -1: #Checks if the square clicked is a bomb
        endGame()
    elif pField[x][y] == 0: #If the square has no bombs around it, it will reveal adjacent bombs until it hits ones with bombs around
        revealAdjBlock(x,y)
    else:
        color = getButtonColor(pField[x][y]) #If it has bombs around it will reveal the number of bombs around it
        buttons[x][y].configure(text = pField[x][y],
                                bg = color,
                                fg = "white", 
                                relief = SUNKEN,
                                state = "disabled")
    win() #checks to see if the user has won
    
#Clears the game screen when restarting game
def clearGame():
    global gameArea, custom, startTime, gameOver
    gameOver = False
    for boxes in custom.winfo_children(): #Checks all the entry boxes in the custom grid
        boxes.destroy() #Destroys them all 
    for w in gameArea.winfo_children(): #Obtains all the grids 
        if type(w) != tk.Menu:#Makes sure it only deletes the grids of minesweeper
            w.destroy() #Destroy them all
    placeBombs(rVal,cVal) #restarts the game
    gameMenu()
    startTime = time.time() #Restarts the timer back
    Timer()
    
customMenu() #Starts the custom menu screen

#run
window.mainloop()
