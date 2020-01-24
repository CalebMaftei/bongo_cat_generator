from tkinter import *


# Main Frame Properties
bongo_cat = Tk()
bongo_cat.configure(background="black")
bongo_cat.geometry("700x500")
bongo_cat.resizable(width=False, height=False)
bongo_cat.title("Bongo Cat Generator")

# Label Frame Properties
title_frame = Frame(bongo_cat)
title_frame.configure(height=100, width=100, background="white")
title_frame.grid(row=1, column=1)
bongo_cat.mainloop()