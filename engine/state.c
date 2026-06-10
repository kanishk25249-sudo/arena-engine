#include <stdio.h>
#include "state.h"

void serialize_state(GameState *gs, int tick) {
    int i;

    printf("{\"tick\":%d,\"players\":[", tick);

    int first_player = 1;
    for (i = 0; i < gs->player_count; i++) {
        Player *p = &gs->players[i];
        if (first_player == 0) {
            printf(",");
        }
        printf("{\"id\":%d,\"x\":%.2f,\"y\":%.2f,\"vx\":%.2f,\"vy\":%.2f,\"health\":%d,\"alive\":%d}",
            p->player_id,
            p->x_coord,
            p->y_coord,
            p->vel_x,
            p->vel_y,
            p->health,
            p->alive_or_dead);
        first_player = 0;
    }

    printf("],\"bullets\":[");

    int first_bullet = 1;
    for (i = 0; i < MAX_BULLETS; i++) {
        Bullet *b = &gs->bullets[i];
        if (b->active == 0) {
            continue;
        }
        if (first_bullet == 0) {
            printf(",");
        }
        printf("{\"x\":%.2f,\"y\":%.2f,\"vx\":%.2f,\"vy\":%.2f,\"owner\":%d}",
            b->x_coord,
            b->y_coord,
            b->vel_x,
            b->vel_y,
            b->owner_id);
        first_bullet = 0;
    }

    printf(",\"events\":[");
    
    int first_event = 1;
    for (i = 0; i < gs->eq.count; i++) {
        Event *e = &gs->eq.events[i];
        if (first_event == 0) {
            printf(",");
        }
        printf("{\"type\":%d,\"player_id\":%d,\"killer_id\":%d,\"damage\":%d}",
            e->type,
            e->player_id,
            e->killer_id,
            e->damage);
        first_event = 0;
    }
    printf("]");

    printf("]}\n");
    fflush(stdout);
}