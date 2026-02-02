import turtle, time, random
from utils import *

set_background("SnowMT")

# TODO - create at least two variables and set their starting value. ex: cookies = 0
style_points = 0
trick_park = 0
cost = 20
# OPTIONAL: use this invisible alien to say a message
message_sprite = create_sprite("alien", -200,200)
message_sprite.hideturtle()



# Section 2 - controls
def get_style_points():
    global style_points
    style_points += 1
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    create_sprite("Snowboy",x,y )

def get_trick_park():
    global trick_park, style_points, cost
    if style_points >= cost:
        cost = cost * 2
        trick_park += 1 
        x = -400 + 120*trick_park
        y = -250
        create_sprite("trick",x,y)

# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")
window.onkeypress(get_style_points,"w")
# TODO - make a second control
window.onkeypress(get_trick_park, "b")




# Section 3 - game loop
window.listen()
for i in range(1000000000):
    message_sprite.clear()
    message_sprite.write(f"style_points: {style_points}\nCost: {cost}\ntrick_park: {trick_park}",font=("Arial",30,"normal"))
    
    # TODO - put any automatic actions here

    # OPTIONAL - use the message sprite to say a message
    # message_sprite.clear()
    # message_sprite.write("Hello")

    time.sleep(0.01)
    window.update()