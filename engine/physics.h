#include <stdio.h>

#ifndef PHYSICS_H
#define PHYSICS_H

#include "entity.h"

#define DT 0.05f
#define MAX_SPEED 300.0f
#define FRICTION 0.85f
#define WORLD_WIDTH 800.0f
#define WORLD_HEIGHT 600.0f
#define BULLET_SPEED 500.0f

void update_physics(GameState *gs);

#endif