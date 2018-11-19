'''
Draw a bullseye in the centre of the screen
'''

x = 0 

def setup():
    size(600, 330)
    noStroke()
    
def draw():
    global x 
    
    if x >= 600:
        x = 0
    x += 3
    
    background(66, 104, 165)
     
    drawCloud(x, 300)
    drawCloud(x, 200)
    drawCloud(x, 100)

def drawCloud(x, y):
    ellipse(x, y, 50, 50)
    ellipse(x+30, y, 50, 50)
    ellipse(x+10, y-20, 50, 50)
        

        
