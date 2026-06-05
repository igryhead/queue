import ctypes

lib_cpp = ctypes.CDLL("./queue_cpp.dll")
lib_stl = ctypes.CDLL("./queue_stl.dll") 

lib_cpp.queueInit()
lib_stl.queueInit()

_lib = lib_cpp


def use_cpp():
    """Переключиться на реализацию с динамической памятью"""
    global _lib
    _lib = lib_cpp


def use_stl():
    """Переключиться на реализацию с STL"""
    global _lib
    _lib = lib_stl


def enqueue(x):
    if _lib.queueEnqueue(x) == 0:
        raise Exception("Недостаточно памяти")


def dequeue():
    val = ctypes.c_int()
    if _lib.queueDequeue(ctypes.byref(val)) == 0:
        raise Exception("Очередь пуста")
    return val.value


def clear():
    _lib.queueClear()


def size():
    return _lib.queueSize()


def get_all():
    data = []
    for i in range(size()):
        data.append(_lib.queueGetAt(i))
    return data


def remove_less(v):
    return _lib.queueRemoveByCondition(0, v)


def remove_greater(v):
    return _lib.queueRemoveByCondition(1, v)


def remove_equal(v):
    return _lib.queueRemoveByCondition(2, v)
