import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -100
y1 = 100
x2 = -100
y2 = 50
x3 = -100
y3 = 0
x4 = -100
y4 = -50


# Section 2 - Setup
set_background("castle")
t1 = create_sprite("Kool-Aid_Man",x1,y1)
t2 = create_sprite("Pepsi_Man",x2,y2)
t3 = create_sprite("Sprite",x3,y3)
t4 = create_sprite("LIL SWEET",x4,y4)

x1 += 199
x2 += 210
x3 += 300
x4 += 350

t1.goto(x1, y1)
t2.goto(x2, y2)
t3.goto(x3, y3)
t4.goto(x4, y4)

window.update()
time.sleep(0.1)


if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("Dr. Pepper wins!")
elif
    print("Sprite wins!")

if x3 >=x4 and x3 >= x1 and x1 >= x2:
    print("LIL SWEET wins!")\
elif
    print("Pepsi-Man wins!")
turtle.exitonclick()