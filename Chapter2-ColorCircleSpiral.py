import turtle
carol= turtle.Pen()
carol.speed(100)
turtle.bgcolor("green")
colors = ["red", "yellow", "blue", "black"]
for x in range(1000):
  carol.pencolor(colors[x%4])
  carol.circle(x)
  carol.left(91)