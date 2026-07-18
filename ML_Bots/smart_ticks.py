ATTACK_RANGE = 150
FINISH_OFF_HP = 10
RETREAT_HP = 30

state = {
    "tick": 13
}

bot_health = 25
enemy_health = 8
distance = 180


''' Emergency movement:
If bot is weak, retreat immediately.'''

if bot_health < RETREAT_HP:
    can_move = True

# Otherwise move every 3 ticks.
else:
    can_move = (state["tick"] % 3 == 0)

''' Emergency shooting:
# Finish off a weak enemy immediately.'''

if enemy_health <= FINISH_OFF_HP:
    can_shoot = True

else:
    can_shoot = (state["tick"] % 4 == 0)

# FSM

if enemy_health <= FINISH_OFF_HP:
    bot_state = "ATTACK"
elif bot_health < RETREAT_HP:
    bot_state = "RETREAT"
elif distance <= ATTACK_RANGE:
    bot_state = "ATTACK"
else:
    bot_state = "CHASE"

print("Tick :", state["tick"])
print("Bot Health :", bot_health)
print("Enemy Health :", enemy_health)
print("Distance :", distance)

print()

print("Bot State :", bot_state)
print("Can Move :", can_move)
print("Can Shoot :", can_shoot)
