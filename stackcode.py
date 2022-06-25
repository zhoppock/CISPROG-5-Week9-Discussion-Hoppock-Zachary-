import random

def stackCode():
  print("-----------------------------------")
  print(">>>> WELCOME TO THE STACK CODE <<<<")
  
  stack1 = []
  stack2 = []

  stack1.append(input("\nInput a character/number: "))

  while len(stack1) < 5:
    stack1.append(input("Input another character/number: "))

  print("\nThe main stack is:\n",stack1)

  print("\nWe will now add two more numbers of our own:")

  number1 = str(random.randint(0, 10))
  number2 = str(random.randint(0, 10))

  stack1.append(number1)
  stack1.append(number2)

  print(number1)
  print(number2)

  print("\nThe main stack is now:\n",stack1)

  print("\nWe will now take the last three items in the main stack and put them in a secondary stack in reverse order.")

  stack2.append(stack1.pop())

  stack2.append(stack1.pop())

  stack2.append(stack1.pop())

  print("\nThe main stack is now:\n",stack1)
  print("\nThe secondary stack is:\n",stack2)
