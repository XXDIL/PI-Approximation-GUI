from turtle import *
import random
from tqdm import tqdm

# HEIGHT = 350
# WIDTH = 350
# screen = Screen()
# screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
# screen.setworldcoordinates(-WIDTH, -HEIGHT, WIDTH, HEIGHT)
r = 300


# Making the circle and the square
t = Turtle()
t.speed(0)

t.up()
t.goto(0, -r)
t.down()

t.pensize(2)
t.circle(r)

t.up()
t.goto(-r, -r)
t.down()

for _ in range(4):
 	t.forward(2*r) # Forward turtle by 2*r units
 	t.left(90)

t.up()


# PI approximation code
tracer(3000, 0)
# tracer(0, 0)
countI = 0
n = 300000
p = Turtle() # point turtles
p.hideturtle()
for i in tqdm(range(n)):

	x = random.uniform(-r, r)
	y = random.uniform(-r, r)

	R = (x*x + y*y)**(1/2);

	if(R <= 300):
		countI+=1
		p.up()
		p.goto(x, y)
		p.down()
		p.dot(2, 'lime')
		continue
	
	p.up()
	p.goto(x, y)	
	p.down()
	p.dot(2, 'red')
	
t = Turtle()
t.speed(0)

t.up()
t.goto(0, -r)
t.down()

t.pensize(2)
t.circle(r)

t.up()
t.goto(-r, -r)
t.down()

for _ in range(4):
 	t.forward(2*r) # Forward turtle by s units
 	t.left(90)

print("PI = ", end = '')
print(countI/n * 4)

done()

''' PI = 3.14159 ''' 