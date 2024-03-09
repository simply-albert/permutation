from itertools import permutations

# Define your set of values
values = ['F', 'F', 'F', 'M', 'M', 'M']

# Get all permutations of the values
all_permutations = permutations(values)

# Convert the permutations to a list for easy display
all_permutations_list =list(set(all_permutations))

# Print the permutations
for permutation in all_permutations_list:
    print(permutation)


