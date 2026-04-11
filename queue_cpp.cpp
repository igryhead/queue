#include <cstdlib>  
#include <cstddef>

struct Node {
    int value;
    Node* next;
};

struct Queue {
    Node* head;
    Node* tail;
    int count;
};

static Queue q = { nullptr, nullptr, 0 };

extern "C" {

__declspec(dllexport) void queueInit() {
    q.head = nullptr;
    q.tail = nullptr;
    q.count = 0;
}

__declspec(dllexport) int queueSize() {
    return q.count;
}

__declspec(dllexport) int queueEnqueue(int value) {
    Node* n = (Node*)std::malloc(sizeof(Node));
    if (!n) return 0;

    n->value = value;
    n->next = nullptr;

    if (q.tail) q.tail->next = n;
    else q.head = n;

    q.tail = n;
    q.count++;
    return 1;
}

__declspec(dllexport) int queueDequeue(int* outValue) {
    if (q.count == 0) return 0;

    Node* n = q.head;
    *outValue = n->value;

    q.head = n->next;
    if (!q.head) q.tail = nullptr;

    std::free(n);
    q.count--;
    return 1;
}

__declspec(dllexport) void queueClear() {
    int tmp;
    while (queueDequeue(&tmp)) {}
}

__declspec(dllexport) int queueGetAt(int index) {
    Node* cur = q.head;
    int i = 0;
    while (cur) {
        if (i == index) return cur->value;
        cur = cur->next;
        i++;
    }
    return -9999;
}

__declspec(dllexport) int queueRemoveByCondition(int mode, int val) {
    int original = q.count;
    int removed = 0;

    for (int i = 0; i < original; i++) {
        int x;
        if (!queueDequeue(&x)) break;

        int del = 0;
        if (mode == 0 && x < val) del = 1;
        if (mode == 1 && x > val) del = 1;
        if (mode == 2 && x == val) del = 1;

        if (del) removed++;
        else queueEnqueue(x);
    }
    return removed;
}

} 