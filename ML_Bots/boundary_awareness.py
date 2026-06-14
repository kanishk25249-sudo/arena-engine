WORLD_WIDTH = 800
WORLD_HEIGHT = 600

bot = {
    "x": 800,
    "y": 300
}
action = {
    "up": 0,
    "down": 0,
    "left": 0,
    "right": 1
}

print("Before checking boundary")
print(action)

if action["left"] == 1 and bot["x"] <= 0:
    action["left"] = 0
if action["right"] == 1 and bot["x"] >= WORLD_WIDTH:
    action["right"] = 0
if action["up"] == 1 and bot["y"] <= 0:
    action["up"] = 0
if action["down"] == 1 and bot["y"] >= WORLD_HEIGHT:
    action["down"] = 0

print()
print("After checking boundary")
print(action)
