'''
Solveable Problem
'''


def put_into_Uhaul():
    uhaul_stack = []
    item = input("what is going into the Uhaul? Type 'Stop' to stop: ")
    while item.upper() != "STOP":
        uhaul_stack.append(item)
        item = input("what is going into the Uhaul? Type 'Stop' to stop: ")
    return uhaul_stack

def coming_out_of_uhaul(stack_list):
    for x in range(len(stack_list)):
        item = stack_list.pop()
        print("you pull out of the uhaul: " + item)

uhaul = put_into_Uhaul()
print(uhaul)
coming_out_of_uhaul(uhaul)