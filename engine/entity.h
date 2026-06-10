#ifndef ENTITY_H
#define ENTITY_H
#include "event.h"

#define MAX_PLAYERS 4
#define MAX_BULLETS 64

typedef struct {
    int player_id;
    float x_coord, y_coord;
    float vel_x, vel_y;
    int health;
    int alive_or_dead;
    int facing_x, facing_y;
} Player;

typedef struct {
    float x_coord, y_coord;
    float vel_x, vel_y;
    int owner_id;
    int active;
} Bullet;

typedef struct {
    Player players[MAX_PLAYERS];
    Bullet bullets[MAX_BULLETS];
    int player_count;
    EventQueue eq; 
} GameState;

void init_game_state(GameState *gs);
void spawn_player(GameState *gs, int id, float x, float y);
void spawn_bullet(GameState *gs, int owner_id, float x, float y, float vx, float vy);

#endif