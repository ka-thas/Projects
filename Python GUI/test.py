import tkinter as tk

window = tk.Tk()

frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()

label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()

frame_a.pack()
frame_b.pack()

greeting = tk.Label(
    master=frame_a,
    text="HEI PÅ DEG BOLLE",
    fg="#e0eeff",
    bg="#303040",
    width=50,
    height=20,
)
greeting.pack()

entry = tk.Entry(width=30)
entry.pack()

button = tk.Button(text="Klikk her", fg="black", bg="white")
button.pack()

window.mainloop()
