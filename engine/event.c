#include <string.h>
#include "event.h"

void event_queue_clear(EventQueue *eq) {
    eq->count = 0;
}

void event_push(EventQueue *eq, Event e) {
    if (eq->count >= MAX_EVENTS) {
        return;
    }
    eq->events[eq->count] = e;
    eq->count = eq->count + 1;
}