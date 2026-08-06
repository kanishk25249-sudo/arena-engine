CELL_SIZE = 20

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

# OPEN LIST UPDATE

def update_open_list(node, open_list):

    for open_node in open_list:
        if (node.x == open_node.x and node.y == open_node.y):

            # Better path found
            if node.g < open_node.g:
                open_node.g = node.g
                open_node.h = node.h
                open_node.f = node.f
                open_node.parent = node.parent

            return

    # Node not present
    open_list.append(node)

# FIND PATH

def find_path(bot_x, bot_y, enemy_x, enemy_y):

    bot = Node(bot_x // CELL_SIZE, bot_y // CELL_SIZE)
    enemy = Node(enemy_x // CELL_SIZE, enemy_y // CELL_SIZE)

    open_list = []
    closed_list = []
    goal_reached = False

    open_list.append(bot)

    while len(open_list) > 0:
        current_node = get_best_node(open_list)

        open_list.remove(current_node)
        closed_list.append(current_node)

        if (current_node.x == enemy.x and current_node.y == enemy.y):
            goal_reached = True
            break

        neighbours = generate_neighbours(current_node)

        calculate_costs(neighbours, current_node, enemy)

        for node in neighbours:
            if in_closed_list(node, closed_list):
                continue

            update_open_list(node, open_list)

    if not goal_reached:
        return []
    
    path = []
    node = current_node

    while node is not None:
        path.append(node)
        node = node.parent

    path.reverse()
    return path

if __name__ == "__main__":
    path = find_path(537, 184, 261, 493)

    print()

    print("Shortest Path")

    print()

    for node in path:
        print("(", node.x, ",", node.y, ")")
