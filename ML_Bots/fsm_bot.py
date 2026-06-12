import math
ATTACK_RANGE = 150
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

# FSM

enemy_health = nearest_enemy["health"]
bot_health = bot["health"]
bot_state = ""

if enemy_health <= 10:
    bot_state = "ATTACK"
elif bot_health < 30:
    bot_state = "RETREAT"
elif smallest_distance <= ATTACK_RANGE:
    bot_state = "ATTACK"
else:
    bot_state = "CHASE"

# CHASE

if bot_state == "CHASE":
    if nearest_enemy["x"] > bot["x"]:
        action["right"] = 1
    elif nearest_enemy["x"] < bot["x"]:
        action["left"] = 1
    if nearest_enemy["y"] > bot["y"]:
        action["down"] = 1
    elif nearest_enemy["y"] < bot["y"]:
        action["up"] = 1

# ATTACK

elif bot_state == "ATTACK":
    if nearest_enemy["x"] > bot["x"]:
        action["right"] = 1
    elif nearest_enemy["x"] < bot["x"]:
        action["left"] = 1
    if nearest_enemy["y"] > bot["y"]:
        action["down"] = 1
    elif nearest_enemy["y"] < bot["y"]:
        action["up"] = 1
    action["shoot"] = 1

# RETREAT

elif bot_state == "RETREAT":
    if nearest_enemy["x"] > bot["x"]:
        action["left"] = 1
    elif nearest_enemy["x"] < bot["x"]:
        action["right"] = 1
    if nearest_enemy["y"] > bot["y"]:
        action["up"] = 1
    elif nearest_enemy["y"] < bot["y"]:
        action["down"] = 1

print("Bot State:", bot_state)
print("Bot Health:", bot_health)
print("Nearest Enemy Health:", enemy_health)
print("Distance:", round(smallest_distance, 2))

print()

print("Generated Action:")
print(action)
