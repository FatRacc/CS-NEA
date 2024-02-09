#pip3 install pygame -pre
#https://www.aqa.org.uk/subjects/computer-science-and-it/as-and-a-level/computer-science-7516-7517/subject-content-a-level/non-exam-assessment-the-computing-practical-project

#[COMPLETED] - buildings are displaying, but lists are not being searched properly ygm??
#[COMPLETED] - keypress -> shortest path between user inputted nodes(clicked on screen)
#[COMPLATED] - Database not working, need to fix??
#[COMPLAETED] - shortest path implement

#===============================================================================
#Modules being imported
#===============================================================================
import pygame
from pygame.locals import *
import sys
import tkinter
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter import *
from tkinter import Tk, Label
from button import Button
import sqlite3
import os
import time
import random
import math
import re
import time
import heapq

#===============================================================================
#parameters
#===============================================================================
pygame.init() #initialising pygame 

fps = 60
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((1920, 1080))
color = (255,255,255)
colorLight = (170,170,170)
colorDark = (100,100,100)
smallfont = pygame.font.SysFont('Corbel',35)
clock = pygame.time.Clock()
run = True
x_1 = 20
y_1 = 20
width = 40
height = 60
vel = 2.87
ALPHA = (0, 255, 0)


#===============================================================================
#display the background image
#===============================================================================
def backgroundDisplay():
    imp = pygame.image.load("assets/Background.png").convert() #loads the image

    screen.blit(imp, (0, 0)) #sets the position of the image
    pygame.display.flip()
    status = True
    while (status): #checks if the game has been closed
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                status = False





#===============================================================================
# main menu
#===============================================================================
BG = pygame.image.load("assets/Background.jpeg")




def get_font(size): # Returns Press-Start-2P in the desired size
  return pygame.font.Font("assets/font.ttf", size)




def play():
    player_render()



def options():
  while True:
      OPTIONS_MOUSE_POS = pygame.mouse.get_pos() #get mouse position




      screen.blit(BG, (0, 0)) #blackout the screen




      OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "White") #render the options screen text
      OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(950, 260))
      screen.blit(OPTIONS_TEXT, OPTIONS_RECT)




      OPTIONS_BACK = Button(image=None, pos=(950, 460),
                          text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green") # display the back button within the options




      OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
      OPTIONS_BACK.update(screen)




      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
          if event.type == pygame.MOUSEBUTTONDOWN:
              if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS): #checks for mouse button presses
                  main_menu() #calls the main menu if so




      pygame.display.update()




def main_menu():
  while True:
      screen.blit(BG, (0, 0)) #blackout the screen




      MENU_MOUSE_POS = pygame.mouse.get_pos()# gets mouse position on the menu screen




      MENU_TEXT = get_font(100).render("FACTORY GAME", True, "#b68f40")# maim menu text
      MENU_RECT = MENU_TEXT.get_rect(center=(950, 100))# location of main menu text




      PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(950, 250), # draws the play button on the screen
                          text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
      OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(950, 400), # draws the options button on the screen
                          text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
      QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(950, 550),# draws the quit button on the screen
                          text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")




      screen.blit(MENU_TEXT, MENU_RECT)




      for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
          button.changeColor(MENU_MOUSE_POS)
          button.update(screen) #updates the buttons on screen depending if hovered or not
    
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
          if event.type == pygame.MOUSEBUTTONDOWN:
              if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                  play() # checks if the player has clicked play
              if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                  options()#checks if the player has clicked options
              if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                  pygame.quit()#checks if the player has clicked quit
                  sys.exit()




      pygame.display.update()#updates the display




#===============================================================================
#charchter render and movement
#===============================================================================
def player_render():
    time.sleep(0.1)#delays the game slightly 
    x, y = 75, 75  #sets charchter position
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #checks if the program is quit
                run = False

        keys = pygame.key.get_pressed() #checks the keys being pressed
        
        
        if keys[pygame.K_a]:
            x -= vel  #player velocity set
            camera_follow()
            print("left")

        if keys[pygame.K_d]:
            x += vel #player velocity set
            camera_follow()
            print("right")

        if keys[pygame.K_w]:
            y -= vel #player velocity set
            camera_follow()
            print("up")

        if keys[pygame.K_s]:
            y += vel #player velocity set
            camera_follow()
            print("down")

        if keys[pygame.K_e]:
            shortestPathInitial()#calls the shortest path function
            print("shortest path calcuator activated")

        if keys[pygame.K_ESCAPE]:
            print("returned to main menu") #returns to the main menu
            main_menu()

        
        left, middle, right = pygame.mouse.get_pressed()
        if left:
            buildingFunction()#calls building function

        if right:
            beltPlacement() #allows belt to be placed

        if middle:
            removeBuildingOrBelt()#calls the remove building or belt function

        if x >= 1920:
            x = 5
        elif x <= 0:
            x = 1915

        if y >= 1080:
            y = 5
        elif y <= 0:
            y = 1075

        checkered_background()#draws the game background
        time.sleep(0.05)
        buildingRender() # renders the buildings
        charachter = pygame.image.load(os.path.join("assets", "SPRITE1.PNG"))
        screen.blit(charachter, (x, y)) #displays the image of the player
        mainPlayerInventory(playerInventory) #initialises the player inventory
        pygame.display.flip()
        #camera_follow()

#===============================================================================
#Building Render
#===============================================================================        
def buildingRender():
    maxlen1 = len(buildingCoordinates) #defines the length of the lists and assigns them a variable
    maxlen2 = len(beltCoordinates)

    for i in range(0, maxlen1):
        x4 = 0
        y4 = 1
        if ((x4 or y4) > maxlen1) or ((x4 or y4) < maxlen1):

            x_coord = buildingCoordinates[x4]
            y_coord = buildingCoordinates[y4]

            image = pygame.image.load(os.path.join("assets", "machine_assembler_tier_1.PNG"))#loads the images specified in the path
            screen.blit(image, (x_coord, y_coord))# blits the image onto the screen

            x4 += 2
            y4 += 2

        else:
            print("No more buildings to render")# error handling

    for i in range(0, maxlen2):
        x5 = 0
        y5 = 1
        if ((x5 or y5) > maxlen2) or ((x5 or y5) < maxlen2):
            x5 = 0
            y5 = 1

            x_coord = beltCoordinates[x5]
            y_coord = beltCoordinates[y5]

            image = pygame.image.load(os.path.join("assets", "machine_miner_tier_1.PNG"))#loads the image specified in the path
            screen.blit(image, (x_coord, y_coord))#blits the imnage onto the screen

            x5 += 2
            y5 += 2

        else:
            print("No more belts to render")# error handling
    
    pygame.display.flip()
#===============================================================================
#tkinter text input window class
#===============================================================================
import tkinter as tk
class App(tk.Tk):#class app for tkinter windows
    def __init__(self):
        super().__init__()#initialises with the super() function

#===============================================================================
#shortest path
#===============================================================================
def shortestPathInitial():

    left, middle, right = pygame.mouse.get_pressed()#checks for the mouse buttons being pressed

    
    if left:
        initialposition = tkinter.askstring("Input", "are you selecting the 'start' or 'end' coordinate?")#asks for user input
        
        if initialposition == "start":#checks the user inout

            x6,y6 = pygame.mouse.get_pos()

            #coordinate maths
            x_over6 = x6 % 32
            x_building_pos6 = x6 - x_over6
            y_over6 = y6 % 32
            y_building_pos6 = y6 - y_over6
            
            #value checking
            print("Initial Y-Position = ", y_building_pos6)
            print("Initial X-Position = ", x_building_pos6)

            #calls the next function if all is ok
            shortestPathSecondary(x_building_pos6, y_building_pos6)
        else:
            print("Incorrect input, try again.")#error handling
            shortestPathInitial()# calls the initial functionof errors occur
            
        
def shortestPathSecondary(x6, y6):

    left, middle, right = pygame.mouse.get_pressed()#checks for mouse button pressed

    if left:
        finalposition = tkinter.askstring("Input", "are you selecting the 'start' or 'end' coordinate?")# asks for user inout
        
        if finalposition == "start":

            x7,y7 = pygame.mouse.get_pos()

            #coordinate math
            x_over7 = x7 % 32
            x_building_pos7 = x7 - x_over7
            y_over7 = y7 % 32
            y_building_pos7 = y7 - y_over7

            #coordinate checking
            print("final Y-Position = ", y_building_pos7)
            print("Final X-Position = ", x_building_pos7)

            #value assignments
            x7 = x_building_pos7
            y7 = y_building_pos7
            print("works!!")#error and progress checking
            dijkstra(x6, y6, x7, y7)#calls djikstra function
        else:
            print("Incorrect input, try again.")#error checking
            shortestPathInitial()#restarting the first function


#===============================================================================
#checkered background
#===============================================================================
def checkered_background():
    square_size = 32 #defines the sqaure size
    width = 1920
    height = 1200
    for row in range(height // square_size):
        for column in range(width // square_size):
            x = column * square_size  # math for calculating the squares
            y = row * square_size  
            if (row+column) % 2 == 0:
                color = (255, 255, 255) #white
            else:
                color = (0, 0, 0) #black
            pygame.draw.rect(screen, color, (x, y, square_size, square_size)) #displays the sqaures




#===============================================================================
#Camera Follow Player
#===============================================================================
def camera_follow():         # currently unused
    camera_width, camera_height = 1280, 1720
    camera = pygame.Rect(0, 0, camera_width, camera_height)
    camera.x, camera.y = 0, 0

    camera_speed = vel
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        camera.x -= camera_speed
        print("CamLeft")
    if keys[pygame.K_RIGHT]:
        camera.x += camera_speed
        print("CamRight")
    if keys[pygame.K_UP]:
        camera.y -= camera_speed
        print("CamUp")
    if keys[pygame.K_DOWN]:
        camera.y += camera_speed
        print("CamDown")

    pygame.display.update(camera.move(camera.x, camera.y))
    pygame.display.flip()

#===============================================================================
#Inventory Main
#===============================================================================
playerInventory = [] #initialise the list

def mainPlayerInventory(playerInventory):
    pygame.draw.rect(screen, (234, 221, 202), (0, 0, 500, 100))#inventory hotbar
    keys = pygame.key.get_pressed()# checks for actively pressed keys

    if keys[pygame.K_q]: #checks the active key and if it is q
        choice = askstring("Input", "Would you like to 'add' or 'retrieve' an item?")#asks the user what item they want to add
        if choice == "add":
            item = askstring("Input", "Please enter the name of the item you would like to add")# item name
            if len(playerInventory) >= 5:#checks if the list is full
                print("Inventory full!")
            else:
                playerInventory.append(item)#adds the item to the list
                print("Item added!")
                print(playerInventory)#recalls the function to draw the inventory again
        elif choice == "retrieve":
            item = askstring("Input", "Please enter the name of the item you would like to retrieve")# asks the user for the item name
            try:
                playerInventory.remove(item)#removes the item from the list
                print("Item retrieved!")
                print(playerInventory)#recalls the function to draw the inventory again
            except ValueError:
                print("Item not in inventory")#checks if the item is there or not 

    posX = len(playerInventory) * 100 #finds the position of the item depending on its position in the list
    pygame.draw.rect(screen, (0, 0, 255), (0, 0, posX, 100)) #updates the screen with the inventory items
    pygame.display.flip()


#===============================================================================
#Mouse x-y coordinate grabber
#===============================================================================
def getMouseXY():
    x1,y1 = pygame.mouse.get_pos()#gets mouse coordinates
    return x1,y1#returns those coordinates


#===============================================================================
#Factory Building Placement
#===============================================================================
buildingCoordinates = [] #initialises the list
beltCoordinates = [] #initialises the list

def buildingFunction():
    print("Building placement attempted")#detects if the mouse is clicked and displays a message if so
    #getMouseXY()
    #coordinate math
    x1,y1 = pygame.mouse.get_pos()
    x_over = x1 % 32 
    x_building_pos = x1 - x_over
    y_over = y1 % 32
    y_building_pos = y1 - y_over

    #checking values
    print("Y-Position = ", y_building_pos)
    print("X-Position = ", x_building_pos)

    print("Currrent Building Locations: ", buildingCoordinates)#printing current list values

    #checking if values exist in the list
    if (y_building_pos in buildingCoordinates and x_building_pos in buildingCoordinates) or (y_building_pos in beltCoordinates and x_building_pos in beltCoordinates):
        print("Building already here!")#error handling
    else:
        #appending coordinates to list
        buildingCoordinates.append(x_building_pos)
        buildingCoordinates.append(y_building_pos)

        #user input
        building_function = askFunction()
                

        #checking building function
        if building_function == "assembler":
            building = pygame.image.load(os.path.join("assets", "machine_assembler_tier_1.PNG"))#loading relevant images
            screen.blit(building, (x_building_pos, y_building_pos))#getting relevant coordinates
            pygame.display.flip()#blits the image onto the screen
                    
                        
        #checking building function
        elif building_function == "miner":
            miner = pygame.image.load(os.path.join("assets", "machine_miner_tier_1.PNG"))#loading releveant image
            screen.blit(miner, (x_building_pos, y_building_pos))# getting relevant coordinates
            pygame.display.flip()#blits thye image onto the screen
                    

        else:
            #error handling
            print("Invalid entry!")
            askFunction()#calling the function again


#===============================================================================
#ask function
#===============================================================================
def askFunction():
    #asking for user input
    building_function = askstring("Input", "Would you like this building to be an 'assembler' or a 'miner'")
    return building_function #returning the user input.


#===============================================================================
#Factory Belt Placement
#===============================================================================
def beltPlacement():
    #getMouseXY()

    #coordinate mathy
    x2,y2 = pygame.mouse.get_pos()
    x_over = x2 % 32 
    x_belt_pos = x2 - x_over
    y_over = y2 % 32
    y_belt_pos = y2 - y_over

    #value checking
    print("Y-Position = ", y_belt_pos)
    print("X-Position = ", x_belt_pos)

    #prints the current list
    print("Currrent Building Locations: ", buildingCoordinates)

    #checking for values in the list alrady
    if (y_belt_pos in buildingCoordinates and x_belt_pos in buildingCoordinates) or (y_belt_pos in beltCoordinates and x_belt_pos in beltCoordinates):
        print("Building already here!")#error handling
    else:
        #appending values to the list
        buildingCoordinates.append(x_belt_pos)
        buildingCoordinates.append(y_belt_pos)

        belt = pygame.image.load(os.path.join("assets", "belt_tier_1.PNG"))#loads the relevant image
        screen.blit(belt, (x_belt_pos, y_belt_pos))#blits ontp the screen
        pygame.display.flip()#updates the scren


#===============================================================================
#remove building or belt
#===============================================================================
def removeBuildingOrBelt():
    #getMouseXY()

    #coordinate math
    x3,y3 = pygame.mouse.get_pos()
    x_over = x3 % 32 
    x_thing_pos = x3 - x_over
    y_over = y3 % 32
    y_thing_pos = y3 - y_over

    #value checking
    print("Y-Position to be removed = ", y_thing_pos)
    print("X-Position to be removed= ", x_thing_pos)

    #checking for values in lists
    if y_thing_pos in buildingCoordinates:
        buildingCoordinates.remove(y_thing_pos)# removes the values
    elif y_thing_pos in beltCoordinates:
        beltCoordinates.remove(y_thing_pos)# removes the values
    else:
        print("no Y-coordinate")#error handling

    if x_thing_pos in buildingCoordinates:
        buildingCoordinates.remove(x_thing_pos)# removes the values
    elif x_thing_pos in beltCoordinates:
        beltCoordinates.remove(x_thing_pos)# removes the values
    else:
        print("no X-Coordinate")# error handling



#===============================================================================
#goofy ahh database
#===============================================================================
#connect main database
    
conn = sqlite3.connect('user_data.db')
c = conn.cursor()

def databaseConnect():
    

    # Create Usernames table
    c.execute('''
        CREATE TABLE IF NOT EXISTS Usernames (
            user_id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE
        )
    ''')

    # Create Passwords table
    c.execute('''
        CREATE TABLE IF NOT EXISTS Passwords (
            user_id INTEGER PRIMARY KEY,
            password TEXT NOT NULL
        )
    ''')

    # Create UserIDs table
    c.execute('''
        CREATE TABLE IF NOT EXISTS UserIDs (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT
        )
    ''')

    conn.commit()
    conn.close()

# Function to insert data into tables
def databaseAppendMain(username, password):
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()

    # Insert username into Usernames table
    c.execute('''
        INSERT INTO Usernames (username)
        VALUES (?)
    ''', (username,))

    # Get the user_id assigned to the inserted username
    user_id = c.lastrowid

    # Insert password and user_id into Passwords table
    c.execute('''
        INSERT INTO Passwords (user_id, password)
        VALUES (?, ?)
    ''', (user_id, password))

    conn.commit()
    conn.close()

# Function to find username and password
def databaseSearch(username):
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()

    # Find user_id for the given username
    c.execute('''
        SELECT user_id FROM Usernames
        WHERE username = ?
    ''', (username,))

    result = c.fetchone()

    if result:
        user_id = result[0]

        # Find password for the given user_id
        c.execute('''
            SELECT password FROM Passwords
            WHERE user_id = ?
        ''', (user_id,))

        password = c.fetchone()[0]
        conn.close()

        return username, password

    conn.close()
    return None  # Return None if username not found



#===============================================================================
# Login system
#===============================================================================
#tkinter window defining
window = tk.Tk()
window.title("Login form")
window.geometry('340x440')
window.configure(bg='#333333')



def login():
    username = "master" #defines username
    password = "password" # defines password
    databaseConnect() #cnnects the database
    #databaseAppendMain(username, password)# appends the main values to the database
    
    master_username = "muser" #defines the master username
    master_password = "mpass" #defines the master password
    if username_entry.get()==master_username and password_entry.get()==master_password:#checks user entry for mater credentials
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")#message if correct
        main_menu()#maine manu function
    elif username_entry.get() == databaseSearch(username_entry.get()) and password_entry.get() == databaseSearch(password_entry.get()):#checks user credientials in the database
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")#message f correct
        main_menu()#main menu function
    else:
        messagebox.showerror(title="Error", message="Invalid login.")#error handling

frame = tkinter.Frame(bg='#333333')#frame size


# Creating widgets
login_label = tk.Label(
    frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
username_label = tk.Label(
    frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tk.Entry(frame, font=("Arial", 16))
password_entry = tk.Entry(frame, show="*", font=("Arial", 16))
password_label = tk.Label(
    frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button = tk.Button(
    frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()#loops the main window. similar to the screen.blit() function in pygame but for tkinter modules and fron the App class instead


#===============================================================================
#djikstras shortest path?
#===============================================================================
def dijkstra(grid, start, end):
    rows, cols = len(grid), len(grid[0]) #defines rows and columns
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] #defines directions on the grid

    # Helper function to check if a cell is within the grid
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    # Priority queue to store nodes with their respective costs
    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)

    # Dictionary to store the cost of reaching each node from the start node
    cost_dict = {start: 0}

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node == end:
            break

        for dx, dy in directions:
            new_x, new_y = current_node[0] + dx, current_node[1] + dy

            if is_valid(new_x, new_y):
                new_cost = current_cost + grid[new_x][new_y]

                if (new_x, new_y) not in cost_dict or new_cost < cost_dict[(new_x, new_y)]:
                    cost_dict[(new_x, new_y)] = new_cost
                    heapq.heappush(priority_queue, (new_cost, (new_x, new_y)))

    # Reconstruct the path
    path = []
    current_node = end

    while current_node != start:
        path.append(current_node)
        for dx, dy in directions:
            prev_node = (current_node[0] - dx, current_node[1] - dy)
            if is_valid(prev_node[0], prev_node[1]) and cost_dict.get(prev_node, float('inf')) == cost_dict[current_node] - grid[prev_node[0]][prev_node[1]]:
                current_node = prev_node
                break

    path.append(start)
    path.reverse()

    return path


#===============================================================================
#Main function
#===============================================================================
def program_start():
    login()#calls the login window
    pygame.quit()#checks if the program is closed down or quit


#===============================================================================
#Main While loop - LEAVE AS IS
#===============================================================================
program_start()#start function to avoid recusrion errors
