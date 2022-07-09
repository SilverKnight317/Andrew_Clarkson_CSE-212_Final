'''
Solveable Problem 
02_Set
'''
zoo_animals = ["tiger", "lion", "bear", "meerkat", "cheetah", "boar", "gorilla", 
"lion", "panda", "red panda", "giraffe", "lion", "boar", 'gorilla', 'bear', 
'panda', 'tiger', 'gorilla', 'panda', 'tiger', 'boar', 'meerkat', 'giraffe', 'elephant',
'tiger', 'gorilla', 'giraffe', 'lion', 'elephant', 'boar', 'panda', 'giraffe', 'lion',
'cheetah', 'lion', 'panda', 'red panda', 'boar', 'gorilla', 'chameleon', 'panda',
'giraffe', 'panda', 'boar', 'panda', 'gorilla', 'chameleon', 'butterfly', 'panda',
'elephant', 'tiger', 'lion', 'gator', 'penguin', 'lion', 'elephant', 'monkey', 'gorilla',
'penguin', 'eagle', 'hippo', 'boar', 'zebra', 'frog', 'butterfly', 'zebra', 'monkey', 
'elephant', 'snake', 'cheetah', 'koala', 'gorilla', 'meerkat', 'giraffe', 'tiger', 'lion']

new_animals = {'komodo dragon', 'panther', 'lemur', 'jaguar', 'wolf', 'naked mole-rat'}

def set_info():
    '''
    this will print out the size of the zoo_set and types of animals in zoo on separate lines, but also see how many duplicates are in the array
    '''

    count = 0

    print("duplicates within the zoo animal count: {}".format(count))

def add_uncounted_animals(animals_to_add):
    '''
    animals_to_add will need to be added into zoo_set individually
    '''

def print_spacing():
    print('\n==================================================')

zoo_set = set(zoo_animals)

print_spacing()
set_info()
print_spacing()
print("animals that are about to come to public: \n {}".format(new_animals))
print_spacing()
add_uncounted_animals(new_animals)
set_info()
