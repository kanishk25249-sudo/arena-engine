#ifndef INPUT_H
#define INPUT_H

#include "entity.h"

#define ACCELERATION 200.0f

typedef struct {
    int player_id;
    int up;
    int down;
    int left;
    int right;
    int shoot;
} PlayerInput;

void apply_input(GameState *gs, PlayerInput *input);
void process_input(GameState *gs);
int parse_input(char *line, PlayerInput *input);



#endif