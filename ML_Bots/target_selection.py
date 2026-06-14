import math

CRITICAL_HP = 25

state = {
    "bot_id": 3,

    "players": [
        {
            "id": 1,
            "x": 100,
            "y": 200,
            "health": 20
        },
        {
            "id": 2,
            "x": 450,
            "y": 300,
            "health": 10
        },
        {
            "id": 3,
            "x": 300,
            "y": 250,
            "health": 80
        }
    ]
}

# Bot Info

bot = None
for player in state["players"]:
    if player["id"] == state["bot_id"]:
        bot = player
        break

# Finding Enemies And Distances

enemies = []
for player in state["players"]:
    if player["id"] != state["bot_id"]:
        distance = math.sqrt(
            (player["x"] - bot["x"])** 2 +(player["y"] - bot["y"])** 2)
        player["distance"] = distance
        enemies.append(player)

# Finding Critical Enemies

critical_enemies = []
for enemy in enemies:
    if enemy["health"] <= CRITICAL_HP:
        critical_enemies.append(enemy)

# Target Selection

target_enemy = None

# Case 1: No Critical Enemies

if len(critical_enemies) == 0:
    target_enemy = enemies[0]
    for enemy in enemies:
        if enemy["distance"] < target_enemy["distance"]:
            target_enemy = enemy

# Case 2: One Critical Enemy

elif len(critical_enemies) == 1:
    target_enemy = critical_enemies[0]

# Case 3: Multiple Critical Enemies

else:
    nearest_enemy = critical_enemies[0]
    farthest_enemy = critical_enemies[0]
    for enemy in critical_enemies:
        if enemy["distance"] < nearest_enemy["distance"]:
            nearest_enemy = enemy
        if enemy["distance"] > farthest_enemy["distance"]:
            farthest_enemy = enemy

    distance_difference = (farthest_enemy["distance"]- nearest_enemy["distance"])

    if distance_difference > 100:
        target_enemy = nearest_enemy
    else:
        target_enemy = critical_enemies[0]
        for enemy in critical_enemies:
            if enemy["health"] < target_enemy["health"]:
                target_enemy = enemy

print("Selected Target")
print("ID:", target_enemy["id"])
print("Health:", target_enemy["health"])
print("Distance:", round(target_enemy["distance"], 2))
