#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <queue>
#include <vector>
#include <stdexcept>

namespace py = pybind11;
static std::queue<int> q;

void enqueue(int value) {
    q.push(value);
}

int dequeue() {
    if (q.empty()) {
        throw std::runtime_error("Очередь пуста");
    }
    int val = q.front();
    q.pop();
    return val;
}

void clear() {
    while (!q.empty()) q.pop();
}

int size() {
    return (int)q.size();
}

std::vector<int> get_all() {
    std::vector<int> result;
    std::queue<int> tmp = q;
    while (!tmp.empty()) {
        result.push_back(tmp.front());
        tmp.pop();
    }
    return result;
}

int remove_by_condition(int mode, int val) {
    int original = (int)q.size();
    int removed = 0;

    for (int i = 0; i < original; i++) {
        if (q.empty()) break;
        int x = q.front();
        q.pop();

        bool del = (mode == 0 && x < val) ||
                   (mode == 1 && x > val) ||
                   (mode == 2 && x == val);

        if (del) removed++;
        else q.push(x);
    }
    return removed;
}

int remove_less(int v)    { return remove_by_condition(0, v); }
int remove_greater(int v) { return remove_by_condition(1, v); }
int remove_equal(int v)   { return remove_by_condition(2, v); }

PYBIND11_MODULE(pybind_module, m) {
    m.doc() = "Очередь на STL через pybind11";
    m.def("enqueue",        &enqueue);
    m.def("dequeue",        &dequeue);
    m.def("clear",          &clear);
    m.def("size",           &size);
    m.def("get_all",        &get_all);
    m.def("remove_less",    &remove_less);
    m.def("remove_greater", &remove_greater);
    m.def("remove_equal",   &remove_equal);
}