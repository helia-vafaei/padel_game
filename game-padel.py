import turtle
import math
import time
import random

def init_screen():    
    w = turtle.Screen()
    w.clear()
    w.title("padel game")
    w.bgcolor("pink")
    w.setup(width=500,height=530)
    w.tracer(0,0)
    return w

def init_padel():
    global t3
    t3 = turtle.Turtle()
    t3.speed(0)
    t3.shape("square")
    t3.color("purple")
    t3.penup()
    t3.shapesize(0.7,3)
    t3.goto(0 , -220)
    t3.direction = "istadeh"
    return t3



def ball():
    global high_score
    global score
    global t1
    t1 = turtle.Turtle()
    t1.speed(0)
    t1.shape("circle")
    t1.color("black")
    t1.penup()
    t1.shapesize(0.9,0.9)
    t1.goto(0 , -203)
    scrn.update()  
    update_score()
    x = 0
    y = -203
    theta = 45
    v0 = 0.5
    t1.penup()
    vx = v0 * math.cos ( theta * math.pi/180 )
    vy = v0 * math.sin ( theta * math.pi/180 )
    t = 0
    scrn.update()
    while True:
        x = x +vx * t
        y = vy * t + y
        t1.setpos(x,y)
        t = t + 0.001
        scrn.update()
        if int(x) > 230 or int(x) < -230:  
            vx = -vx            
            scrn.update()
        if int(y) > 230 :  
            vy = -vy            
            scrn.update()    
        for j in range(21):            
            (x1,y1) = saghf1[j].position()            
            if (x1<x and x<x1+70) and (y1<y and y<y1+30):
                saghf1[j].penup()    
                saghf1[j].setpos(1000,1000)                
                vy = -vy             
                score=score + 10
                update_score()        
                scrn.update()             
            (x2,y2) = t3.position()    
        if (x2<x and x<x2+75) and (y2<y and y<y2+16):        
            vy = -vy    
            scrn.update()
        if int(y) < -245:
            if score > high_score:
                high_score = score
            score = 0
            update_score()
            reset_game()
            break  

def reset_game():
    head.goto(0 , -220)
    scrn.update()
    t1.goto(0 , -203)
    scrn.update()
    #saghf()
    


def go_right():
    head.forward(50)
    scrn.update()        

def go_left():
    head.forward(-50)
    scrn.update()

def set_random_color(n):
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    n.color(r,g,b)

def saghf():
    global saghf1   
    x = 210
    y = 250    
    saghf1 = [ ]    
    for l in range(3):
        y = y - 30 
        x = 210           
        for i in range(7):            
            t2 = turtle.Turtle() 
            turtle.colormode(255)               
            set_random_color(t2)            
            scrn.update()
            t2.speed(0)
            t2.shape("square")        
            t2.penup()
            t2.shapesize(1.3,3.3)          
            t2.setpos(x,y)                
            t2.pendown()                                
            scrn.update()
            saghf1.append(t2)
            x = x - 70
    return t2 


def update_score():
    score_writer.undo()
    score_writer.hideturtle()
    score_writer.goto(130,-250 )
    s = "Score: {} High Score: {}".format(score, high_score)
    score_writer.write(s, align="center", font=("Courier", 12, "normal"))     
                    
def init_score_writer():
    pen = turtle.Turtle()                              
    pen.speed(0)
    pen.shape("square")
    pen.color("blue")
    pen.penup()    
    scrn.update()
    pen.hideturtle()
    return pen

score = 0
high_score = 0
time.sleep(0.1)
while True:
    scrn = init_screen()
    #scrn.clear()
    head = init_padel()
    score_writer = init_score_writer()
    saghf()
    win= turtle.Screen()
    win.listen()
    win.onkey(go_right,"Right") 
    win.onkey(go_left,"Left")
    ball()
    update_score()
    scrn.update()
    #time.sleep(0.1)
turtle.mainloop()
    



