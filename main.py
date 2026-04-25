import tkinter as tk
from tkinter import messagebox
import python_module
import queue_module

queue = python_module

root = tk.Tk()
root.title("Очередь")

canvas = tk.Canvas(root, width=700, height=200)
canvas.pack(pady=10)

entry = tk.Entry(root)
entry.pack()

notify_var = tk.BooleanVar(value=True)
check = tk.Checkbutton(root, text="Показывать уведомления", variable=notify_var)
check.pack()

def switch_module():
    global queue
    saved = queue.get_all()

    if module_var.get() == "python":
        queue = python_module
    else:
        queue = queue_module

    queue.clear()
    for v in saved:
        queue.enqueue(v)

    draw_queue()


module_frame = tk.Frame(root)
module_frame.pack(pady=5)

module_var = tk.StringVar(value="python")

tk.Label(module_frame, text="Модуль:").pack(side=tk.LEFT)
tk.Radiobutton(
    module_frame, text="Python", variable=module_var,
    value="python", command=switch_module
).pack(side=tk.LEFT, padx=5)
tk.Radiobutton(
    module_frame, text="C++", variable=module_var,
    value="dll", command=switch_module
).pack(side=tk.LEFT, padx=5)

def draw_queue():
    canvas.delete("all")
    data = queue.get_all()
    x = 40

    for value in data:
        canvas.create_rectangle(x, 80, x + 60, 120)
        canvas.create_text(x + 30, 100, text=str(value))
        canvas.create_line(x + 60, 100, x + 70, 100, arrow=tk.LAST)
        x += 70

    
    canvas.create_text(
        350, 30,
        text=f"Размер очереди: {queue.size()}  ",
        font=("Arial", 14)
    )

def enqueue():
    try:
        value = int(entry.get())
        queue.enqueue(value)
        draw_queue()
    except ValueError:
        messagebox.showerror("Ошибка", "Введите число")


def dequeue():
    try:
        v = queue.dequeue()
        draw_queue()
        if notify_var.get():
            messagebox.showinfo("Удаление", f"Удалён элемент {v}")
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))


def clear():
    queue.clear()
    draw_queue()


def remove_less():
    try:
        v = int(entry.get())
        removed = queue.remove_less(v)
        draw_queue()
        if notify_var.get():
            messagebox.showinfo("Удалено", f"Удалено элементов: {removed}")
    except:
        messagebox.showerror("Ошибка", "Введите число")


def remove_greater():
    try:
        v = int(entry.get())
        removed = queue.remove_greater(v)
        draw_queue()
        if notify_var.get():
            messagebox.showinfo("Удалено", f"Удалено элементов: {removed}")
    except:
        messagebox.showerror("Ошибка", "Введите число")


def remove_equal():
    try:
        v = int(entry.get())
        removed = queue.remove_equal(v)
        draw_queue()
        if notify_var.get():
            messagebox.showinfo("Удалено", f"Удалено элементов: {removed}")
    except:
        messagebox.showerror("Ошибка", "Введите число")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="Добавить", width=12, command=enqueue).grid(row=0, column=0)
tk.Button(frame, text="Удалить", width=12, command=dequeue).grid(row=0, column=1)
tk.Button(frame, text="Очистить", width=12, command=clear).grid(row=0, column=2)

tk.Button(frame, text="Удалить <", width=12, command=remove_less).grid(row=1, column=0)
tk.Button(frame, text="Удалить >", width=12, command=remove_greater).grid(row=1, column=1)
tk.Button(frame, text="Удалить =", width=12, command=remove_equal).grid(row=1, column=2)

draw_queue()
root.mainloop()
