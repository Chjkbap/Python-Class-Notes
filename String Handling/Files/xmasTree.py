# This program prints a christmas tree made out of an ascii
# character the user picks. The user also chooses the height of
# the tree.

print('Time to put up your Christmas Tree')
print('----------------------------------\n')

# Print a Christmas Tree (triangle) using strings

# Let the user pick with ascii character they want to use to print the tree
tree_char = input('Enter a single letter, number or symbol you want to build your tree with [+]: ')

# If the user makes an invalid input set the character to +
tree_char_invalid = tree_char == '' or len(tree_char) > 1
if tree_char_invalid == True:
    tree_char = '+'


# Initialise tree_height variable to invalid value
tree_height = 0

# While tree_height has and invalid value as the user to input a value
while tree_height < 2 or tree_height > 20:
    tree_height = input('How tall do you want your tree [any number between 2 and 20]?')
    tree_height = int(tree_height)


tree_space = tree_height
tree_width=1

print('\n\n')


# From zero to tree_height print each layer of the tree with
# Less space and wider branches
for tree_layer in range(0, tree_height):

    branch = ''


    # From zero to the number of spaces required add a space to branch
    for space in range(0, tree_space):
        branch = branch + ' '

    # From zero to the width of tree required add a character to the branch
    for symbol in range(0, tree_width):
        branch = branch + tree_char

    # Increase the width of tree
    tree_width = tree_width + 1

    # Decrease the space needed by 1
    tree_space = tree_space - 1

    # Print the branch for this layer
    print(branch)

# Loop to next layer until tree_height is reached

print('\n\nSorry, no Christmas presents under this tree yet :(\n\n')

