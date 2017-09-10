#Sam Leung
#BurgerTime.py
#May 25, 2016
#This program will simulate a fun and simplified version of the classic retro game BurgerTime.

import math
import random
import pygame, sys
from pygame.locals import *
pygame.init()

#set screen dimensions 
WIDTH = 600
HEIGHT = 600 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('BurgerTime')

#define colour values 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#loading images
title = pygame.image.load("title screen.jpg")
start = pygame.image.load("start.jpg")
levelone = pygame.image.load("level one demo.png")
win = pygame.image.load("win.jpg")
gameover = pygame.image.load("game over.jpg")
burgertop = pygame.image.load("burgertop.png")
beef = pygame.image.load("beef.png")
lettuce = pygame.image.load("lettuce.png")
burgerbottom = pygame.image.load("burgerbottom.png")
pp_stand_front = pygame.image.load("pp_stand_front.png")
pp_stand_back = pygame.image.load("pp_stand_back.png")
pp_down_1 = pygame.image.load("pp down 1.png")
pp_down_2 = pygame.image.load("pp down 2.png")
pp_down_3 = pygame.image.load("pp down 3.png")
pp_down_4 = pygame.image.load("pp down 4.png")
pp_up_1 = pygame.image.load("pp up 1.png")
pp_up_2 = pygame.image.load("pp up 2.png")
pp_up_3 = pygame.image.load("pp up 3.png")
pp_up_4 = pygame.image.load("pp up 4.png")
pp_right_1 = pygame.image.load("pp right 1.png")
pp_right_2 = pygame.image.load("pp right 2.png")
pp_right_3 = pygame.image.load("pp right 3.png")
pp_right_4 = pygame.image.load("pp right 4.png")
pp_left_1 = pygame.image.load("pp left 1.png")
pp_left_2 = pygame.image.load("pp left 2.png")
pp_left_3 = pygame.image.load("pp left 3.png")
pp_left_4 = pygame.image.load("pp left 4.png")
pp_dead = pygame.image.load("dead.png")
hd_left_1 = pygame.image.load("hot_dog_left_1.png")
hd_right_1 = pygame.image.load("hot_dog_right_1.png")
zero = pygame.image.load("zero.png")
one = pygame.image.load("one.png")
two = pygame.image.load("two.png")
three = pygame.image.load("three.png")
four = pygame.image.load("four.png")
five = pygame.image.load("five.png")
six = pygame.image.load("six.png")
seven = pygame.image.load("seven.png")
eight = pygame.image.load("eight.png")
nine = pygame.image.load("nine.png")
pepper = pygame.image.load("pepper.png")

#global variables
pp = pp_stand_front
hdp = hd_right_1
current = title
ax = 195
ay = 360
px = 290
py = 445
hdx = [50, 50, 277, 158]
hdy = [67, 361, 151, 193]
direction = "standfront"
hddirection = ["right", "left", "right", "right"]
speed = 2
right = 0
left = 0
up = 0
down = 0
burgertops = 0
lettuces = 0
beefs = 0
burgerbottoms = 0
score = 0
lives = 3
peppers = 1
btx = [78, 200, 320, 440]
bty = [170, 85, 85, 85]
lx = [78, 200, 320, 440]
ly = [250, 295, 170, 170]
bx = [78, 200, 320, 440]
by = [375, 375, 295, 250]
bbx = [78, 200, 320, 440]
bby = [465, 465, 465, 340]
firstcolumn = [170, 250, 375, 465]
secondcolumn = [85, 295, 375, 465]
thirdcolumn = [85, 170, 295, 375, 465]
fourthcolumn = [85, 170, 250, 340, 465]
instructions = False
dead = False

#arrow - redraws arrow on screen
#@param - none
#@return - none
def arrow():
    pygame.draw.polygon(screen, WHITE, ((ax, ay), (ax+20, ay+10), (ax, ay+20)))

#player - shows player's movements
#@param - none
#@return - none    
def player():
    if dead == True:
        pp = pp_dead
    else:
        if direction == "right":
            if right % 2 != 0 and right % 3 != 0 and right % 4 != 0:
                pp = pp_right_1
            elif right % 2 == 0:
                pp = pp_right_2
            elif right % 3 == 0:
                pp = pp_right_3
            if right % 4 == 0:
                pp = pp_right_4
        elif direction == "left":
            if left % 2 != 0 and left % 3 != 0 and left % 4 != 0:
                pp = pp_left_1
            elif left % 2 == 0:
                pp = pp_left_2
            elif left % 3 == 0:
                pp = pp_left_3
            if left % 4 == 0:
                pp = pp_left_4
        elif direction == "up":
            if up % 2 != 0 and up % 3 != 0 and up % 4 != 0:
                pp = pp_up_1
            elif up % 2 == 0:
                pp = pp_up_2
            elif up % 3 == 0:
                pp = pp_up_3
            if up % 4 == 0:
                pp = pp_up_4
        elif direction == "down":
            if down % 2 != 0 and down % 3 != 0 and down % 4 != 0:
                pp = pp_down_1
            elif down % 2 == 0:
                pp = pp_down_2
            elif down % 3 == 0:
                pp = pp_down_3
            if down % 4 == 0:
                pp = pp_down_4
        elif direction == "standfront":
            pp = pp_stand_front
    screen.blit(pp, (px, py))

#burgerTop - shows where burger top is
#@param - none
#@return - none    
def burgerTop():
    for i in range(0, 4):
        screen.blit(burgertop, (btx[i], bty[i]))

#green - shows where lettuce is
#@param - none
#@return - none        
def green():
    for i in range(0, 4):
        screen.blit(lettuce, (lx[i], ly[i]))

#patty - shows where patty is
#@param - bx (list), by (list)
#@return - none    
def patty():
    for i in range(0, 4):
        screen.blit(beef, (bx[i], by[i]))

#burgerBottom - shows where burger bottom is
#@param - none
#@return - none    
def burgerBottom():
    for i in range(0, 4):
        screen.blit(burgerbottom, (bbx[i], bby[i]))

#hotdog- shows where sausage is
#@param - none
#@return - none
def hotdog():
    for i in range(0, len(hdx)):
        if hddirection[i] == "right":
            hdp = hd_right_1
        elif hddirection[i] == "left":
            hdp = hd_left_1
        screen.blit(hdp, (hdx[i], hdy[i]))

#scoring - displays score on screen
#@param - scorenumbers (list)
#@return - none
def scoring(scorenumbers):
    thousands = score // 1000
    hundreds = (score % 1000)/100
    tens = (score % 100)/10
    if current == levelone:
        screen.blit(zero, (300, 20))
        screen.blit(zero, (240, 20))
        if tens == 5:
            screen.blit(scorenumbers[5], (285, 20))
        else:
            screen.blit(scorenumbers[0], (285, 20))
        for i in range(0, 10):
            if hundreds == i:
                screen.blit(scorenumbers[i], (270, 20))
        for i in range(0, 10):
            if thousands == i:
                screen.blit(scorenumbers[i], (255, 20))
    elif current == gameover or current == win:
        screen.blit(zero, (300, 300))
        screen.blit(zero, (240, 300))
        if tens == 5:
            screen.blit(scorenumbers[5], (285, 300))
        else:
            screen.blit(scorenumbers[0], (285, 300))
        for i in range(0, 10):
            if hundreds == i:
                screen.blit(scorenumbers[i], (270, 300))
        for i in range(0, 10):
            if thousands == i:
                screen.blit(scorenumbers[i], (255, 300))

#oneup - shows number of lives
#@param - none
#@return - none
def life():
    if lives == 0:
        screen.blit(zero, (85, 20))
    elif lives == 1:
        screen.blit(one, (85, 20))
    elif lives == 2:
        screen.blit(two, (85, 20))
    elif lives == 3:
        screen.blit(three, (85, 20))

#shaker - shows pepper shakers
#@param - scorenumbers (list)
#@return - none        
def shaker(scorenumbers):
    for i in range(0, (peppers*25 + 1), 25):
        screen.blit(pepper, (10, 600-i))
        if peppers == 1:
            screen.blit(scorenumbers[1], (500, 20))
        elif peppers == 0:
            screen.blit(scorenumbers[0], (500, 20))
    
#redraw_screen - redraws screen and controls all other functions
def redraw_screen():
    
    scorenumbers = [zero, one, two, three, four, five, six, seven, eight, nine]
    
    #filling colour of screen  
    screen.fill(BLACK)
    screen.blit(current, (0, 0))
    
    if current == title:
        arrow()
    elif current == levelone:
        burgerTop()
        green()
        patty()
        burgerBottom()
        player()
        hotdog()
        scoring(scorenumbers)
        life()
        shaker(scorenumbers)
    elif current == win:
        arrow()
        scoring(scorenumbers)
    elif current == gameover:
        arrow()
        scoring(scorenumbers)
        
    #updating
    pygame.display.update()
     
inPlay = True

print "2 Player not optional."
print "Hit ESC to end the program." 

while inPlay: 
    
    #deals with any keyboard options once program is run 
    #looks for the event (action of using keyboard) 
    pygame.event.get() 
    
    # get_pressed() method generates a True/False list for the 
    # status of all keys 
    keys = pygame.key.get_pressed()   
     
    #looks for escape to be pressed
    if keys[pygame.K_ESCAPE]:
        
        inPlay = False
        
    elif keys[pygame.K_SPACE]:
        
        if current == levelone:
            #peppers
            if peppers > 0:
                for i in range(0, len(hdx)):
                    if px > hdx[i] - 50 and px < hdx[i] + 50:
                        if py == hdy[i]:
                            peppers -= 1
                            hdy[i] = 700
                            score += 200
        else:
            #arrow shifting
            if ay == 360:
                ay += 50
            elif ay == 410:
                ay -= 50
        
    elif keys[pygame.K_RETURN] and (ay == 360):
        
        #restart game
        if current == title or current == gameover or current == win:
            current = start
            px = 290
            py = 445
            lives = 3
            burgertops = 0
            lettuces = 0
            beefs = 0
            burgerbottoms = 0
            score = 0
            peppers = 1
            hdx = [50, 50, 277, 158]
            hdy = [67, 361, 151, 193]
            btx = [78, 200, 320, 440]
            bty = [170, 85, 85, 85]
            lx = [78, 200, 320, 440]
            ly = [250, 295, 170, 170]
            bx = [78, 200, 320, 440]
            by = [375, 375, 295, 250]
            bbx = [78, 200, 320, 440]
            bby = [465, 465, 465, 340]        
            redraw_screen()
            pygame.time.delay(3000)
            current = levelone
        
    elif keys[pygame.K_RETURN] and (ay == 410):
        
        if current == title:
            #only print instructions once
            if instructions == False:
                print
                print "Objective:"
                print
                print "Get all burger parts down to plate by getting your character, Peter Pepper, to drop the burger parts by touching them."
                print "Avoid meeting a hot dog without proper protection from your one spray of pepper or else you will lose one of your 3 lives."
                print
                print "Instructions:"
                print
                print "After selecting a 1 Player game, you begin the level."
                print "To move right, left, up ladders, and down ladders, you use the arrow keys."
                print "To spray pepper at a hot dog, have a close proximity and press space."
                print "Burger parts that go down a floor - 50 points."
                print "Burger parts that get to the plate - 100 points"
                print "Crushing hot dogs with a burger part - 300 points"
                print "Spraying a hot dog with pepper - 200 points"
                print
                instructions = True
                
        elif current == gameover or current == win:
            inPlay = False
            print "Thanks for playing!"
            print
        
    elif keys[pygame.K_UP]:
        #all bottoms of ladders

        #bottom most left ladder
        if (px >= 35 and px <= 55 and py <= 445 and py >= 236):
            direction = "up"
            up += 1
            py -= speed
        #top most left ladder
        elif (px >= 35 and px <= 55 and py <= 151 and py >= 68):
            direction = "up"
            up += 1
            py -= speed
        #second to left ladder
        elif (px >= 155 and px <= 175 and py <= 445 and py >= 68):
            direction = "up"
            up += 1
            py -= speed
        #middle ladder
        elif (px >= 277 and px <= 297 and py <= 445 and py >= 68):
            direction = "up"
            up += 1
            py -= speed
        #second to right ladder
        elif (px >= 397 and px <= 417 and py <= 445 and py >= 68):
            direction = "up"
            up += 1
            py -= speed
        #bottom most right ladder
        elif (px >= 515 and px <= 535 and py <= 445 and py >= 320):
            direction = "up"
            up += 1
            py -= speed
        #top most right ladder
        elif (px >= 515 and px <= 535 and py <= 235 and py >= 68):
            direction = "up"
            up += 1
            py -= speed
            
    elif keys[pygame.K_DOWN]:
        #all tops of ladders
        
        #bottom most left ladder
        if (px >= 35 and px <= 55 and py < 445 and py >= 235):
            direction = "down"
            down += 1 
            py += speed
        #top most left ladder
        elif (px >= 35 and px <= 55 and py < 151 and py >= 67):
            direction = "down"
            down += 1 
            py += speed
        #second to left ladder
        elif (px >= 155 and px <= 175 and py < 445 and py >= 67):
            direction = "down"
            down += 1 
            py += speed
        #middle ladder
        elif (px >= 277 and px <= 297 and py < 445 and py >= 67):
            direction = "down"
            down += 1 
            py += speed
        #second to right ladder
        elif (px >= 397 and px <= 417 and py < 445 and py >= 67):
            direction = "down"
            down += 1 
            py += speed
        #bottom most right ladder
        elif (px >= 515 and px <= 535 and py < 445 and py >= 319):
            direction = "down"
            down += 1 
            py += speed
        #top most right ladder
        elif (px >= 515 and px <= 535 and py < 235 and py >= 67):
            direction = "down"
            down += 1 
            py += speed
            
    elif keys[pygame.K_RIGHT]:
        if py == 445:
            direction = "right"
            right += 1
            px += speed
        elif py == 235 and px <= 176:
            direction = "right"
            right += 1
            px += speed
        elif py == 67:
            direction = "right"
            right += 1
            px += speed
        #easier to go to first platform in middle of bottom most left ladder
        elif py >= 357 and py <= 365 and px <= 418:
            py = 361
            direction = "right"
            right += 1
            px += speed
        #easier to go to second platform in middle of second to most right ladder
        elif py >= 315 and py <= 323 and px >= 396:
            py = 319
            direction = "right"
            right += 1
            px += speed
        #easier to go to third platform in middle of second to most left ladder and middle ladder
        elif py >= 273 and py <= 281 and px >= 154 and px <= 418:
            py = 277
            direction = "right"
            right += 1
            px += speed
        #easier to go to fourth platform right in middle of second to most right ladder
        elif py >= 231 and py <= 239 and px >= 396:
            py = 235
            direction = "right"
            right += 1
            px += speed
        #easier to go to fifth platform in middle of second to most left ladder
        elif py >= 189 and py <= 197 and px >= 157 and px <= 300:
            py = 193
            direction = "right"
            right += 1
            px += speed
        #easier to go to sixth platform right in middle of middle ladder and second to most right ladder
        elif py >= 147 and py <= 155:
            if px <= 178 or px >= 277:
                py = 151
                direction = "right"
                right += 1
                px += speed
            
    elif keys[pygame.K_LEFT]:
        if py == 445:
            direction = "left"
            left += 1
            px -= speed
        elif py == 319 and px >= 396:
            direction = "left"
            left += 1
            px -= speed
        elif py == 235 and px >= 396:
            direction = "left"
            left += 1
            px -= speed
        elif py == 151 and px >= 277:
            direction = "left"
            left += 1
            px -= speed
        elif py == 67:
            direction = "left"
            left += 1
            px -= speed
        #easier to go to first platform in middle of second to most left ladder
        elif py >= 357 and py <= 365 and px <= 418:
            py = 361
            direction = "left"
            left += 1
            px -= speed
        #easier to go to third platform in middle of second to most right ladder
        elif py >= 273 and py <= 281 and px >= 154 and px <= 418:
            py = 277
            direction = "left"
            left += 1
            px -= speed
        #easier to go to fourth platform left in middle of second to most left ladder
        elif py >= 231 and py <= 239 and px <= 176:
            py = 235
            direction = "left"
            left += 1
            px -= speed
        #easier to go to fifth platform in middle of middle ladder
        elif py >= 189 and py <= 197 and px >= 157 and px <= 300:
            py = 193
            direction = "left"
            left += 1
            px -= speed
        #easier to go to sixth platform left in middle of second to most left ladder
        elif py >= 147 and py <= 155 and px <= 178:
            py = 151
            direction = "left"
            left += 1
            px -= speed
    
    #player platform restrictions
    #level 0
    if py == 445:
        if px <= 35:
            px = 36
        elif px >= 533:
            px = 532
    #level 1
    if py == 361 and px <= 418:
        if px <= 35:
            px = 36
        elif px >= 417:
            px = 416
    #level 2
    if py == 319 and px >= 396:
        if px <= 397:
            px = 398
        elif px >= 533:
            px = 532
    #level 3
    elif py == 277 and px >= 154 and px <= 418:
        if px <= 155:
            px = 156
        elif px >= 417:
            px = 416
    #level 4 left
    elif py == 235 and px <= 176:
        if px <= 35:
            px = 36
        elif px >= 175:
            px = 174
    #level 4 right
    elif py == 235 and px >= 396:
        if px <= 397:
            px = 398
        elif px >= 533:
            px = 532
    #level 5
    elif py == 193 and px >= 157 and px <= 300:
        if px <= 160:
            px = 161
        elif px >= 297:
            px = 296
    #level 6 left
    elif py == 151 and px <= 178:
        if px >= 175:
            px = 174
        elif px <= 35:
            px = 36
    #level 6 right
    elif py == 151 and px >= 277:
        if px <= 280:
            px = 281
        elif px >= 533:
            px = 532
    #level 7
    elif py == 67:
        if px <= 35:
            px = 36
        elif px >= 533:
            px = 532
    
    #hot dog platform restrictions horizontal
    for i in range(0, len(hdx)):
        #level 1
        if hdy[i] == 361 and hdx[i] <= 418:
            if hdx[i] <= 35:
                hddirection[i] = "right"
            elif hdx[i] >= 415:
                hddirection[i] = "left"
        #level 5
        elif hdy[i] == 193 and hdx[i] >= 157 and hdx[i] <= 300:
            if hdx[i] <= 160:
                hddirection[i] = "right"
            elif hdx[i] >= 297:
                hddirection[i] = "left"
        #level 6 right
        elif hdy[i] == 151 and hdx[i] >= 277:
            if hdx[i] <= 280:
                hddirection[i] = "right"
            elif hdx[i] >= 533:
                hddirection[i] = "left"
        #level 7
        elif hdy[i] == 67:
            if hdx[i] <= 35:
                hddirection[i] = "right"
            elif hdx[i] >= 533:
                hddirection[i] = "left"
                
    #hot dog movement
    for i in range(0, len(hdx)):
        if hddirection[i] == "right":
            hdx[i] += speed
        elif hddirection[i] == "left":
            hdx[i] -= speed
            
    #player enemy collision
    for i in range(0, len(hdx)):
        #can only kill peter pepper if they are on the same platform and touch each other
        if px >= hdx[i] - 8 and px <= hdx[i] + 14 and hdy[i] == py:
            lives -= 1
            dead = True
            redraw_screen()
            pygame.time.delay(1000) #pause for 1 second
            dead = False
            if lives > 0:
                px = 290
                py = 445
                direction = "standfront"
            else:
                current = gameover
    
    #first column burger part collisions
    if bty[0] == ly[0]:
        if ly[0] == firstcolumn[1]:
            ly[0] = firstcolumn[2]
            score += 50
            if hdx[1] >= lx[0] and hdx[1] <= lx[0] + 80:
                hdy[1] = 700
                score += 300
        elif ly[0] == firstcolumn[2]:
            ly[0] = firstcolumn[3]
            score += 50
        elif ly[0] == firstcolumn[3]:
            ly[0] = 525
            lettuces += 1
            score += 100
    if ly[0] == by[0]:
        if by[0] == firstcolumn[2]:
            by[0] = firstcolumn[3]
            score += 50
        elif by[0] == firstcolumn[3]:
            by[0] = 545
            beefs += 1
            score += 100
    if by[0] == bby[0]:
        bby[0] = 565
        burgerbottoms += 1
        score += 100
        
    #second column burger part collisions
    if bty[1] == ly[1]:
        if ly[1] == secondcolumn[1]:
            ly[1] = secondcolumn[2]
            score += 50
            if hdx[1] >= lx[1] and hdx[1] <= lx[1] + 80:
                hdy[1] = 700
                score += 300
        elif ly[1] == secondcolumn[2]:
            ly[1] = secondcolumn[3]
            score += 50
        elif ly[1] == secondcolumn[3]:
            ly[1] = 525
            lettuces += 1
            score += 100
    if ly[1] == by[1]:
        if by[1] == secondcolumn[2]:
            by[1] = secondcolumn[3]
            score += 50
        elif by[1] == secondcolumn[3]:
            by[1] = 545
            beefs += 1
            score += 100
    if by[1] == bby[1]:
        bby[1] = 565
        burgerbottoms += 1
        score += 100
        
    #third column burger part collisions
    if bty[2] == ly[2]:
        if ly[2] == thirdcolumn[1]:
            ly[2] = thirdcolumn[2]
            score += 50
        elif ly[2] == thirdcolumn[2]:
            ly[2] = thirdcolumn[3]
            score += 50
            if hdx[1] >= lx[2] and hdx[1] <= lx[2] + 80:
                hdy[1] = 700
                score += 300
        elif ly[2] == thirdcolumn[3]:
            ly[2] = thirdcolumn[4]
            score += 50
        elif ly[2] == thirdcolumn[4]:
            ly[2] = 525
            lettuces += 1
            score += 100
    if ly[2] == by[2]:
        if by[2] == thirdcolumn[2]:
            by[2] = thirdcolumn[3]
            score += 50
            if hdx[1] >= bx[2] and hdx[1] <= bx[2] + 80:
                hdy[1] = 700
                score += 300
        elif by[2] == thirdcolumn[3]:
            by[2] = thirdcolumn[4]
            score += 50
        elif by[2] == thirdcolumn[4]:
            by[2] = 545
            beefs += 1
            score += 100
    if by[2] == bby[2]:
        bby[2] = 565
        burgerbottoms += 1
        score += 100
        
    #fourth column burger part collisions
    if bty[3] == ly[3]:
        if ly[3] == fourthcolumn[1]:
            ly[3] = fourthcolumn[2]
            score += 50
        elif ly[3] == fourthcolumn[2]:
            ly[3] = fourthcolumn[3]
            score += 50
        elif ly[3] == fourthcolumn[3]:
            ly[3] = fourthcolumn[4]
            score += 50
        elif ly[3] == fourthcolumn[4]:
            ly[3] = 525
            lettuces += 1
            score += 100
    if ly[3] == by[3]:
        if by[3] == fourthcolumn[2]:
            by[3] = fourthcolumn[3]
            score += 50
        elif by[3] == fourthcolumn[3]:
            by[3] = fourthcolumn[4]
            score += 50
        elif by[3] == fourthcolumn[4]:
            by[3] = 545
            beefs += 1
            score += 100
    if by[3] == bby[3]:
        bby[3] = 565
        burgerbottoms += 1
        score += 100
    
    #player collision with burger on level 0    
    if py == 445:
        for i in range(0, 4):
            if px >= bbx[i] and px <= bbx[i] + 80 and bby[i] == 465:
                bby[i] = 565
                burgerbottoms += 1
                score += 100
            elif px >= bx[i] and px <= bx[i] + 80 and by[i] == 465:
                by[i] = 545
                beefs += 1
                score += 100
            elif px >= lx[i] and px <= lx[i] + 80 and ly[i] == 465:
                ly[i] = 525
                lettuces += 1
                score += 100
            elif px >= btx[i] and px <= btx[i] + 78 and bty[i] == 465:
                bty[i] = 505
                burgertops += 1
                score += 100

    #player collision with burger on level 1                         
    elif py == 361:
        for i in range(0, 3):
            if px >= bx[i] and px <= bx[i] + 80 and by[i] == 375:
                by[i] = 465
                score += 50
            elif px >= lx[i] and px <= lx[i] + 80 and ly[i] == 375:
                ly[i] = 465
                score += 50
            elif px >= btx[i] and px <= btx[i] + 78 and bty[i] == 375:
                bty[i] = 465
                score += 50
                
    #player collision with burger on level 2            
    elif py == 319:
        if px >= bbx[3] and px <= bbx[3] + 80 and bby[3] == 340:
            bby[3] = 465
            score += 50
        elif px >= bx[3] and px <= bx[3] + 80 and by[3] == 340:
            by[3] = 465
            score += 50
        elif px >= lx[3] and px <= lx[3] + 80 and ly[3] == 340:
            ly[3] = 465
            score += 50
        elif px >= btx[3] and px <= btx[3] + 78 and bty[3] == 340:
            bty[3] = 465
            score += 50
    
    #player collision with burger on level 3
    elif py == 277:
        if px >= bx[2] and px <= bx[2] + 80 and by[2] == 295:
            by[2] = 375
            score += 50
            if hdx[1] >= bx[2] and hdx[1] <= bx[2] + 80:
                hdy[1] = 700
                score += 300
        for i in range(1, 3):
            if px >= lx[i] and px <= lx[i] + 80 and ly[i] == 295:
                ly[i] = 375
                score += 50
                if hdx[1] >= lx[i] and hdx[1] <= lx[i] + 80:
                    hdy[1] = 700
                    score += 300
            elif px >= btx[i] and px <= btx[i] + 78 and bty[i] == 295:
                bty[i] = 375
                score += 50
                if hdx[1] >= btx[i] and hdx[1] <= btx[i] + 80:
                    hdy[1] = 700
                    score += 300
    
    #player collision with burger on level 4            
    elif py == 235:
        #left side
        if px >= lx[0] and px <= lx[0] + 80 and ly[0] == 250:
            ly[0] = 375
            score += 50
            if hdx[1] >= lx[0] and hdx[1] <= lx[0] + 80:
                hdy[1] = 700
                score += 300
        elif px >= btx[0] and px <= btx[0] + 78 and bty[0] == 250:
            bty[0] = 375
            score += 50
            if hdx[1] >= btx[0] and hdx[1] <= btx[0] + 80:
                hdy[1] = 700
                score += 300
        #right side
        elif px >= bx[3] and px <= bx[3] + 80 and by[3] == 250:
            by[3] = 340
            score += 50
        elif px >= lx[3] and px <= lx[3] + 80 and ly[3] == 250:
            ly[3] = 340
            score += 50
        elif px >= btx[3] and px <= btx[3] + 78 and bty[3] == 250:
            bty[3] = 340
            score += 50

    #player collision with burger on level 5
    elif py == 193:
        if px >= btx[1] and px <= btx[1] + 78 and bty[1] == 210:
            bty[1] = 295
            score += 50
    
    #player collision with burger on level 6
    elif py == 151:
        #left side
        if px >= btx[0] and px <= btx[0] + 78 and bty[0] == 170:
            bty[0] = 250
            score += 50
        #second to right side
        elif px >= lx[2] and px <= lx[2] + 80 and ly[2] == 170:
            ly[2] = 295
            score += 50
        elif px >= btx[2] and px <= btx[2] + 78 and bty[2] == 170:
            bty[2] = 295
            score += 50
        #right side
        elif px >= lx[3] and px <= lx[3] + 80 and ly[3] == 170:
            ly[3] = 250
            score += 50
        elif px >= btx[3] and px <= btx[3] + 78 and bty[3] == 170:
            bty[3] = 250
            score += 50
    
    #player collision with burger on level 7        
    elif py == 67:
        #second to left side
        if px >= btx[1] and px <= btx[1] + 78 and bty[1] == 85:
            bty[1] = 210
            score += 50
            if hdx[3] >= btx[1] and hdx[3] <= btx[1] + 80:
                hdy[3] = 700
                score += 300
        for i in range (2, 4):
            #second to right side and right side
            if px >= btx[i] and px <= btx[i] + 78 and bty[i] == 85:
                bty[i] = 170
                score += 50
                if hdx[2] >= btx[i] and hdx[2] <= btx[i] + 80:
                    hdy[2] = 700
                    score += 300
    
    #winning conditions            
    if burgerbottoms == 4 and beefs == 4 and lettuces == 4 and burgertops == 4:
        current = win
            
    redraw_screen()
                      
# the screen window must be constantly redrawn - animation 
    pygame.time.delay(2)
# pause for 2 miliseconds 
#---------------------------------------#                        
pygame.quit()                           # always quit pygame when done!