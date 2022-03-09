from tkinter import Tk, Canvas, NW, PhotoImage


win = Tk()

photoimage = PhotoImage(file="pictures/logo.png")

width, height = photoimage.width(), photoimage.height()
canvas = Canvas(win, width=width, height=height)
canvas.pack()

canvas.create_image(0, 0, image=photoimage, anchor=NW)

win.mainloop()

# atm cant resize and show into main script