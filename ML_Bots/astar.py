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
