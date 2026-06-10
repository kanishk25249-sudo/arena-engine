#include "collision.h"

typedef struct {
    float left;
    float right;
    float top;
    float bottom;
} Box;

static Box get_player_box(Player *p) {
    Box b;
    b.left   = p->x_coord - PLAYER_WIDTH / 2.0f;
    b.right  = p->x_coord + PLAYER_WIDTH / 2.0f;
    b.top    = p->y_coord - PLAYER_HEIGHT / 2.0f;
    b.bottom = p->y_coord + PLAYER_HEIGHT / 2.0f;
    return b;
}

static Box get_bullet_box(Bullet *b) {
    Box box;
    box.left   = b->x_coord - BULLET_WIDTH / 2.0f;
    box.right  = b->x_coord + BULLET_WIDTH / 2.0f;
    box.top    = b->y_coord - BULLET_HEIGHT / 2.0f;
    box.bottom = b->y_coord + BULLET_HEIGHT / 2.0f;
    return box;
}

static int boxes_overlap(Box a, Box b) {
    if (a.right < b.left) {
        return 0;
    }
    if (a.left > b.right) {
        return 0;
    }
    if (a.bottom < b.top) {
        return 0;
    }
    if (a.top > b.bottom) {
        return 0;
    }
    return 1;
}

static void check_bullet_player_collisions(GameState *gs) {
    int i;
    int j;
    for (i = 0; i < MAX_BULLETS; i++) {
        if (gs->bullets[i].active == 0) {
            continue;
        }
        for (j = 0; j < MAX_PLAYERS; j++) {
            if (gs->players[j].alive_or_dead == 0) {
                continue;
            }
            if (gs->bullets[i].owner_id == gs->players[j].player_id) {
                continue;
            }
            Box bullet_box = get_bullet_box(&gs->bullets[i]);
            Box player_box = get_player_box(&gs->players[j]);
            if (boxes_overlap(bullet_box, player_box)) {
                gs->players[j].health = gs->players[j].health - BULLET_DAMAGE;
                gs->bullets[i].active = 0;
                Event hit_event;
                hit_event.type = EVENT_PLAYER_HIT;
                hit_event.player_id = gs->players[j].player_id;
                hit_event.killer_id = gs->bullets[i].owner_id;
                hit_event.damage = BULLET_DAMAGE;
                event_push(&gs->eq, hit_event);
                if (gs->players[j].health <= 0) {
                    gs->players[j].health = 0;
                    gs->players[j].alive_or_dead = 0;
                    Event death_event;
                    death_event.type = EVENT_PLAYER_DIED;
                    death_event.player_id = gs->players[j].player_id;
                    death_event.killer_id = gs->bullets[i].owner_id;
                    death_event.damage = 0;
                    event_push(&gs->eq, death_event);
                }
            }
        }
    }
}

static void check_player_player_collisions(GameState *gs) {
    int i;
    int j;
    for (i = 0; i < MAX_PLAYERS; i++) {
        if (gs->players[i].alive_or_dead == 0) {
            continue;
        }
        for (j = i + 1; j < MAX_PLAYERS; j++) {
            if (gs->players[j].alive_or_dead == 0) {
                continue;
            }
            Box a = get_player_box(&gs->players[i]);
            Box b = get_player_box(&gs->players[j]);
            if (boxes_overlap(a, b)) {
                float overlap_x = (a.right - b.left) / 2.0f;
                float overlap_y = (a.bottom - b.top) / 2.0f;
                if (overlap_x < overlap_y) {
                    gs->players[i].x_coord = gs->players[i].x_coord - overlap_x;
                    gs->players[j].x_coord = gs->players[j].x_coord + overlap_x;
                } else {
                    gs->players[i].y_coord = gs->players[i].y_coord - overlap_y;
                    gs->players[j].y_coord = gs->players[j].y_coord + overlap_y;
                }
            }
        }
    }
}

void check_collisions(GameState *gs) {
    check_bullet_player_collisions(gs);
    check_player_player_collisions(gs);
}