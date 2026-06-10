#ifndef COLLISION_H
#define COLLISION_H

#include "entity.h"

#define PLAYER_WIDTH 32.0f
#define PLAYER_HEIGHT 32.0f
#define BULLET_WIDTH 6.0f
#define BULLET_HEIGHT 6.0f
#define BULLET_DAMAGE 5

void check_collisions(GameState *gs);

#endif