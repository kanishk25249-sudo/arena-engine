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

#Finding Bot

bot = None
for player in state["players"]:
    if player["id"] == state["bot_id"]:
        bot = player
        break


#Finding Enemy

enemy = None
for player in state["players"]:
    if player["id"] != state["bot_id"]:
        enemy = player
        break

print("Bot Position : ", (bot["x"], bot["y"]))
print("Enemy Position :", (enemy["x"], enemy["y"]))
print()


blocked = False

for obstacle in state["obstacles"]:

    obstacle_left = obstacle["x"]
    obstacle_right = obstacle["x"] + obstacle["width"]

    obstacle_top = obstacle["y"]
    obstacle_bottom = obstacle["y"] + obstacle["height"]

    path_left = min(bot["x"], enemy["x"])
    path_right = max(bot["x"], enemy["x"])

    path_top = min(bot["y"], enemy["y"])
    path_bottom = max(bot["y"], enemy["y"])

    x_overlap = (
        obstacle_right >= path_left and
        obstacle_left <= path_right
    )

    y_overlap = (
        obstacle_bottom >= path_top and
        obstacle_top <= path_bottom
    )

    if x_overlap and y_overlap:
        blocked = True

        print("Obstacle Found!")

        print()

        print("Obstacle ID :", obstacle["id"])
        print("X :", obstacle["x"])
        print("Y :", obstacle["y"])
        print("Width :", obstacle["width"])
        print("Height :", obstacle["height"])
        break

if blocked:

    print()

    print("Decision : Path is Blocked")
else:
    print("Decision : Clear Path")
