import math
state = {
    "bot_id": 3,

    "players": [
        {
            "id": 1,
            "x": 100,
            "y": 200,
            "health": 100
        },

        {
            "id": 2,
            "x": 300,
            "y": 250,
            "health": 80
        },

        {
            "id": 3,
            "x": 500,
            "y": 100,
            "health": 70
        }
    ]
}

# Bot Info
bot_id = state["bot_id"]

bot = None
for player in state["players"]:
    if player["id"] == bot_id:
        bot = player
        break

# Enemies Info

enemies = []

for player in state["players"]:
    if player["id"] != bot_id:
        enemies.append(player)

# Finding nearest enemy

nearest_enemy = None
smallest_distance = float("inf")

for enemy in enemies:
    distance = math.sqrt(
        (enemy["x"] - bot["x"])** 2 +(enemy["y"] - bot["y"])** 2
    )
    if distance < smallest_distance:
        smallest_distance = distance
        nearest_enemy = enemy

# Generating movement action

action = {
    "player_id": bot["id"],
    "up": 0,
    "down": 0,
    "left": 0,
    "right": 0,
    "shoot": 0
}

# Horizontal movement

if nearest_enemy["x"] > bot["x"]:
    action["right"] = 1
elif nearest_enemy["x"] < bot["x"]:
    action["left"] = 1

# Vertical movement (y increases downward)

if nearest_enemy["y"] > bot["y"]:
    action["down"] = 1
elif nearest_enemy["y"] < bot["y"]:
    action["up"] = 1

print("Bot Position:", bot["x"], bot["y"])
print("Nearest Enemy ID:", nearest_enemy["id"])
print("Nearest Enemy Position:", nearest_enemy["x"], nearest_enemy["y"])

print()

print("Generated Action:")
print(action)
