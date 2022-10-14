import badger2040
from random import randint
from time import sleep, time
#setup
badger = badger2040.Badger2040()
badger.update_speed(1)
score = 0
#-----------------------------------------------------------------
#clear command
def clr():
    badger.pen(15)
    badger.clear()
#-----------------------------------------------------------------
#SPALSH SCREEN
badger.pen(0)
badger.font("serif")
badger.text("Target Practice!", 10, 50, scale=1.0)
badger.update()
sleep(0.5)
badger.text("Press b to start!", 50, 80, scale=0.70)
badger.update()
while True:
    if badger.pressed(badger2040.BUTTON_B):
        clr()
        break
#SELECT TARGET REPETITION
turnCounter = 10 #number of targets that must be hit before the game finishes
badger.text("How many targets?", 10, 50, scale=1.0)

while True:
    if badger.pressed(badger2040.BUTTON_UP):
        turnCounter = turnCounter + 5
        badger.text(turnCounter, 50, 100, scale=0.70)
        badger.update()
        clr()
    if badger.pressed(badger2040.BUTTON_DOWN):
        turnCounter = turnCounter - 5
        badger.text(turnCounter, 50, 100, scale=0.70)
        badger.update()
        clr()
    if badger.pressed(badger2040.BUTTON_B):
        clr()
        break
#-----------------------------------------------------------------
#Font set
badger.font("bitmap8")
#-----------------------------------------------------------------
#Side Box
def rectangle():
    #badger.pen(8)
    #badger.rectangle(0, 0,100,128)
    badger.pen(0)
#-----------------------------------------------------------------
#Score box output
def scorebox(totalRounds,startTime, count):
    badger.pen(0)
    badger.font("serif")
    currentTime = time() - startTime
    badger.text("Remaining:", 2, 10, scale=0.60)
    badger.text(str((totalRounds - count)-1), 30, 30, scale=0.70)
    badger.text("Time:", 2, 70, scale=0.60)
    badger.text(str(currentTime) + "s", 30, 90, scale=0.70)
    badger.font("bitmap8")
#-----------------------------------------------------------------
#TARGET
#row 1
def target1():
    badger.pen(0)
    badger.text("----", 105, -17, scale=4.0)
    badger.text("| 0 |", 107, 5, scale=4.0)
    badger.text("----", 105, 20, scale=4.0)

def target2():
    badger.pen(0)
    badger.text("----", 170, -17, scale=4.0)
    badger.text("| 0 |", 172, 5, scale=4.0)
    badger.text("----", 170, 20, scale=4.0)

def target3():
    badger.pen(0)
    badger.text("----", 235, -17, scale=4.0)
    badger.text("| 0 |", 237, 5, scale=4.0)
    badger.text("----", 235, 20, scale=4.0)

#row 2
def target4():
    badger.pen(0)
    badger.text("----", 105, 27, scale=4.0)
    badger.text("| 0 |", 107, 49, scale=4.0)
    badger.text("----", 105, 64, scale=4.0)

def target5():
    badger.pen(0)
    badger.text("----", 170, 27, scale=4.0)
    badger.text("| 0 |", 172, 49, scale=4.0)
    badger.text("----", 170, 64, scale=4.0)

def target6():
    badger.pen(0)
    badger.text("----", 235, 27, scale=4.0)
    badger.text("| 0 |", 237, 49, scale=4.0)
    badger.text("----", 235, 64, scale=4.0)

#row 3
def target7():
    badger.pen(0)
    badger.text("----", 105, 71, scale=4.0)
    badger.text("| 0 |", 107, 93, scale=4.0)
    badger.text("----", 105, 108, scale=4.0)

def target8():
    badger.pen(0)
    badger.text("----", 170, 71, scale=4.0)
    badger.text("| 0 |", 172, 93, scale=4.0)
    badger.text("----", 170, 108, scale=4.0)

def target9():
    badger.pen(0)
    badger.text("----", 235, 71, scale=4.0)
    badger.text("| 0 |", 237, 93, scale=4.0)
    badger.text("----", 235, 108, scale=4.0)
#-----------------------------------------------------------------
#AIM
def aim1():
    badger.pen(0)
    badger.text("| x |", 107, 5, scale=4.0)

def aim2():
    badger.pen(0)
    badger.text("| x |", 172, 5, scale=4.0)

def aim3():
    badger.pen(0)
    badger.text("| x |", 237, 5, scale=4.0)

#row 2
def aim4():
    badger.pen(0)
    badger.text("| x |", 107, 49, scale=4.0)

def aim5():
    badger.pen(0)
    badger.text("| x |", 172, 49, scale=4.0)

def aim6():
    badger.pen(0)
    badger.text("| x |", 237, 49, scale=4.0)

#row 3
def aim7():
    badger.pen(0)
    badger.text("| x |", 107, 93, scale=4.0)

def aim8():
    badger.pen(0)
    badger.text("| x |", 172, 93, scale=4.0)

def aim9():
    badger.pen(0)
    badger.text("| x |", 237, 93, scale=4.0)
    
#-----------------------------------------------------------------
    
def targetOut():
    global target
    
    if target == 1:
        target1()
        print("targetout1")
    if target == 2:
        target2()
        print("targetout2")
        
    if target == 3:
        target3()
        print("targetout3")
        
    if target == 4:
        target4()
        print("targetout4")
        
    if target == 5:
        print("targetout5")
        target5()
        
    if target == 6:
        print("targetout6")
        target6()
        
    if target == 7:
        print("targetout7")
        target7()
        
    if target == 8:
        print("targetout8")
        target8()
        
    if target == 9:
        print("targetout9")
        target9()
        
def aimOut():
    global aim

    if aim == 1:
        aim1()
        print("aimout1")
        
    if aim == 2:
        aim2()
        print("aimout2")
        
    if aim == 3:
        aim3()
        print("aimout3")
        
    if aim == 4:
        aim4()
        print("aimout4")
        
    if aim == 5:
        print("aimout5")
        aim5()
        
    if aim == 6:
        print("aimout6")
        aim6()
        
    if aim == 7:
        print("aimout7")
        aim7()
        
    if aim == 8:
        print("aimout8")
        aim8()
        
    if aim == 9:
        print("aimout9")
        aim9()
            

def selectNumbers():
    global target, aim
    target = randint(1 , 9)
    aim = randint(1, 9)
    while target == aim:
        aim = randint(1, 9)
    print("target number", target)
    print("aim number", aim)

#main
badger.update_speed(2) #will help to clear display
turnCountConst = turnCounter
startTime = time() #starts stopwatch
while turnCounter > 1:
    clr()
    badger.update_speed(3) #mega speed
    selectNumbers()
    targetOut()
    aimOut()
    rectangle()
    scorebox(turnCountConst,startTime, score)
    badger.update()
    while target != aim:
        if badger.pressed(badger2040.BUTTON_A):
            clr()
            aim = aim - 1
            targetOut()
            aimOut()
            rectangle()
            scorebox(turnCountConst,startTime, score)
            badger.update()
            sleep(0.01)
        if badger.pressed(badger2040.BUTTON_C):
            clr()
            aim = aim + 1
            targetOut()
            aimOut()
            rectangle()
            scorebox(turnCountConst,startTime, score)
            badger.update()
            sleep(0.01)
        if badger.pressed(badger2040.BUTTON_UP):
            aim = aim - 3
            clr()
            targetOut()
            aimOut()
            rectangle()
            scorebox(turnCountConst,startTime, score)
            badger.update()
            sleep(0.01)
        if badger.pressed(badger2040.BUTTON_DOWN):
            aim = aim + 3
            clr()
            targetOut()
            aimOut()
            rectangle()
            scorebox(turnCountConst,startTime, score)
            badger.update()
            sleep(0.01)
        if aim > 9:
            aim = 1
            clr()
            targetOut()
            aimOut()
            rectangle()
            scorebox(turnCountConst,startTime, score)
            badger.update()
            sleep(0.01)
        if aim < 1:
            aim = 9
            clr()
            targetOut()
            aimOut()
            rectangle()
            scorebox(turnCountConst,startTime, score)
            badger.update()
            sleep(0.01)
    score = score + 1
    turnCounter = turnCounter - 1
    print("Score is", score)
    clr()
    
stopTime = time() #stop time
        

