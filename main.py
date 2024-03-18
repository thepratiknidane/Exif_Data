import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Button, Entry, Text
from exif_utils import ExtractExifData
from file_utils import SelectImage, SaveFile
# from alert_utils import Alert

root = tk.Tk()
root.geometry('600x600')
root.resizable(False, False)
root.title("Exif Metadata Extractor")

BackgroundImage = Image.open("images/Background2.png")
ResizedImage = BackgroundImage.resize((600, 600))
BackgroundPhoto = ImageTk.PhotoImage(ResizedImage)
BackgroundLabel = tk.Label(root, image=BackgroundPhoto, border=False)
BackgroundLabel.place(x=0,y=0)

MainLabel = tk.Label(root, text="Exif Metadata", font=('Times New Roman',14), fg='#FFFFFF', background="#000000")
MainLabel.place(x=10,y=10)

LabelImageButton = ImageTk.PhotoImage(Image.open("images/1.png").resize((80, 30)))
ImageSelectionButton = Button(root, image=LabelImageButton, bd=False, borderwidth=-10, border=False, bg='black', highlightbackground='black', command=lambda: SelectImage(ImageFileEntry))
ImageSelectionButton.place(x=40, y=50)

ImageFileEntry = Entry(root, width=45)
ImageFileEntry.place(x=160, y=55)

LabelExtractButtonImage = ImageTk.PhotoImage(Image.open("images/2.png").resize((80, 30)))
ExtractButton = Button(root, image=LabelExtractButtonImage, bd=False, borderwidth=-10, border=False, bg='black', highlightbackground='black', command=lambda: ExtractExifData(ImageFileEntry.get(), ExifDisplay))
ExtractButton.place(x=40, y=90)

ExifDisplay = Text(root, width=60, height=20)
ExifDisplay.place(x=40,y=130)

LabelSaveInfoButton = ImageTk.PhotoImage(Image.open("images/4.png").resize((70, 30)))
SaveButton = Button(root, image=LabelSaveInfoButton, bd=False, borderwidth=-10, bg='black', highlightbackground='black', command=lambda: SaveFile(ExifDisplay))
SaveButton.place(x=450, y=90)

LabelExitButton = ImageTk.PhotoImage(Image.open("images/3.png").resize((70, 30)))
ExitButton = Button(root, image=LabelExitButton, bd=False, borderwidth=-10, border=False, bg='white', highlightbackground='white', command=root.destroy)
ExitButton.place(x=250, y=500)

root.mainloop()
