from gpiozero import LED, LEDBoard
from time import sleep
from signal import pause


treevertical=[ 18, 5, 9, 11, 21, 10, 7, 12, 6, 1,14, 3, 20, 24, 13, 15,2, 17, 16, 23,8, 22, 4, 19 ]
treehorizontal=[ 4, 12, 18, 7, 21, 15, 22, 6, 16, 20, 11, 2, 19, 1, 10, 24, 14, 8, 13, 5, 23, 3, 9, 17 ]
treemap={ 1:4, 7:5, 16:6, 22:7, 6:8 , 14:9, 8:10, 21:11, 15:12, 3:13, 19:14, 2:15, 9:16, 10:17, 20:18, 18:19,17:20, 4:21, 24:22, 23:23, 13:24, 5:25, 12:26, 11:27 
}

starled=LED(2)
starstate=False
starblink=5
starcount=starblink

leds=LEDBoard(*range(4,28), pwm=True)

def toggleStar():
    global starstate,starcount
    starcount-=1
    if starcount==0:
        starcount=starblink
        starstate=not starstate
        if starstate:
            starled.on()
        else:
            starled.off()

def labelToPin(l):
	return treemap[l]

def toBoard(l):
    return labelToPin(l)-4
     
while True:    
    for i in treevertical:
        sleep(0.1)
        leds.on(toBoard(i))
        toggleStar()
    
    for i in treevertical:
        sleep(0.1)
        leds.off(toBoard(i))
        toggleStar()
        
    for i in treehorizontal:
        sleep(0.1)
        leds.on(toBoard(i))
        toggleStar()
        
    for i in treehorizontal:
        sleep(0.1)
        leds.off(toBoard(i))
        toggleStar()
        

    
