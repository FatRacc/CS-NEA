#pip3 install pygame -pre
#redo tasks 1-5 of the NEA to ensure continuity.



#===============================================================================
#Modules being imported
#===============================================================================
import pygame
from pygame.locals import *
import sys
from tkinter.simpledialog import askstring
from tkinter import *
from button import Button
import os
import time
import random
import math
import re
import time

#===============================================================================
#parameters
#===============================================================================
pygame.init() #initialising pygame 

fps = 60
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720
))
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
BG = pygame.image.load("assets/Background.jpg")




def get_font(size): # Returns Press-Start-2P in the desired size
  return pygame.font.Font("assets/font.ttf", size)




def play():
    main_account_screen()



def options():
  while True:
      OPTIONS_MOUSE_POS = pygame.mouse.get_pos()




      screen.fill("white")




      OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
      OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
      screen.blit(OPTIONS_TEXT, OPTIONS_RECT)




      OPTIONS_BACK = Button(image=None, pos=(640, 460),
                          text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")




      OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
      OPTIONS_BACK.update(screen)




      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
          if event.type == pygame.MOUSEBUTTONDOWN:
              if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                  main_menu()




      pygame.display.update()




def main_menu():
  while True:
      screen.blit(BG, (0, 0))




      MENU_MOUSE_POS = pygame.mouse.get_pos()




      MENU_TEXT = get_font(100).render("FACTORY GAME", True, "#b68f40")
      MENU_RECT = MENU_TEXT.get_rect(center=(675, 100))




      PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                          text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
      OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                          text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
      QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                          text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")




      screen.blit(MENU_TEXT, MENU_RECT)




      for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
          button.changeColor(MENU_MOUSE_POS)
          button.update(screen)
    
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
          if event.type == pygame.MOUSEBUTTONDOWN:
              if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                  play()
              if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                  options()
              if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                  pygame.quit()
                  sys.exit()




      pygame.display.update()


#===============================================================================
# Login system
#===============================================================================
def register(): #registration window
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()

def login(): #login window
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()

def register_user(): #event on register button
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    button(login_success_screen, text="OK", command=delete_login_success).pack()
    player_render()

# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
from tkinter import Tk, Label

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    
    Login_button = button(main_screen, text="Login", height="2", width="30", command=login)
    Login_button.pack()
    
    Label(text="").pack()
    
    Register_button = button(main_screen, text="Register", height="2", width="30", command=register)
    Register_button.pack()

    main_screen.mainloop()

#===============================================================================
#button class
#===============================================================================

class button():
    def __init__(self, master, text, height, width, command):
        self.master = master
        self.text = text
        self.height = height
        self.width = width
        self.command = command
        self.button = tk.Button(self.master, text=self.text, height=self.height, width=self.width, command=self.command)


#===============================================================================
#tkinter text input window class
#===============================================================================
import tkinter as tk
class App(tk.Tk):
    def __init__(self):
        super().__init__()

app = App()
app.mainloop()
#===============================================================================
#charchter render and movement
#===============================================================================
def player_render():
    time.sleep(0.1)
    x, y = 0, 0  #sets charchter position
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

        if keys[pygame.K_ESCAPE]:
            print("returned to main menu") #returns to the main menu
            main_menu()

        left, middle, right = pygame.mouse.get_pressed()
        if left:
            time.sleep(0.3)
            buildingPlacement() #allows factory building to be placed
        if right:
            time.sleep(0.3)
            beltPlacement() #allows belt to be placed

        

        checkered_background()
        charachter = pygame.image.load(os.path.join("assets", "SPRITE1.PNG"))
        screen.blit(charachter, (x, y)) #displays the image of the player
        mainPlayerInventory(playerInventory) #initialises the player inventory
        pygame.display.flip()
        #camera_follow()

#===============================================================================
#checkered background
#===============================================================================
def checkered_background():
    square_size = 32 #defines the sqaure size
    width = 1920
    height = 1080
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
    x1,y1 = pygame.mouse.get_pos()
    return x1,y1
#===============================================================================
#Factory Building Placement
#===============================================================================
buildingCoordinates = [] #initialises the list

def buildingPlacement():
    print("Building placement attempted")#detects if the mouse is clicked and displays a message if so
    #getMouseXY()
    x1,y1 = pygame.mouse.get_pos()
    x_over = x1 % 32 
    x_building_pos = x1 - x_over
    y_over = y1 % 32
    y_building_pos = y1 - y_over

    print("Y-Position = ", y_building_pos)
    print("X-Position = ", x_building_pos)

    print("Currrent Building Locations: ", buildingCoordinates)

    if y_building_pos in buildingCoordinates and x_building_pos in buildingCoordinates:
        print("Building already here!")
    else:
        buildingCoordinates.append(x_building_pos)
        buildingCoordinates.append(y_building_pos)
        buildingFunction(x_building_pos, y_building_pos)
        print("Buildings placed at ", buildingCoordinates)
        
        
        building = pygame.image.load(os.path.join("assets", "machine_assembler_tier_1.PNG"))
        screen.blit(building, (x_building_pos, y_building_pos))
        pygame.display.flip()
        

#===============================================================================
#Factory Building function window
#===============================================================================
def buildingFunction(x_building_pos, y_building_pos):
    window = tk.Tk()
    window.title("Building Function")
    
    def button_click(button_number):
        print(f"button {button_number} clicked!")
#===============================================================================
#Factory Belt Placement
#===============================================================================
def beltPlacement():
    print("Belt Placed")#detects if mouse was clicked and displays a message if so

#===============================================================================
#Main function
#===============================================================================
def program_start():
    main_menu()#calls the main menu
    pygame.quit()#checks if the program is closed down or quit


#===============================================================================
#Main While loop - LEAVE AS IS
#===============================================================================
while run:
  program_start()#start function to avoid recusrion errors

