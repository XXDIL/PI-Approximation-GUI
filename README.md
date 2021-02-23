# PI-Approximation-GUI

### How Do We Calculate the Value of π Using Random Numbers?

This is a really interesting problem to think that randomness can get us the value of a well known constant π. To understand this better i'll have to get into what a Monte Carlo Simulation is. It can be thought of as computational algorithms that enable us to model probabilities that are difficult to calculate. This is done by using repeated random sampling to our advantage. With random sampling, the data we are using has no bias so we can simulate situations where the probabilities we obtain are close to the actual value. The more random data we use, the closer we get to the true value. Monte Carlo Simulations find their use in various fields, like Finance, Telecommunications and much more, but here I will analyze the use of a simple Monte Carlo Simulation to calculate the value of π (pi).

More on this here : [Monte Carlo Simulation](https://www.investopedia.com/terms/m/montecarlosimulation.asp)

------

### Basic Concept :

The whole process revolves around a basic idea of area of a circle and area of a square. Imagine a square now imagine a circle incribed in the square. like the image below :

<img src="https://user-images.githubusercontent.com/66634743/108888475-f4a0a100-7624-11eb-95c9-80451cb58b0e.png" height=400 width=400>

For the sake of simplicity we assume the **radius of the circle = 1**, So naturally a side of the **square will be = 2**

`Area of a circle = π*r*r` and `Area of a square = 4*r*r`.

Now lets take their ratio : `Area of a circle / Area of a square  =  π / 4`.

As we can see the radius cuts out, so this ratio does not depend on the radius of the circle.(ie we can take any size circle)


Now the main question arises that, how can we obtain the area of the circle and square?

How about a naive approach of filling the circle with small points and similarly with the square. That could work. Infact thats precicely why we be using the random number generator. generate 2 values one for x coordinate and the other for the y coordinate. There you go, you now have a point. Like the following image.

<img src = "https://user-images.githubusercontent.com/66634743/108888483-f66a6480-7624-11eb-9ad2-a1f3bdf33e75.png" height=400 width=400>

We assume that the area of each point is 1 unit. If we generate millions of such points we will be able to precicely find  the area of the circle and the square.

------

### Specifics

Now that we understand the basic working of the area calculation we can now quantify the areas as follows

`Area of circle = number of points in the circle`

`Area of square = number of points in total`

Therefore : `π =  4 * number of points in the circle / number of points in total`

How can we say that a randomly generated point belongs inside the circle or outside ?

Simple take the distance from the center to the ponit. if its less than the radius of the circle it lies inside else it lies outside.

------

### Simulation

We now know everything to make this. I would highly recommend first trying this yourself. It will help a lot in undertstanding the basics.

The simulation is as follows:

![PI](https://user-images.githubusercontent.com/66634743/108892390-3d5a5900-7629-11eb-8845-7a2a79a2432b.gif)

------

### Huge thanks to:

#### 1) [YT - Video](https://www.youtube.com/watch?v=pvimAM_SLic)
#### 2) [Joma Tech](https://www.youtube.com/channel/UCV0qA-eDDICsRR9rPcnG7tw)
#### 3) [Microsoft OMP - Slide 62](https://www.openmp.org/wp-content/uploads/omp-hands-on-SC08.pdf)









