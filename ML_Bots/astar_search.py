ATTACK_RANGE = 150

class Node:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.g = 0
        self.h = 0
        self.f = 0

        self.parent = None

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

        node.h = (abs(enemy.x - node.x)+ abs(enemy.y - node.y))

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

# BOT

bot = Node(2, 2)

# ENEMY

enemy = Node(8, 5)

# OPEN LIST

open_list = []
open_list.append(bot)

# CLOSED LIST

closed_list = []

# SEARCH

while len(open_list) > 0:
    current_node = get_best_node(open_list)
    open_list.remove(current_node)
    closed_list.append(current_node)

    print()

    print( "Current Node :", "(", current_node.x, ",", current_node.y , ")" )

    distance = calculate_distance(current_node.x, current_node.y, enemy.x, enemy.y)

    print("Distance :", distance)

    if distance <= ATTACK_RANGE:

        print()

        print("Enemy is inside Attack Range")
        break

    neighbours = generate_neighbours(current_node)

    calculate_costs(neighbours, current_node, enemy)

    for node in neighbours:
        if in_closed_list(node, closed_list):
            continue

        open_list.append(node)

    print()

    print("Open List :", len(open_list))
    print("Closed List :", len(closed_list))
  
