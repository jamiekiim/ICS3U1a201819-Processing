page = 0 
keyboard = 0

def setup():
    global back_img0
    global back_img1
    global back_img2
    global back_img3 
    global back_img4
    global back_img5
    global back_img6
    global back_img7
    global back_img8
    global back_img9
    global back_img10
    global back_img11
    global back_img12
    
    size(915, 600)
    back_img0 = loadImage("entrance.jpg") #entrance
    back_img1 = loadImage("locker.jpg") #locker
    back_img2 = loadImage("com.jpg") #computer room
    back_img3 = loadImage("lowerstairs.jpg") #lower stairs
    back_img4 = loadImage("upperstairs.jpg") #upper stairs
    back_img5 = loadImage("classroom.jpg") #classroom
    back_img6 = loadImage("storage.jpg") #storage
    back_img7 = loadImage("office.jpg") #teacher's office
    back_img8 = loadImage("hallway.jpg") #hallway
    back_img9 = loadImage("washroom.jpg") #washroom
    back_img10 = loadImage("lowerladder.jpg") #lower ladder
    back_img11 = loadImage("upper.ladder.jpg") #upper ladder
    back_img12 = loadImage("exit.jpg") # exit
    

def draw():
    if page == 0: 
        background(back_img0)
    elif page == 1: 
        background(back_img1)
    elif page == 2: 
        background(back_img2)
    elif page == 3: 
        background(back_img3) 
    elif page == 4: 
        background(back_img4) 
    elif page == 5: 
        background(back_img5) 
    elif page == 6: 
        background(back_img6) 
    elif page == 7: 
        background(back_img7) 
    elif page == 8: 
        background(back_img8) 
    elif page == 9: 
        background(back_img9)
    elif page == 10: 
        background(back_img10)
    elif page == 11: 
        background(back_img11)
    elif page == 12: 
        background(back_img12)
    
def keyPressed():
    global page 
    page += 1
    if page == 13:
        page = 0
