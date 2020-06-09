import turtle
abel = turtle.Pen()
abel.speed(100)
turtle.bgcolor("black")
sides = eval(input("Enter a number of sides between 2 and 6: "))
colors = ["red", "yellow", "blue", "orange", "green", "purple"]
for x in range (360):
  abel.pencolor(colors[x%sides])
  abel.forward(x * 3/sides + x)
  abel.left(360/sides + 1)
  abel.width(x*sides/200)