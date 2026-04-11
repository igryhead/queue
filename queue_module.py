import ctypes

use_cpp = True

if use_cpp:
    lib = ctypes.CDLL("./queue_cpp.dll")
else:
    lib = ctypes.CDLL("./queue.dll")

lib.queueInit()

def enqueue(x):
    if lib.queueEnqueue(x) == 0:
        raise Exception("Недостаточно памяти")

def dequeue():
    val = ctypes.c_int()
    if lib.queueDequeue(ctypes.byref(val)) == 0:
        raise Exception("Очередь пуста")
    return val.value

def clear():
    lib.queueClear()

def size():
    return lib.queueSize()

def get_all():
    data = []
    for i in range(size()):
        data.append(lib.queueGetAt(i))
    return data

def remove_less(v):
    return lib.queueRemoveByCondition(0, v)

def remove_greater(v):
    return lib.queueRemoveByCondition(1, v)

def remove_equal(v):
    return lib.queueRemoveByCondition(2, v)