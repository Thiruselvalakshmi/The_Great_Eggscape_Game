'''
****THE GREAT EGGSCAPE****
A little boy is there who needs to collect the egg and escape from the chick.
Since both of them will fall down randomly the task of the boy is to catch the egg
and escape from the chick.
Totally three chances/lives are provided since for every hit he get from the chick
and for every egg miss a chance will be reduced.
Once when all the chances are gone the game ends.
'''


import turtle
import random

coop = turtle.Screen()
coop.setup(740,600)
coop.title("-+-+-+-THE GREAT EGGSCAPE-+-+-+-")
coop.bgpic("D:\MY DETAILS (THIRU)\LMES\game6\chickhouse.gif")
coop.addshape("D:\MY DETAILS (THIRU)\LMES\game6\chick.gif")
coop.addshape("D:\MY DETAILS (THIRU)\LMES\game6\egg.gif")
coop.addshape("D:\MY DETAILS (THIRU)\LMES\game6\lboy.gif")
coop.addshape("D:\MY DETAILS (THIRU)\LMES\game6\Rboy.gif")

chick = turtle.Turtle()
chick.shape("D:\MY DETAILS (THIRU)\LMES\game6\chick.gif")
chick.penup()
chick.hideturtle()
chick.goto(0,250)

egg = turtle.Turtle()
egg.shape("D:\MY DETAILS (THIRU)\LMES\game6\egg.gif")
egg.penup()
egg.hideturtle()
x = random.randint(-300,300)
egg.goto(x,280)

boy = turtle.Turtle()
boy.shape("D:\MY DETAILS (THIRU)\LMES\game6\Rboy.gif")
boy.penup()
boy.goto(0,-170)

scoreboard = turtle.Turtle()
scoreboard.penup()
scoreboard.goto(200,278)
scoreboard.write("Score: 0",font=("Courier",14,"bold"))
scoreboard.hideturtle()
score = 0

chance = turtle.Turtle()
chance.penup()
chance.goto(-200,278)
chance.write("Chances: 3",font=("Courier",14,"bold"))
chance.hideturtle()
chances = 3

coop.listen()

def boyleft():
    x = boy.xcor()
    x = x-10
    if x<=-300:
        x = -300
    boy.shape("D:\MY DETAILS (THIRU)\LMES\game6\lboy.gif")
    boy.setx(x)

def boyrgt():
    x = boy.xcor()
    x = x+10
    if x>=300:
        x = 300
    boy.shape("D:\MY DETAILS (THIRU)\LMES\game6\Rboy.gif")
    boy.setx(x)

def eggmove():
    chick.hideturtle()
    egg.showturtle()
    y = egg.ycor()
    y = y-7
    egg.sety(y)

def chickmove():
    egg.hideturtle()
    chick.showturtle()
    y = chick.ycor()
    y = y-7
    chick.sety(y)

movement_functions = {
    "eggmove": eggmove,
    "chickmove": chickmove
}
chosen_move = random.choice(list(movement_functions.keys()))

coop.onkeypress(boyleft,"Left")
coop.onkeypress(boyrgt,"Right")

while True:
    coop.update()
    movement_functions[chosen_move]()
    ey = egg.ycor()
    cy = chick.ycor()
    if ey<=-220:
        egg.hideturtle()
        chances = chances-1
        if chances == 0:
            chance.write("Chances: {}".format(chances),font=("Courier",14,"bold"))
            chance.goto(-180,180)
            chance.clear()
            chance.write("No Chances Left",font=("Courier",24,"bold"))
            break
        chance.clear()
        chance.write("Chances: {}".format(chances),font=("Courier",14,"bold"))
        x = random.randint(-300,300)
        egg.goto(x,280)
        egg.showturtle()
        chosen_move = random.choice(list(movement_functions.keys()))
        movement_functions[chosen_move]()
        
    if egg.distance(boy)<50:
        score = score+1
        egg.hideturtle()
        scoreboard.clear()
        scoreboard.write("Score: {}".format(score),font=("Courier",14,"bold"))
        x = random.randint(-300,300)
        egg.goto(x,280)
        egg.showturtle()
        chosen_move = random.choice(list(movement_functions.keys()))
        movement_functions[chosen_move]()

    if cy<=-220:
        chick.hideturtle()
        x = random.randint(-300,300)
        chick.goto(x,280)
        chick.showturtle()
        chosen_move = random.choice(list(movement_functions.keys()))
        movement_functions[chosen_move]()

    if chick.distance(boy)<80:
        chances = chances-1
        if chances == 0:
            chance.write("Chances: {}".format(chances),font=("Courier",14,"bold"))
            chance.goto(-180,180)
            chance.clear()
            chance.write("No Chances Left",font=("Courier",24,"bold"))
            break
        chance.clear()
        chance.write("Chances: {}".format(chances),font=("Courier",14,"bold")) 
        chick.hideturtle()
        x = random.randint(-300,300)
        chick.goto(x,280)
        chick.showturtle() 
        chosen_move = random.choice(list(movement_functions.keys()))
        movement_functions[chosen_move]()

turtle.done()