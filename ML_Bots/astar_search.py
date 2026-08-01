class Node:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.g = 0
        self.h = 0
        self.f = 0

        self.parent = None

# DISTANCE

def calculate_distance(x1, y1, x2, y2):

    dx = x2 - x1
    dy = y2 - y1

    return (dx * dx + dy * dy) ** 0.5

# GENERATING NEIGHBOURS

def generate_neighbours(current_node):

    neighbours = []

    left = Node(current_node.x - 1, current_node.y)
    left.parent = current_node

    right = Node(current_node.x + 1, current_node.y)
    right.parent = current_node

    up = Node(current_node.x, current_node.y - 1)
    up.parent = current_node

    down = Node(current_node.x, current_node.y + 1)
    down.parent = current_node

    neighbours.append(left)
    neighbours.append(right)
    neighbours.append(up)
    neighbours.append(down)

    return neighbours

# CALCULATING COSTS

def calculate_costs(neighbours, current_node, enemy):

    for node in neighbours:
        node.g = current_node.g + 1
        node.h = (abs(enemy.x - node.x) + abs(enemy.y - node.y))
        node.f = node.g + node.h

# BEST NODE

def get_best_node(open_list):
    best_node = open_list[0]

    for node in open_list:
        if node.f < best_node.f:
            best_node = node
        elif node.f == best_node.f:
            if node.h < best_node.h:
                best_node = node

    return best_node

# CLOSED LIST CHECK

def in_closed_list(node, closed_list):

    for closed_node in closed_list:
        if (node.x == closed_node.x and node.y == closed_node.y):
            return True

    return False

# OPEN LIST CHECK

def in_open_list(node, open_list):

    for open_node in open_list:
        if (node.x == open_node.x and node.y == open_node.y):
            return True

    return False

# BOT

bot = Node(2, 2)

# ENEMY

enemy = Node(20, 15)

# OPEN LIST

open_list = []
open_list.append(bot)

# CLOSED LIST

closed_list = []

# SEARCH

i = 0

while len(open_list) > 0:

    current_node = get_best_node(open_list)
    if (current_node.x == enemy.x and current_node.y == enemy.y):
        print()

        print("Goal Reached")
        break

    open_list.remove(current_node)
    closed_list.append(current_node)

    print()

    print("Current Node :", "(", current_node.x, ",", current_node.y, ")")

    neighbours = generate_neighbours(current_node)

    calculate_costs(neighbours, current_node, enemy)

    for node in neighbours:
        if in_closed_list( node, closed_list):
            continue
        if in_open_list(node, open_list):
            continue

        open_list.append(node)

    print()

    print("Open List")

    for node in open_list:
        print( "(", node.x, ",", node.y, ")", "g =", node.g, "h =", node.h, "f =", node.f)

    print()

    print("Closed List")

    for node in closed_list:

        print( "(", node.x, ",", node.y, ")")

    print()
    
    print("Open List Size :", len(open_list))
    print("Closed List Size :", len(closed_list))

path = []
node = current_node

while node != None:
    path.append(node)
    node = node.parent

path.reverse()

print()

print("Shortest Path")

print()

for node in path:
    print("(", node.x, ",", node.y, ")")
