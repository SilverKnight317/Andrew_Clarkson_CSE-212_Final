"""
Stack example
This is just a placeholder until whole example is ready to put into stack example.
"""

fruit_stack = []
fruit = None
def making_a_stack():
    while input != "stop" or input != "STOP":
        fruit = input("input a fruit that you want to add to this stack: ")
        if fruit != "stop" or fruit != "STOP":
            fruit_stack.append(fruit)

if fruit == None:
    making_a_stack()
print(fruit_stack)