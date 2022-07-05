'''
Solveable Problem
'''
from queue import Empty

# old_house contains all the items needing to be moved into the uhaul and then dumped into the new house
old_house = [
    "box of knick knacks", "reclining chair", "couch", "box of shoes", "fridge",
     "box of spices", "box of clothes", "box of hats", "bbq grill", "dining room table",
      "tv", "box of cleaning supplies", "bed frame", "mattress", "box of clothes hangers",
       "box of electronics", "box of sewing materials", "coat rack", "blender", "box of kitchen tools"
]
# new_house has all the items moved from the old house
new_house = []

# counts all the items left within the old house
def currently_in_old_house():
    for x in range(len(old_house)):
        print("{place}. {house_item}".format(place = x + 1, house_item = old_house[x]))

# counts all the items now in the new house
def currently_in_new_house():
    for x in range(len(new_house)):
        print("{place}. {house_item}".format(place = x + 1, house_item = new_house[x]))

# looks at the remaining items in the old house to see what can be put into the Uhaul truck
def putting_into_Uhaul():
    print_old_house()
    truck_load = []
    print("Here are the items still in the old house: ")
    currently_in_old_house()
    i = 0
    for i in range(5):
        print("{} items left to fit into truck".format(5 - i))
        print("choose a number on the list and that'll be what's put out of the house and now into the truck")
        carry = None
        while carry == None:
            carry = int(input("which number on the list? "))
            if carry <= 0:
                print("that's not a number on the list")
                carry = None
            if carry > len(old_house):
                print("that's not a number on the list")
                carry = None
            else:
                '''
                we need to add the specific items into the truck and out of the old house, and something 
                that'd also help is if we showed what was left in the house 
                '''
                pass
        print("what's currently in the truck: \n{truck}".format(truck = truck_load))
    return truck_load

# Takes items out of the truck and then puts them into the new house
def taking_out_of_Uhaul(truck_load):
    print_new_house()
    print("what's stacked into the truck: {truck}".format(truck = truck_load))
    '''
    we need to pull each item off the truck one at a time and then put it into the house. 
    It'd also likely help showing up what is in the house after the truck has been emptied
    '''
    pass

# ascii art of a little old house
def print_old_house():
    print("  ____||____")
    print(" ///////////\\")
    print("///////////  \\")
    print("|    _    |  |")
    print("|[] | | []|[]|")
    print("|   | |   |  |")

# a nicer looking newer house
def print_new_house():
    print("           _")
    print("       ,--j j-------,")
    print("      /_.-.___.-.__/ \\")
    print("    ,8| [_],-.[_] | oOo")
    print(",,,oO8|_o8_|_|_8o_|&888o,,,")

while len(old_house) > 0:
    truck_stack = putting_into_Uhaul()
    taking_out_of_Uhaul(truck_stack)
print("Great! You're now fully moved!")