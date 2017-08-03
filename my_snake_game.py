import turtle
import random

turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y)

turtle.penup()

SQUARE_SIZE=20
START_LENGTH=1

score_list=[]
pos_list=[]
stamp_list=[]
food_pos=[]
food_stamps=[]
snake= turtle.clone()
snake.shape('square')
UP_ARROW='Up'
LEFT_ARROW='Left'
DOWN_ARROW='Down'
RIGHT_ARROW='Right'
TIME_STEP=100

SPACEBAR='space'
score=0
UP=0
LEFT=2
DOWN=1
RIGHT=3

turtle.hideturtle()

for i in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos= snake.pos()[1]
    x_pos+=SQUARE_SIZE

    my_pos=(x_pos,y_pos)
    snake.goto(x_pos, y_pos)
    pos_list.append(x_pos)
    a=snake.stamp()
    stamp_list.append(a)


food=turtle.clone()
food.shape('turtle')



food.hideturtle()


direction= 0
UP_EDGE=250
DOWN_EDGE=-250
RIGHT_EDGE=400
LEFT_EDGE= -400
def up():
    global direction
    if direction!= DOWN:
        direction=UP
    print("you pressed the up key")

def down():
    global direction
    if direction!= UP:
        direction=DOWN
    print("you pressed the down key")
     

def left():
    global direction
    if direction!= RIGHT:
        direction=LEFT
    print("you pressed the left key")

def right():
    global direction
    if direction!= LEFT:
        direction=RIGHT
    print("you pressed the right key")

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()

def move_snake():
    global score
    my_pos= snake.pos()
    x_pos= my_pos[0]
    y_pos= my_pos[1]

    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print('you moved right')

    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print('you moved left')
    elif direction==UP:
        snake.goto(x_pos,  y_pos + SQUARE_SIZE)
        print('you moved up')
    elif direction==DOWN:
        snake.goto(x_pos,y_pos - SQUARE_SIZE )
        print('you moved down')
    
    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp=snake.stamp()
    stamp_list.append(new_stamp)

    if snake.pos() in pos_list[0:-1]:
        quit()

    
    global food_stamps, food_pos
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])

        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print('You have eaten the food!')
        make_food()
        
        b=snake.stamp()
        pos_list.append(b)
        stamp_list.append(b)

                
        
        turtle.clear()
        score= score + 1
        score_list.append(score)
        turtle.goto(-SIZE_X/2+17, SIZE_Y/2-18
                    )
        turtle.write('score =' +str(score))
        

    new_pos= snake.pos()
    new_x_pos=new_pos[0]
    new_y_pos= new_pos[1]
    if new_x_pos>= RIGHT_EDGE:
        print('you hit the right edge! GAME OVER!')
        quit()
    if new_x_pos<= LEFT_EDGE:
        print('you hit the left edge! GAME OVER!')
        quit()
    if new_y_pos>= UP_EDGE:
        print('you hit the yp edge! GAME OVER')
        quit()
    if new_y_pos<= DOWN_EDGE:
        print('u  hit the down edge! GAME OVER!')
        quit()

    old_stamp= stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)
    turtle.ontimer(move_snake,TIME_STEP)
move_snake()


def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    food_x= random.randint(min_x, max_x) *SQUARE_SIZE
    food_y= random.randint(min_y, max_y) *SQUARE_SIZE
    
    food.goto(food_x, food_y)
    c=(food_x, food_y)
    food_pos.append(c)
    xfoodx= food.stamp()
    food_stamps.append(xfoodx)

make_food()

edges=turtle.clone()
edges.pu
edges.goto(-385,245)
edges.pd()
edges.goto(385, 245)
edges.goto(385,-245)
edges.goto(-385,-245)
edges.goto(-385, 245)
edges.goto(-385,-245)

