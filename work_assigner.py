from random import randint

file = 'phase3.txt'
members = {'Jonathan': [], 'Adrià': [], 'Pol': [], 'Raúl': []}

funcs = []
# Read and store the functions from the file
for line in open(file):
    if not line.startswith('#'):
        funcs.append(line.strip())

# Assign a new function randomly
while funcs:    # While funcs is not empty
    index = randint(0, len(funcs) - 1)

    chosen = 'Jonathan'
    minimum = len(members[chosen])
    for member in members.keys():
        if len(members[member]) < minimum:
            chosen = member
            minimum = len(members[chosen])
    
    members[chosen].append(funcs[index])
    del funcs[index]

# Print the output in console in markdown format for pasting directly into readme file
print("Here are the results:")
for member in members.keys():
    print("\t- " + member + ":")
    for func in members[member]:
        print("\t\t- " + func)
