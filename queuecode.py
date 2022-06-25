from collections import deque

def queueCode():
  print("\n-----------------------------------")
  print(">>>> WELCOME TO THE QUEUE CODE <<<<")

  queue = []
  queue2 = ["Stephanie"]

  queue.append(input("\nInput a name: "))

  while len(queue) < 3:
    queue.append(input("Input another name: "))
  
  queue1 = deque(queue)
  print("\nOur current group consists of:\n", queue1)

  print("\nThe group will have two more joining:")
  print("Jason")
  print("Rebecca")
  queue1.append("Jason")
  queue1.append("Rebecca")

  print("\nOur current group now consists of:\n", queue1)
  
  print("\nNow the first two members of our group will join another group that includes Stephanie.")

  queue2.append(queue1.popleft())
  queue2.append(queue1.popleft())

  queue2 = deque(queue2)

  print("\nOur current group now consists of:\n", queue1)
  print("\nThe other group consists of:\n", queue2)