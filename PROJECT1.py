from KoshyFunctions import*
turtle.colormode(255)
bob.width(10)
bob.speed(0)

x = -500
y = 400
jump(x,y)
for times in range(255):
    c = (times,136,136)
    bob.color(c)
    bob.forward(1000)
    jump(x,y-times*4)

bob.width(1)

#1
jump(380,380)
for times in range(255):
    bob.color(255,times,150)
    bob.circle(50)
    bob.left(19)
jump(340,340)
for times in range(255):
    bob.color(150,255,times)
    bob.circle(50)
    bob.left(19)
jump(300,300)
for times in range(255):
    bob.color(times,150,255)
    bob.circle(50)
    bob.left(19)
#2
jump(260,260)
for times in range(255):
    bob.color(210,times,2)
    bob.circle(50)
    bob.left(19)
jump(220,220)
for times in range(255):
    bob.color(2,210,times)
    bob.circle(50)
    bob.left(19)
jump(180,180)
for times in range(255):
    bob.color(times,2,210)
    bob.circle(50)
    bob.left(19)
#3
jump(140,140)
for times in range(255):
    bob.color(0,times,0)
    bob.circle(50)
    bob.left(19)
jump(100,100)
for times in range(255):
    bob.color(200,25,times)
    bob.circle(50)
    bob.left(19)
jump(60,60)
for times in range(255):
    bob.color(times,90,200)
    bob.circle(50)
    bob.left(19)
#4
jump(20,20)
for times in range(255):
    bob.color(7,times,160)
    bob.circle(50)
    bob.left(19)
jump(-20,-20)
for times in range(255):
    bob.color(160,7,times)
    bob.circle(50)
    bob.left(19)
jump(-60,-60)
for times in range(255):
    bob.color(times,160,7)
    bob.circle(50)
    bob.left(19)
#5
jump(-100,-100)
for times in range(255):
    bob.color(255,times,30)
    bob.circle(50)
    bob.left(19)
jump(-140,-140)
for times in range(255):
    bob.color(30,255,times)
    bob.circle(50)
    bob.left(19)
jump(-180,-180)
for times in range(255):
    bob.color(times,30,255)
    bob.circle(50)
    bob.left(19)
#6
jump(-220,-220)
for times in range(255):
    bob.color(35,times,35)
    bob.circle(50)
    bob.left(19)
jump(-260,-260)
for times in range(255):
    bob.color(30,35,times)
    bob.circle(50)
    bob.left(19)
jump(-300,-300)
for times in range(255):
    bob.color(times,35,30)
    bob.circle(50)
    bob.left(19)
#7
jump(-340,-340)
for times in range(255):
    bob.color(25,times,0)
    bob.circle(50)
    bob.left(19)
jump(-380,-380)
for times in range(255):
    bob.color(0,25,times)
    bob.circle(50)
    bob.left(19)
jump(-420,-420)
for times in range(255):
    bob.color(times,0,25)
    bob.circle(50)
    bob.left(19)
#8

