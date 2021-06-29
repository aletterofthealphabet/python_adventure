# Vi Vu, Hermon Gebrehiwet
from random import *

# monster room- you will need to rename this function.
def heat_room():
  # some prompts
  # '\n' is to print the line in a new line
  print("This is the heat room, you see a furance, you can: ")
  print("1) Turn the heat up")
  print("2) Leave the heat alone") # Activates wall trap

  # get user input take input()
  answer = input(">")
  if answer == "1":
    ranNum = randint(1, 2)
    if ranNum == 1:
        falling_room()
    else:
        spike_room()
  else:
    game_over("You froze to death")

def falling_room():
    print("There are two steep paths in this room, to get to the door you can: ")
    print("1) Take the path") # Path will collapse
    print("2) Use a rope")

    answer = input(">")

    if answer == "2":
        spike_room()
    else:
        game_over("The path gave out, you've fallen to your death")

def walls_room():
    print("Theres a riddle in the middle of this room with a keyboard to enter in a word.")
    print("I speak without a mouth and hear without ears. I have no body but I come alive with wind. What am I?")
    
    answer = input(">").lower()

    if answer == "echo":
        game_over("You've excaped the escape room!")
    else:
        game_over("The room closes in on itself, you got crushed to death")

def spike_room():
    print("In this room there's a path and a wall. To escape you can either climb the wall or use the path.")
    print("1) You can climb the wall")
    print("2) You can use the path")

    answer = input(">")

    if answer == "2":
        walls_room()
    else:
        game_over("You got impaled by spikes.")

# function to ask play again or not
def play_again():
  # use print statement to ask if user wants to play again
  print("Do you want to play again? Y/N")
  # get input
  answer = input(">")
  # evaluate input using conditional 
  if(answer == "y"):
    start()
  else:
    exit()


# game_over function accepts an argument called "reason"
def game_over(reason):
  # print the "reason" in a new line (\n)
  print("\n" + reason)
  print("Game Over!")
  # STRETCH: maybe ask player to play again or not. 
  play_again()


def start():
# have some introductory text printed like: ("\nYou are standing in a dark room.")
    print("\nNow you've entered the excape room!")
    print("The escape room is full of traps.\n To escape you need to avoid the traps, if you get them wrong,")
    print("they will activate.")   
    print("You can go to the: ")
    print("1) Heat room")
    print("2) Walls room")
  
    # get user input using input() and save 
    answer = input(">").lower()
    if answer == "1":
        heat_room()
    elif answer == "2":
        walls_room()
    else:
        game_over("Don't you know how to type something properly?")


# calling start function. 
start()