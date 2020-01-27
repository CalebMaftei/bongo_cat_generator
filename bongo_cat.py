from tkinter import *

root = Tk()

# window title
root.title("Bongo Cat Generator")
root.geometry("700x500")
root.resizable(width = False, height = False)


# adding a header
banner = Label(root, text = "Bongo Cat Generator",
 bg = "grey", fg = "white")
banner.grid(row = 0, columnspan = 2)

# entry field
entry_label = Label(root, text = "What should Bongo Cat say? ")
entry_box = Entry(root)
entry_label.grid(row = 1, column = 0, sticky = E)
entry_box.grid(row = 1, column = 1)

# the button
the_button = Button(root, text = "GIVE ME BONGO CAT!",
 bg = "grey", fg = "white")
the_button.grid(row = 2, columnspan = 2)

# bonus option (for extra fun)
c = Checkbutton(root, text = "Check this box if you like checking boxes")
c.grid(columnspan = 2)

# image display

root.mainloop()
