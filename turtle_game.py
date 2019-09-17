import turtle


my_circle = turtle.Turtle()
my_circle.speed(10)
def circle(length,angle):
  for i in range(4):
    my_circle.forward(length)
    my_circle.right(angle)
  
  
for i in range(400000):
  circle(100,90)
  my_circle.right(10)

