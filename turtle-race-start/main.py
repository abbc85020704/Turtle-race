from turtle import Turtle, Screen   # turtle, module; Turtle class
import random    # random是standard library
import time

screen = Screen()

screen.setup(width=600, height=400)    # 調整畫面大小
background = Turtle(shape="square")
background.shapesize(stretch_wid=20, stretch_len=30)
background.color("forestgreen")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: (red、orange、purple、yellow)")   # 跳出視窗
colors = ["red", "orange", "purple", "yellow"]   # 幾隻
all_turtle = []

for block_index in range(10):
    end_line = Turtle(shape="square")
    end_line.color("black")
    end_line.shapesize(stretch_wid=0.9)
    end_line.penup()
    end_line.speed(0)
    end_line.goto(x=280, y=-175 + block_index * 40)

for block_index in range(9):
    end_line = Turtle(shape="square")
    end_line.color("white")
    end_line.shapesize(stretch_wid=0.9)
    end_line.penup()
    end_line.speed(0)
    end_line.goto(x=280, y=-155 + block_index * 40)

for turtle_index in range(0, 4):    # 幾隻
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-280, y=-60 + turtle_index * 40)
    all_turtle.append(new_turtle)

staring_line = Turtle(shape="circle")
staring_line.hideturtle()
staring_line.width(5)
staring_line.penup()
staring_line.setx(-260)
staring_line.sety(-150)
staring_line.pendown()
staring_line.goto(x=-260, y=150)
staring_line.write(arg="Starting line", font=("Verdana", 14, "normal"))

count_down = Turtle()
count_down.penup()
count_down.goto(x=-10, y=-30)
count = 3
while count > 0:
    count_down.hideturtle()
    count_down.write(arg=count, align="center", font=("Verdana", 80, "normal"))
    time.sleep(1)
    count_down.clear()
    count -= 1

slogan = Turtle()
slogan.hideturtle()
slogan.penup()
slogan.goto(x=-10, y=-30)
slogan.write(arg="GO!", align="center", font=("Verdana", 80, "normal"))
time.sleep(1)
slogan.clear()

is_race_on = True

while is_race_on == True:
    for turtle in all_turtle:
        if turtle.xcor() > 250:    # 到終點
            count += 1
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"The {winning_color} turtle is the winner.")
            else:
                print(f"The {winning_color} turtle is the winner.")

        rand_distance = random.randint(0, 8)
        turtle.forward(rand_distance)

screen.exitonclick()
