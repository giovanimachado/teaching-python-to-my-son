import turtle
giovana = turtle.Pen()
colors = ["red", "orange", "yellow", "green","blue", "violet"]
giovana.speed(10000)
turtle.bgcolor("black")
for x in range(1000):
  giovana.pencolor(colors[x%6])
  giovana.forward(x)
  giovana.left(91)