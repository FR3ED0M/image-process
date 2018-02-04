from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
parent = Tk()


def do_popup(event):
    try:
        popup.tk_popup(event.x_root, event.y_root, 0)
    finally:
        popup.grab_release()


class openImage:
    def openPlains(self):
        image = Image.open("plains.jpg")
        image.save('new_image.png')
        image = image.resize((250, 250), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label4 = Label(image=photo)
        label4.image = photo
        label4.place(x=10, y=75)
        return

    def openBoxy(self):
        image = Image.open("boxy.jpg")
        image.save('new_image.png')
        image = image.resize((250, 250), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label4 = Label(image=photo)
        label4.image = photo
        label4.place(x=10, y=75)
        return

    def openColors(self):
        image = Image.open("colors.jpg")
        image.save('new_image.png')
        image = image.resize((250, 250), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label4 = Label(image=photo)
        label4.image = photo
        label4.place(x=10, y=75)
        return

    def openSpace(self):
        image = Image.open("space.jpg")
        image.save('new_image.png')
        image = image.resize((250, 250), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label4 = Label(image=photo)
        label4.image = photo
        label4.place(x=10, y=75)
        return

    def openPlasma(self):
        im = Image.open("plasma.jpg")
        im.save('new_image.png')
        im = im.resize((250, 250), Image.ANTIALIAS)
        ph = ImageTk.PhotoImage(im)
        label4 = Label(image=ph)
        label4.image = ph
        label4.place(x=10, y=75)
        return im


def rgbPixel():
    im2 = Image.open("new_image.png")
    im2 = im2.resize((250, 250), Image.ANTIALIAS)
    im2.getpixel((0, 0))

    for i in range(0, 50):
        for j in range(0, 50):
            im2.putpixel((i*5, j*5), (255, 0, 0))
            im2.putpixel((5 * i + 2, 5 * j + 2), (0, 0, 255))
            im2.putpixel((5 * i + 3, 5 * j + 3), (0, 255, 0))

    ph2 = ImageTk.PhotoImage(im2)
    label8 = Label(image=ph2)
    label8.image = ph2
    label8.place(x=300, y=75)
    return


def grayscale():
    im3 = Image.open("new_image.png").convert('L')
    im3 = im3.resize((250, 250), Image.ANTIALIAS)
    ph3 = ImageTk.PhotoImage(im3)
    label8 = Label(image=ph3)
    label8.image = ph3
    label8.place(x=300, y=75)
    return


# create a popup menu
x = openImage()
popup = Menu(parent, tearoff=0)
popup.add_command(label="Boxy", command=x.openBoxy)
popup.add_command(label="Colors", command=x.openColors)
popup.add_command(label="Space", command=x.openSpace)
popup.add_command(label="Plains", command=x.openPlains)
popup.add_command(label="Plasma", command=x.openPlasma)


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
jdata = 0
select = ttk.Button(parent, text="Select Image")
select.bind("<Button-1>", do_popup)
processBttn = ttk.Button(parent, text="Colorify Pixels", command=rgbPixel)
grayscaleBttn = ttk.Button(parent, text="Grayscale", command=grayscale)


# placement geometry
select.place(x=10, y=15)
processBttn.place(x=300, y=15)
grayscaleBttn.place(x=395, y=15)


parent.geometry("565x375")
parent.mainloop()