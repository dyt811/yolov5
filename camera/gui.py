# Mainly adapted from: https://stackoverflow.com/questions/16366857/show-webcam-sequence-tkinter

import PIL
from PIL import Image, ImageTk
import cv2
from tkinter import Label, Tk

# Width and Height of the window to be displayed.
width, height = 800, 600

# Capture the video from the very first device:
open_cv_capture = cv2.VideoCapture(0)

# Set the capture width and height.
open_cv_capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
open_cv_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Root window is an instance of tkinter.Tk class.
root = Tk()

# Bind the root window with escape key to quit
root.bind("<Escape>", lambda e: root.quit())

# Create a Label widget in the TK class.
label_main = Label(root)

# Pack the label widget
label_main.pack()


def show_frame():
    """
    Capture the image from FRAME, do various levels of convertions, and fill it in the label.
    :return:
    """
    # Read frame from the capture.
    _, frame_capture = open_cv_capture.read()

    # Flip the image.
    frame_capture = cv2.flip(frame_capture, 1)

    # Convert the input image from BGR to RGBA data matrix format
    image_RGBA_arrays = cv2.cvtColor(frame_capture, cv2.COLOR_BGR2RGBA)

    # Convert the input into a PIL.image
    image_pil_format = PIL.Image.fromarray(image_RGBA_arrays)

    # Convert from PIL.Image into a TK.Photoimage
    image_tk_format = ImageTk.PhotoImage(image=image_pil_format)

    # Load the tk_format to
    label_main.imgtk = image_tk_format
    label_main.configure(image=image_tk_format)

    # Invoke the function every 10ms
    label_main.after(10, show_frame)


show_frame()
root.mainloop()
