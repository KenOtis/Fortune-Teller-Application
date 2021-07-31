#magic 8 ball 
from random import randint

def question():
    question=input("What question would you like answered? ")
    

def answer():
    value=randint(0,5)
    if value == 0:
        print("It is certain")
    elif value == 1:
        print("It is not likely")
    elif value == 2:
        print ("It is inevitable")
    elif value == 3:
        print ("Ask again Later")
    elif value == 4:
        print ("It is not clear")
    elif value == 5:
        print ("My sources say no")

x='y' 
while x == 'y':
    question()
    answer()
    x=input("Would you like to ask again? (y/n)")