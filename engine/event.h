#ifndef EVENT_H
#define EVENT_H

#define MAX_EVENTS 32

typedef enum {
    EVENT_PLAYER_HIT,
    EVENT_PLAYER_DIED,
    EVENT_BULLET_SPAWNED,
    EVENT_GAME_OVER
} EventType;

typedef struct {
    EventType type;
    int player_id;
    int killer_id;
    int damage;
} Event;

typedef struct {
    Event events[MAX_EVENTS];
    int count;
} EventQueue;

void event_queue_clear(EventQueue *eq);
void event_push(EventQueue *eq, Event e);

#endif