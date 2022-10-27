#////////////////////////////////////////////////////////////////////
# 10 pts
#Write a Python program to print the following string in a specific format (see the output).
print("Twinkle, twinkle, little star, \n        How I wonder what you are! \n              Up above the world so high, \n              Like a diamond in the sky. \nTwinkle, twinkle, little star, \n        How I wonder what you are")

#////////////////////////////////////////////////////////////////////
# 10 pts
# Write a Python program thataccepts the radius (any positive number) of a circle from the user and computesthe area. Use pi = 3.1416.
pi = 3.1416
    
radius = float(input("Enter a radius to compute it's area."))
if radius>=0:
    print((pi*(radius*radius)), "is the area of your input.")
else:
    print("Please only input positive numbers.")
  
#//////////////////////////////////////////////////////////////////// 
# 10 pts
#Write a Python program that accepts the radius (any positive number) of a sphere from the user and computesthe volume. Use pi = 3.1416.
pi = 3.1416

radius = float(input("Enter a radius to compute it's volume."))
if radius>=0:
    print((1.33*pi*(radius*radius*radius)), "is the volume of your input.")
else:
    print("Please only input positive numbers.")
  
#////////////////////////////////////////////////////////////////////
# 20 pts   
#Write a Python program that accepts threeunique positive integers from the user. Print the value of their sumif the inputs are unique. Otherwise, print "Please try again.".
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))

if x==y:
  print("Please try again")
elif z==x:
      print("Please try again")
elif y==z:
    print("Please try again")
else:
  print(x+y+z)
 
#////////////////////////////////////////////////////////////////////
# 20 pts
#Write a Python program that accepts threeunique positive integers from the user. Print the value of their sumif the inputs are unique. Otherwise, print "Please try again.".
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))

if x==y:
  print("Please try again")
elif z==x:
      print("Please try again")
elif y==z:
    print("Please try again")
else:
  print(x+y+z)
  
#////////////////////////////////////////////////////////////////////
# 30 pts
#Write a Python program that asks the user for their birth year, prints their age, and recommends a music genre.

year = int(input("What is your birth year?"))
age = 2022 - year

if year >= 1922 and year <= 1949:
    print("Your age is" , age , "; you might find Rap music interesting!")
elif year >= 1950 and year <= 1959:
    print("Your age is" , age , "; you might find Rap music interesting!")
elif year >= 1960 and year <= 1969:
    print("Your age is" , age , "; you might find Rap music interesting!")
elif year >= 1970 and year <= 1979:
    print("Your age is" , age , "; you might find Rap music interesting!")
elif year >= 1980 and year <= 1989:
    print("Your age is" , age , "; you might find Rap music interesting!")
elif year >= 1990 and year <= 1999:
    print("Your age is" , age , "; you might find Rap music interesting!")
elif year >= 2000 and year <= 2009:
    print("Your age is " , age , "; you might find Rap music interesting!")
else:
    print("Your age is" , age , "You may listen to any genre of music.")  
    
 #Lab Activty 10/27/2022
