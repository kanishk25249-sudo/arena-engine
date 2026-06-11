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

# Finding bot id
bot_id = state["bot_id"]
print("Bot ID:", bot_id)
print()

# Finding bot info

bot = None
for player in state["players"]:
    if player["id"] == bot_id:
        bot = player
        break

print("My Bot")
print("ID:", bot["id"],
      "X:", bot["x"],
      "Y:", bot["y"],
      "Health:", bot["health"]
    )
print()

# Finding enemies info

enemies = []

for player in state["players"]:
    if player["id"] != bot_id:
        enemies.append(player)

print("Enemies")

for enemy in enemies:
    print(
        "ID:",enemy["id"],
        "X:",enemy["x"],
        "Y:",enemy["y"],
        "Health:",enemy["health"]
    )
