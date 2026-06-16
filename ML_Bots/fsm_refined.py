ATTACK_RANGE = 150

CRITICAL_TARGET_HP = 25

FINISH_OFF_HP = 10

RETREAT_HP = 30

# Testing Values

bot_health = 25
enemy_health = 15
distance = 100

# FSM

if bot_health == 0:
    bot_state = "DEAD"
elif enemy_health <= FINISH_OFF_HP:
    bot_state = "ATTACK"
elif bot_health < RETREAT_HP:
    bot_state = "RETREAT"
elif distance <= ATTACK_RANGE:
    bot_state = "ATTACK"
else:
    bot_state = "CHASE"

print("Bot Health:", bot_health)
print("Enemy Health:", enemy_health)
print("Distance:", distance)

print()

print("Bot State:", bot_state)
