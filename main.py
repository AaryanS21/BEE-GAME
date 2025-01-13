import pgzrun
import random
import time

WIDTH = 600
HEIGHT = 600
score = 0
game_over = False
bee=Actor('bee')
bee.pos=(100,100)
flower=Actor('flower')
flower.pos=(200,200)
msg=''

def draw():
    screen.blit('background',(0,0))
    flower.draw()
    bee.draw()
    screen.draw.text('score:' +str(score), color='black' , topleft=(10,10))
    
    if game_over:
        screen.fill('blue')
        global msg
        msg="Time's up!\nYour Final Score:"
        screen.draw.text(msg+str(score),midtop=(WIDTH/2,20),fontsize=50, color='green')
    

def place_flower():
    flower.x = random.randint(50,(WIDTH-50))
    flower.y = random.randint(50,(HEIGHT-50))



def time_up():
    global game_over
    game_over = True

def update():
    global score
    if keyboard.left:
        bee.x = bee.x - 2
    if keyboard.right:
        bee.x = bee.x +2
    if keyboard.up:
        bee.y = bee.y -2
    if keyboard.down:
        bee.y = bee.y +2
    # if flower img box collides with bee img box 
    flower_collected = bee.colliderect(flower)
    if flower_collected==True:
        score = score + 10
        place_flower()

clock.schedule(time_up, 45.0)
pgzrun.go()