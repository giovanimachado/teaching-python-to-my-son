#NiceHexSpiral.py
#Meu pai esta ensinando python
import turtle
colors=['white', 'purple', 'blue', 'green', 'yellow', 'orange']
t=turtle.Pen()
turtle.bgcolor('black')
for x in range(1000):
  t.pencolor(colors[x%6])
  t.width(x/100+1)
  t.forward(x)
  t.left(59)