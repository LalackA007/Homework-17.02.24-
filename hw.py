import tkinter

root = tkinter.Tk()
clicks = 0
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry(f'300x200+{int(w / 2) - 150}+{int(h / 2) - 100}')


def change_text():
    global clicks
    if label.cget("text") == "Початковий текст":
        label.config(text="Новий текст")
    else:
        label.config(text="Початковий текст")
    clicks += 1
    root.title(f'{clicks}')


label = tkinter.Label(root, text="Початковий текст", padx=15, pady=10)
label.pack()

btn = tkinter.Button(root, text="Змінити текст", command=change_text, padx=15, pady=10)
btn.place(x=90, y=50)

root.mainloop()
