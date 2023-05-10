import tkinter as tk

def show_photo():
    photo = tk.PhotoImage(file=r'photo_next_py.png')
    image_label = tk.Label(root, image=photo)
    image_label.pack()
    image_label.image = photo


root = tk.Tk()
label = tk.Label(root, text="What's my favorite video?", fg="pink", bg="white")
label.pack()
button = tk.Button(root, text="Click to find out!", command=show_photo)
button.pack()

root.mainloop()