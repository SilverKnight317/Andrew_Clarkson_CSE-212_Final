"""
Stack example
This is just a placeholder until whole example is ready to put into stack example.
"""

def making_a_stack():
    item = ""
    stack_list = []
    while item.upper() != "STOP":
        item = input('Type what you want in a bag, then type "stop" to stop: ')
        if item.upper() != "STOP":
            stack_list.append(item) # the .append() command adds the variable onto the stack
    return stack_list

# Processing the stack after it's been made
def processing_a_stack(stack):
    for x in range(len(stack)): # The len() command is used here to get the length for the for loop
        output = stack.pop() # The .pop() command pops the last item off the stack
        print(output)

item_stack = making_a_stack()
processing_a_stack(item_stack)