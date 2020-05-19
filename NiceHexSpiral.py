#NiceHexSpiral.py
#Meu pai esta ensinando python
import turtle
colors=['white', 'purple', 'blue', 'green', 'yellow', 'orange']
t=turtle.Pen()
turtle.bgcolor('black')
#Enter with the number of lines
lines = 360
for x in range(lines):
  t.pencolor(colors[x%6])
  t.width(x/100+1)
  t.forward(x)
  t.left(59)