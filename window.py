from tkinter import *

class Window:
    def __init__(self, window_title) -> None:
        root = Tk()
        root.title("window_title")
        root.geometry("600x450")

        body_frame = Frame(root, background="RED")
        body_frame.pack(side = "bottom", padx=10, pady=10)

        body = Text(body_frame)
        root.mainloop()