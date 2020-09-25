# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码

from turtle import *
def curvemove():
    for i in range(200):
        right(1)
        forward(1)
setup(600,600,400,400)
hideturtle()
pencolor('black')
fillcolor("red")
pensize(2)
begin_fill()
left(140)
forward(111.65)
curvemove()
left(120)
curvemove()
forward(111.65)
end_fill()
penup()
goto(-27, 85)
pendown()
done()
