x = 100
y = 100
a = 4
b = 2 
press = 0 
keyboard = 0 


def setup():
    global sat_img
    global back_img

    size(1200, 775)
    sat_img = loadImage("snowman.png")
    back_img = loadImage("snow_1.png")


def draw():
    background(back_img)
    
    global x
    global a
    global keyboard  
    
    if keyboard == 1: 
        if x > 1080 or x < 40: #cloud
            a = a*(-1)
        x += a 
    
    # cloud
    noStroke()
    fill(247, 247, 247)
    ellipse(x, height/7, 100, 100)
    ellipse(x+80, height/7, 100, 100)
    ellipse(x+30, height/7-40, 100, 100)
    
    #christmas tree
    fill(17, 104, 62)
    triangle(850, 730, 903, 400, 1000, 730)
    
    fill(109, 84, 9)
    rect(893, 730, 55, 55)

    global y 
    global b

    #snowman
    if press == 1: 
        if y > 500 or y < 60: 
            b = b*(-1)
        y += b 
    
    image(sat_img, y-50, 550, 250, 230) #snowman
    
    #text
    textSize(50)
    fill (191, 15, 62)
    text ("Merry Christmas!", 350, 100) 
    

def mousePressed ():
    global press
    press += 1
    if press == 2:
        press = 0 
    
def keyPressed (): 
    global keyboard
    keyboard += 1
    if keyboard == 2: 
        keyboard = 0 
  
    
