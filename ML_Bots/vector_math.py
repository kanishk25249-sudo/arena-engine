import math

bot = {
    "x": 100,
    "y": 100
}

enemy = {
    "x": 500,
    "y": 300
}

dx = enemy["x"] - bot["x"]
dy = enemy["y"] - bot["y"]

print("dx =", dx)
print("dy =", dy)

distance = math.sqrt(dx * dx + dy * dy)

print()

print("Distance =", round(distance, 2))

direction_x = dx / distance
direction_y = dy / distance

print()

print("Direction X =", round(direction_x, 3))
print("Direction Y =", round(direction_y, 3))

action = {
    "up": 0,
    "down": 0,
    "left": 0,
    "right": 0
}

if direction_x > 0:
    action["right"] = 1
elif direction_x < 0:
    action["left"] = 1

if direction_y > 0:
    action["down"] = 1
elif direction_y < 0:
    action["up"] = 1

print()

print("Action")
print(action)
