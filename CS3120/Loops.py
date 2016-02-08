#!/usr/bin/python
#This program shows how if statements, for loops and while loops work
# This is and if statement
x = 5
if x > 0:
   pass
else:
   print("*")
   
   
#This is a for loop   
y=[1,2,3,4,5]
for index in range(len(y)):
   print(y[index])
   
print("\n")
   
#This is a while loop   
def whileLoop():
   x=5
   while x >= 0:
      print("*")
      x = x-1
   else:
      print("No more stars")

whileLoop()

