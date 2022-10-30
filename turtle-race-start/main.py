from turtle import Turtle, Screen   # turtle, library; Turtle class
import random    # random是standard library
import time

screen = Screen()

screen.setup(width=600, height=400)    # 調整畫面大小
background = Turtle(shape="square")    # 調整背景大小
background.shapesize(stretch_wid=20, stretch_len=30)
background.color("forestgreen")        # 調整背景顏色
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: (red、orange、purple、yellow)")   # 跳出視窗
colors = ["red", "orange", "purple", "yellow", "blue"]    # 看要設定幾隻烏龜
all_turtle = []

for block_index in range(10):           # 終點線黑色部分
    end_line = Turtle(shape="square")
    end_line.color("black")
    end_line.shapesize(stretch_wid=0.9)
    end_line.penup()
    end_line.speed(0)
    end_line.goto(x=280, y=-175 + block_index * 40)

for block_index in range(9):            # 終點線白色部分
    end_line = Turtle(shape="square")
    end_line.color("white")
    end_line.shapesize(stretch_wid=0.9)
    end_line.penup()
    end_line.speed(0)
    end_line.goto(x=280, y=-155 + block_index * 40)

for turtle_index in range(0, 5):    # 看要設定幾隻烏龜
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-280, y=-(len(colors)-1) * 20 + turtle_index * 40)
    all_turtle.append(new_turtle)

staring_line = Turtle(shape="circle")    # 畫起跑線
staring_line.hideturtle()
staring_line.width(5)
staring_line.penup()
staring_line.setx(-260)
staring_line.sety(-150)
staring_line.pendown()
staring_line.goto(x=-260, y=150)
staring_line.write(arg="Starting line", font=("Verdana", 14, "normal"))


def draw_racetracks(num):                          # 依照烏龜數量畫賽道
    for i in range(0, 15):
        racetracks = Turtle(shape="square")
        racetracks.color("white")
        racetracks.shapesize(stretch_len=1.2, stretch_wid=0.2)
        racetracks.penup()
        racetracks.speed(0)
        racetracks.goto(x=-240 + i * 35, y=-len(all_turtle) * 20 + num * 40)


for j in range(0, len(all_turtle) + 1):            # 賽道位置
    draw_racetracks(j)


count_down = Turtle()                    # 倒數計時
count_down.penup()
count_down.goto(x=-10, y=-30)
count = 3
while count > 0:
    count_down.hideturtle()
    count_down.write(arg=count, align="center", font=("Verdana", 80, "normal"))
    time.sleep(1)
    count_down.clear()
    count -= 1

slogan = Turtle()                         # GO!
slogan.hideturtle()
slogan.penup()
slogan.goto(x=-10, y=-30)
slogan.write(arg="GO!", align="center", font=("Verdana", 80, "normal"))
time.sleep(1)
slogan.clear()

is_race_on = True

while is_race_on == True:          # 是否要繼續跑
    for turtle in all_turtle:
        if turtle.xcor() > 250:    # 到終點
            count += 1
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"The {winning_color} turtle is the winner.")
            else:
                print(f"The {winning_color} turtle is the winner.")

        rand_distance = random.randint(0, 10)   # 一次走多少
        turtle.forward(rand_distance)

screen.exitonclick()
