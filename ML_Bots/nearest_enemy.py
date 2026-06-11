import math
state = {
    "bot_id": 2,

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
    print(
        "Enemy ID:",
        enemy["id"],
        "Distance:",
        round(distance, 2)
    )
    if distance < smallest_distance:
        smallest_distance = distance
        nearest_enemy = enemy

print()
print("Nearest Enemy")
print("ID:", nearest_enemy["id"],
      "X:", nearest_enemy["x"],
      "Y:", nearest_enemy["y"],
      "Distance:", round(smallest_distance, 2))        
