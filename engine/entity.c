#include <string.h>
#include "entity.h"

void init_game_state(GameState *gs) {
    memset(gs, 0, sizeof(GameState));
}

void spawn_player(GameState *gs, int id, float x, float y) {
    int index = gs->player_count;
    gs->player_count = gs->player_count + 1;
    gs->players[index].player_id = id;
    gs->players[index].x_coord = x;
    gs->players[index].y_coord = y;
    gs->players[index].vel_x = 0;
    gs->players[index].vel_y = 0;
    gs->players[index].health = 100;
    gs->players[index].alive_or_dead = 1;
}

void spawn_bullet(GameState *gs, int owner_id, float x, float y, float vx, float vy) {
    int i;
    for (i = 0; i < MAX_BULLETS; i++) {
        if (gs->bullets[i].active == 0) {
            gs->bullets[i].x_coord = x;
            gs->bullets[i].y_coord = y;
            gs->bullets[i].vel_x = vx;
            gs->bullets[i].vel_y = vy;
            gs->bullets[i].owner_id = owner_id;
            gs->bullets[i].active = 1;
            return;
        }
    }
}