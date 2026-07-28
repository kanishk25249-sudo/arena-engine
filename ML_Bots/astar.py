class Node:

    def __init__(self, x, y):

        # Position of this node
        self.x = x
        self.y = y

        # Distance travelled by Bot(Start)
        self.g = 0

        # Estimated distance left to Enemy(Goal)
        self.h = 0

        # Total Distance
        # f = g + h
        self.f = 0

        # Previous node
        self.parent = None

# BOT (START)
bot = Node(2, 2)

# ENEMY (GOAL)
enemy = Node(8, 5)


open_list = []
open_list.append(bot)

closed_list = []

# Printing bot info

print("Bot Position")
print(bot.x, bot.y)

print()

# Printing enemy info

print("Enemy Position")
print(enemy.x, enemy.y)

print()

print("Open List")
for node in open_list:
    print( "(",node.x,",",node.y,")")

print()

# CLOSED LIST

print("Closed List")
if len(closed_list) == 0:
    print("Empty")

print()

# CURRENT NODE

current_node = open_list[0]

print("Current Node")
print("(",current_node.x,",",current_node.y,")")

print()

# Moving Current Node from Open List to Closed List

open_list.remove(current_node)
closed_list.append(current_node)

print("Current Node moved to Closed List")

print()

# OPEN LIST

print("Open List")
if len(open_list) == 0:
    print("Empty")

print()

# CLOSED LIST

print("Closed List")
for node in closed_list:
    print("(",node.x,",",node.y,")")

print()


# Neighbouring Nodes

neighbours = []

# Left
left = Node(current_node.x - 1, current_node.y)

# Right
right = Node(current_node.x + 1, current_node.y)

# Up
up = Node(current_node.x, current_node.y - 1)

# Down
down = Node(current_node.x, current_node.y + 1)

neighbours.append(left)
neighbours.append(right)
neighbours.append(up)
neighbours.append(down)

print("Neighbour Nodes")

for node in neighbours:
    print("(", node.x, ",", node.y, ")")

print()

# Calculating g

for node in neighbours:
    # Every neighbour is exactly one step away
    node.g = 1

print("g Values")

for node in neighbours:
    print("(", node.x, ",", node.y, ")", "g =", node.g)

print()

# Calculating h

for node in neighbours:
    node.h = (abs(enemy.x - node.x)+
        abs(enemy.y - node.y))

print("h Values")

for node in neighbours:
    print("(", node.x, ",", node.y, ")", "h =", node.h)

print()

# Calculating f

for node in neighbours:
    node.f = node.g + node.h

print("Neighbour Information")

for node in neighbours:
    print( "(", node.x, ",", node.y, ")", "g =", node.g, "h =", node.h, "f =", node.f)

print()

# FINDING BEST NEIGHBOUR

best_node = neighbours[0]

for node in neighbours:
    if node.f < best_node.f:
        best_node = node

print("Best Neighbour")
print( "(", best_node.x, ",", best_node.y, ")")
print("g =", best_node.g)
print("h =", best_node.h)
print("f =", best_node.f)
