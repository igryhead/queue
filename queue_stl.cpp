#include <queue>

static std::queue<int> q;

extern "C" {

__declspec(dllexport) void queueInit() {
    while (!q.empty()) q.pop();
}

__declspec(dllexport) int queueSize() {
    return (int)q.size();
}

__declspec(dllexport) int queueEnqueue(int value) {
    q.push(value);
    return 1;
}

__declspec(dllexport) int queueDequeue(int* outValue) {
    if (q.empty()) return 0;
    *outValue = q.front();
    q.pop();
    return 1;
}

__declspec(dllexport) void queueClear() {
    while (!q.empty()) q.pop();
}

__declspec(dllexport) int queueGetAt(int index) {
    // std::queue не поддерживает индексацию
    // копируем во временную очередь
    std::queue<int> tmp = q;
    for (int i = 0; i < index; i++) {
        if (tmp.empty()) return -9999;
        tmp.pop();
    }
    if (tmp.empty()) return -9999;
    return tmp.front();
}

__declspec(dllexport) int queueRemoveByCondition(int mode, int val) {
    int original = (int)q.size();
    int removed = 0;

    for (int i = 0; i < original; i++) {
        if (q.empty()) break;
        int x = q.front();
        q.pop();

        int del = 0;
        if (mode == 0 && x < val) del = 1;
        if (mode == 1 && x > val) del = 1;
        if (mode == 2 && x == val) del = 1;

        if (del) removed++;
        else q.push(x);
    }
    return removed;
}

} // extern "C"