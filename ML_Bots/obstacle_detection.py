state = {
    "bot_id": 3,

    "players": [
        {
            "id": 1,
            "x": 650,
            "y": 250,
            "health": 100
        },
        {
            "id": 3,
            "x": 100,
            "y": 250,
            "health": 80
        }
    ],
    "obstacles": [
        {
            "id": 1,
            "x": 350,
            "y": 200,
            "width": 100,
            "height": 100
        }
    ]
}

# Finding Bot

bot = None
for player in state["players"]:
    if player["id"] == state["bot_id"]:
        bot = player
        break

# Finding Enemy

enemy = None
for player in state["players"]:
    if player["id"] != state["bot_id"]:
        enemy = player
        break

print("Bot Position :", bot["x"], bot["y"])
print("Enemy Position :", enemy["x"], enemy["y"])
print()

# Checking Obstacles

obstacle_found = False
for obstacle in state["obstacles"]:
    obstacle_left = obstacle["x"]
    obstacle_right = obstacle["x"] + obstacle["width"]

    bot_x = bot["x"]
    enemy_x = enemy["x"]

    minimum_x = min(bot_x, enemy_x)
    maximum_x = max(bot_x, enemy_x)

    if obstacle_right >= minimum_x and obstacle_left <= maximum_x:
        obstacle_found = True

        print("Obstacle Detected")
        print()

        print("Obstacle Position")
        print("X :", obstacle["x"])
        print("Y :", obstacle["y"])
        print("Width :", obstacle["width"])
        print("Height :", obstacle["height"])

        break

if obstacle_found == False:
    print("Clear Path")
