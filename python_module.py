class Node:
    __slots__ = ('value', 'next')

    def __init__(self, value: int):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

q = Queue()

def init():
    q.head = None
    q.tail = None
    q.count = 0

def size() -> int:
    return q.count

def enqueue(value: int):
    n = Node(value)
    if q.tail:
        q.tail.next = n
    else:
        q.head = n
    q.tail = n
    q.count += 1

def dequeue() -> int:
    if q.count == 0:
        raise RuntimeError("Очередь пуста")
    n = q.head
    value = n.value
    q.head = n.next
    if not q.head:
        q.tail = None
    q.count -= 1
    return value

def clear():
    q.head = None
    q.tail = None
    q.count = 0

def get_all():
    data = []
    cur = q.head

    while cur:
        data.append(cur.value)
        cur = cur.next
    return data

def remove_less(val: int) -> int:
    return _remove_by_condition(0, val)

def remove_greater(val: int) -> int:
    return _remove_by_condition(1, val)

def remove_equal(val: int) -> int:
    return _remove_by_condition(2, val)

def _remove_by_condition(mode: int, val: int) -> int:
    original = q.count
    removed = 0
    
    for _ in range(original):
        if q.count == 0:
            break
        x = dequeue()
        delete = (
            (mode == 0 and x < val) or
            (mode == 1 and x > val) or
            (mode == 2 and x == val)
        )
        
        if delete:
            removed += 1
        else:
            enqueue(x)
    return removed
