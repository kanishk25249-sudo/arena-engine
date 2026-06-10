#include "physics.h"

static void update_player(Player *p) {
    if (p->alive_or_dead == 0) {
        return;
    }

    p->vel_x = p->vel_x * FRICTION;
    p->vel_y = p->vel_y * FRICTION;

    if (p->vel_x > MAX_SPEED) {
        p->vel_x = MAX_SPEED;
    }
    if (p->vel_x < -MAX_SPEED) {
        p->vel_x = -MAX_SPEED;
    }
    if (p->vel_y > MAX_SPEED) {
        p->vel_y = MAX_SPEED;
    }
    if (p->vel_y < -MAX_SPEED) {
        p->vel_y = -MAX_SPEED;
    }

    p->x_coord = p->x_coord + p->vel_x * DT;
    p->y_coord = p->y_coord + p->vel_y * DT;

    if (p->x_coord < 0.0f) {
        p->x_coord = 0.0f;
    }
    if (p->x_coord > WORLD_WIDTH) {
        p->x_coord = WORLD_WIDTH;
    }
    if (p->y_coord < 0.0f) {
        p->y_coord = 0.0f;
    }
    if (p->y_coord > WORLD_HEIGHT) {
        p->y_coord = WORLD_HEIGHT;
    }
}

static void update_bullet(Bullet *b) {
    if (b->active == 0) {
        return;
    }

    b->x_coord = b->x_coord + b->vel_x * DT;
    b->y_coord = b->y_coord + b->vel_y * DT;

    if (b->x_coord < 0.0f || b->x_coord > WORLD_WIDTH) {
        b->active = 0;
    }
    if (b->y_coord < 0.0f || b->y_coord > WORLD_HEIGHT) {
        b->active = 0;
    }
}

void update_physics(GameState *gs) {
    int i;
    for (i = 0; i < gs->player_count; i++) {
        update_player(&gs->players[i]);
    }
    for (i = 0; i < MAX_BULLETS; i++) {
        update_bullet(&gs->bullets[i]);
    }
}
