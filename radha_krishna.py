import turtle

#keeping the background color dark blue
turtle.bgcolor('#ffc233')

#Defining title of program
turtle.title("Radhe Krishna")

#Creating turtle screen
screen= turtle.Screen()
#Defining height and width of screen
screen.setup(650,580)

t1 = turtle.Turtle()

#keeping the fasted speed for now, you can keep the speed as needed
#'fastest' : 0
#'fast' : 10
#'normal' : 6
#'slow' : 3
#'slowest' : 1

t1.speed(4)

#Let's move down and go the position from where we will start to draw
t1.right(90)
t1.pu()
t1.forward(180)
t1.left(90)
#Now, the turtle is pointing positive x-axis

#Let's keep the pen down and start to draw the base
t1.pd()
#Here we have dipped our turtle brush in a shade of blue color
t1.fillcolor("#ff99d1")
t1.begin_fill()
t1.forward(400)
t1.right(90)
t1.forward(100)
t1.right(90)
t1.forward(800)
t1.right(90)
t1.forward(100)
t1.right(90)
t1.forward(400)
t1.end_fill()
#Now, we have drawn the base which is rectangular in shape
#end_fill will fill blue color (selected above), in the shape formed by turtle

#Now, we will start to draw moon,I have selected a very light shade of blue to color moon
t1.fillcolor("#CDEEF1")
t1.begin_fill()
t1.forward(160)
t1.left(40)
#this method will draw the moon's border  
t1.circle(250,280)
t1.left(40)
t1.forward(160)
t1.end_fill()
#Now, we have drawn the moon as well as filled color in it

#Now, we will start drawing Radha Krishna
#We will draw Radha on our right side and Krishna on left side
#We will start with Radha
t1.fillcolor("#012427")
t1.begin_fill()
#We will start with the duppata
t1.forward(160)
t1.left(130)
t1.circle(-300,30)
t1.forward(95)
#This will draw the shoulder
t1.circle(50,40)
t1.right(40)
#This will draw the head
t1.forward(43)
t1.circle(80,25)
t1.circle(50,30)
t1.left(10)
t1.circle(35,28)
#Now, we have completed drawing Radha

#Now, let's draw krishna's turban
t1.right(160)
t1.circle(10,100)
t1.right(100)
t1.circle(10,80)
t1.forward(20)
t1.left(80)
t1.circle(100,15)
t1.right(90)
t1.forward(6)
t1.left(65)
t1.circle(60,55)

#Following code will draw Krishna's morpankh
t1.right(160)
t1.circle(20,100)
t1.forward(10)
t1.circle(-20,25)
t1.left(170)
t1.circle(-20,40)
t1.forward(10)
t1.circle(20,80)
#morpankh done

#We will continue to draw rest part of turban
t1.right(135)
t1.circle(60,15)
t1.left(70)
t1.forward(6)

t1.right(110)
t1.forward(9)

t1.left(80)
t1.circle(70,24)

t1.right(60)
t1.circle(65,30)
t1.circle(-5,110)

#Below lines of code will draw the right hand of Krishna
t1.circle(5,120)
t1.right(90)
t1.circle(5,60)
t1.forward(10)
t1.circle(10,5)
t1.right(80)
t1.forward(15)
t1.circle(-5,160)
#Now, we will draw the first open finger of right hand
t1.forward(6)
t1.circle(2,180)
t1.forward(6)
t1.circle(20,30)

#Below lines will draw fingers holding bansuri
t1.right(140)
t1.circle(3,150)
t1.right(110)
t1.circle(4,80)
t1.forward(2)
t1.right(100)

#Here, we will draw second open finger of krishna
t1.forward(6)
t1.right(60)
t1.forward(9)
t1.circle(2,180)
t1.forward(10)
t1.left(30)
t1.forward(15)

#We will now start to draw bansuri
t1.right(85)
t1.forward(40)
t1.right(60)
t1.circle(5,310)
t1.right(80)
t1.forward(3)
t1.right(90)

#dor on bansuri
t1.forward(42)
t1.right(30)
t1.forward(10)
t1.left(90)
t1.circle(20,60)
t1.left(95)
t1.forward(12)
t1.right(29)
t1.forward(42)

#We will draw the rest part of bansuri
t1.right(90)
t1.forward(34)
t1.right(85)

#left hand of Krishna
t1.forward(2)
t1.circle(60,25)

#Now, we will draw Krishna's duppata
t1.right(80)
t1.circle(10,40)
t1.forward(45)
t1.left(10)
t1.forward(130)

#Below lines will draw the plates of duppata
t1.left(90)
t1.forward(20)
t1.right(90)
t1.forward(10)
t1.left(90)
t1.forward(10)
t1.right(90)
t1.forward(5)
t1.left(90)
t1.forward(25)

#This will complete drawing duppata
t1.left(100)
t1.forward(120)

t1.right(175)
t1.circle(50,50)

#Now, we will tilt turtle towards required direction and draw Krishna's dhoti
t1.right(80)
t1.circle(110,15)
t1.forward(75)

#The turtle will now reach to the rectangular base we had drawn in the beginning
t1.left(97)
t1.forward(260)
t1.end_fill()
#At this point, we have completed drawing Radhe Krishna

t1.pu()
t1.right(100)
t1.forward(115)
t1.right(85)
t1.forward(420)

#Lets also write their holy name in our drawing 
t1.color("#00a606")
t1.write("Radha Krishna - Preetam ", font=("Harlow Solid Italic",45, "bold"))

t1.hideturtle()

turtle.done()