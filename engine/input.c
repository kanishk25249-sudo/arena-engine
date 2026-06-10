#include <stdio.h>
#include <string.h>
#include "input.h"
#include "physics.h"

static int find_player(GameState *gs, int id) {
    int i;
    for (i = 0; i < MAX_PLAYERS; i++) {
        if (gs->players[i].player_id == id) {
            return i;
        }
    }
    return -1;
}

void apply_input(GameState *gs, PlayerInput *input) {
    int index = find_player(gs, input->player_id);
    if (index == -1) {
        return;
    }

    Player *p = &gs->players[index];
    if (p->alive_or_dead == 0) {
        return;
    }

    if (input->right == 1) {
        p->vel_x = p->vel_x + ACCELERATION * DT;
        p->facing_x = 1.0f;
        p->facing_y = 0.0f;
    }
    if (input->left == 1) {
        p->vel_x = p->vel_x - ACCELERATION * DT;
        p->facing_x = -1.0f;
        p->facing_y = 0.0f;
    }
    if (input->down == 1) {
        p->vel_y = p->vel_y + ACCELERATION * DT;
        p->facing_x = 0.0f;
        p->facing_y = 1.0f;
    }
    if (input->up == 1) {
        p->vel_y = p->vel_y - ACCELERATION * DT;
        p->facing_x = 0.0f;
        p->facing_y = -1.0f;
    }

    if (input->shoot == 1) {
        float bx  = p->x_coord + p->facing_x * 20.0f;
        float by  = p->y_coord + p->facing_y * 20.0f;
        float bvx = p->facing_x * BULLET_SPEED;
        float bvy = p->facing_y * BULLET_SPEED;
        spawn_bullet(gs, p->player_id, bx, by, bvx, bvy);
    }
}

int parse_input(char *line, PlayerInput *input) {
    int result = sscanf(line,
        "{\"player_id\":%d,\"up\":%d,\"down\":%d,\"left\":%d,\"right\":%d,\"shoot\":%d}",
        &input->player_id,
        &input->up,
        &input->down,
        &input->left,
        &input->right,
        &input->shoot);
    return result == 6;
}

void process_input(GameState *gs) {
    char buffer[256];
    PlayerInput input;

    while (fgets(buffer, 256, stdin) != NULL) {
        if (parse_input(buffer, &input)) {
            apply_input(gs, &input);
        }
    }
}
