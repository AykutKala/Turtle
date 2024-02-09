import turtle

colors_turtle = ['red', 'purple','white', 'blue', 'green', 'orange', 'yellow']
t = turtle.Turtle()
#t = turtle.Pen()
turtle.bgcolor('black')

for i in range(360):
    t.color(colors_turtle[i % 7])
    
    t.width(i // 100 + 1)
    t.left(144)
    t.forward(i)
    

#turtle.done()
turtle.mainloop()
