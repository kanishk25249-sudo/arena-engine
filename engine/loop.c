#include <stdio.h>
#include <windows.h>
#include "loop.h"
#include "entity.h"
#include "physics.h"
#include "collision.h"
#include "input.h"
#include "state.h"

#define TICK_RATE 20
#define DT_NS (1000000000LL / TICK_RATE)

static long long get_time_ns() {
    LARGE_INTEGER freq, counter;
    QueryPerformanceFrequency(&freq);
    QueryPerformanceCounter(&counter);
    return (counter.QuadPart * 1000000000LL) / freq.QuadPart;
}

static void read_input(GameState *gs) {
    HANDLE h = GetStdHandle(STD_INPUT_HANDLE);
    DWORD available = 0;
    char buffer[256];
    PlayerInput input;
    PeekNamedPipe(h, NULL, 0, NULL, &available, NULL);
    while (available > 0) {
        if (fgets(buffer, 256, stdin) == NULL) {
            break;
        }
        if (parse_input(buffer, &input)) {
            apply_input(gs, &input);
        }
        PeekNamedPipe(h, NULL, 0, NULL, &available, NULL);
    }
}

void game_loop_run(GameState *gs) {
    long long previous = get_time_ns();
    long long lag = 0;
    int tick = 0;
    while (1) {
        long long current = get_time_ns();
        long long elapsed = current - previous;
        previous = current;
        lag += elapsed;
        while (lag >= DT_NS) {
            event_queue_clear(&gs->eq);
            read_input(gs);
            update_physics(gs);
            check_collisions(gs);
            serialize_state(gs, tick);
            tick = tick + 1;
            lag = lag - DT_NS;
        }
    }
}        