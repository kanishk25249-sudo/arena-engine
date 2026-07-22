import math

# GAME CONSTANTS

MAX_SPEED = 300.0
FRICTION = 0.85

WORLD_WIDTH = 800
WORLD_HEIGHT = 600

BULLET_SPEED = 500

ATTACK_RANGE = 150

CRITICAL_TARGET_HP = 25
FINISH_OFF_HP = 10
RETREAT_HP = 30

# HELPER FUNCTIONS

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# FINDING BOT

def find_bot(state):
    bot_id = state["bot_id"]
    for player in state["players"]:
        if player["id"] == bot_id:
            return player

    return None

# FINDING ENEMIES

def find_enemies(state, bot):
    enemies = []
    for player in state["players"]:
        if player["id"] != bot["id"]:
            enemy = player.copy()

            enemy["distance"] = calculate_distance(
                bot["x"],
                bot["y"],
                enemy["x"],
                enemy["y"]
            )
            enemies.append(enemy)

    return enemies

# TARGET SELECTION

def select_target(enemies):
    if len(enemies) == 0:
        return None
    critical_enemies = []

    for enemy in enemies:
        if enemy["health"] <= CRITICAL_TARGET_HP:
            critical_enemies.append(enemy)

    # CASE 1
    # No critical enemy
    # Choosing nearest

    if len(critical_enemies) == 0:
        target_enemy = enemies[0]

        for enemy in enemies:
            if enemy["distance"] < target_enemy["distance"]:
                target_enemy = enemy

        return target_enemy

    # CASE 2
    # Only one critical enemy

    elif len(critical_enemies) == 1:
        return critical_enemies[0]

    # CASE 3
    # Multiple critical enemies

    else:
        nearest_enemy = critical_enemies[0]
        farthest_enemy = critical_enemies[0]

        for enemy in critical_enemies:
            if enemy["distance"] < nearest_enemy["distance"]:
                nearest_enemy = enemy
            if enemy["distance"] > farthest_enemy["distance"]:
                farthest_enemy = enemy

        distance_difference = farthest_enemy["distance"]- nearest_enemy["distance"]
        
        # If one critical enemy is much closer,
        # finish him first.

        if distance_difference > 100:
            return nearest_enemy

        # Otherwise attack the enemy
        # with the lowest HP.

        target_enemy = critical_enemies[0]

        for enemy in critical_enemies:
            if enemy["health"] < target_enemy["health"]:
                target_enemy = enemy

        return target_enemy
