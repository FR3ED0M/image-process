from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
parent = Tk()


def do_popup(event):
    # display the popup menu
    try:
        popup.tk_popup(event.x_root, event.y_root, 0)
    finally:
        # make sure to release the grab
        popup.grab_release()


def openPlains():
    image = Image.open("plains.jpg")
    image = image.resize((250, 250), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    label4 = Label(image=photo)
    label4.image = photo
    label4.place(x=5, y=75)


def openBoxy():
    image = Image.open("boxy.jpg")
    image = image.resize((250, 250), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    label4 = Label(image=photo)
    label4.image = photo
    label4.place(x=5, y=75)


def openColors():
    image = Image.open("colors.jpg")
    image = image.resize((250, 250), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    label4 = Label(image=photo)
    label4.image = photo
    label4.place(x=5, y=75)


def openSpace():
    image = Image.open("space.jpg")
    image = image.resize((250, 250), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    label4 = Label(image=photo)
    label4.image = photo
    label4.place(x=5, y=75)


def openPlasma():
    image = Image.open("plasma.jpg")
    image = image.resize((250, 250), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    label4 = Label(image=photo)
    label4.image = photo
    label4.place(x=5, y=75)
    return image


def renderfy():
    photo = openPlasma()
    label8 = Label(image=photo)
    label8.image = photo
    label8.place(x=350, y=75)



# def showNew():



# create a popup menu
popup = Menu(parent, tearoff=0)
popup.add_command(label="Boxy", command=openBoxy)
popup.add_command(label="Colors", command=openColors)
popup.add_command(label="Space", command=openSpace)
popup.add_command(label="Plains", command=openPlains)
popup.add_command(label="Plasma", command=openPlasma)


# def openImage():
#     image = Image.open("space.jpg")
#     image = image.resize((250, 250), Image.ANTIALIAS)
#     photo = ImageTk.PhotoImage(image)
#     label4 = Label(image=photo)
#     label4.image = photo
#     label4.place(x=5, y=75)


# -------------------------------------------
# images have to be 640 x 480
# images are now being resized to 250 x 250
#  ------------------------------------------

# title of window
parent.title('Image Process')

# frames
frame = ttk.Frame(parent, borderwidth=5)

# buttons
select = ttk.Button(parent, text="Select Image")
select.bind("<Button-1>", do_popup)
mess_with = ttk.Button(parent, text="Process Image", command=renderfy)


# placement geometry
select.place(x=175, y=15)
mess_with.place(x=285, y=15)

parent.geometry("570x475")
parent.mainloop()