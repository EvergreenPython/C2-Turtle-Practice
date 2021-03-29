import turtle 

# Ask the user how many sides they want for the polygon
# Create the polygon based on the user input 
# Error checking, to make sure the user's input is greater than 3 and less than 10 

turtle.shape("turtle")


whileLoop = True 
while(whileLoop == True): 
  userInput = int(input("How many sides do you want?: "))
  if(userInput >= 3 and userInput <= 10): 
    whileLoop = False 
  else: 
    print("Error: That's not the correct number of sides.")
  


while(userInput > 10 or userInput < 3): 
  userInput = int(input("You need more than 3 sides but less than 10"))

for i in range(userInput): 
    turtle.forward(100)
    turtle.right(360/userInput)