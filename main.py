import tkinter as tk
from PIL import *
from PIL import Image, ImageTk  # For image handling
from PIL.ExifTags import TAGS  # For extracting EXIF data
from tkinter import Button, filedialog, messagebox
import os




def ExtractExifData():
   ImagePath = ImageFileEntry.get()
   try:
       img = Image.open(ImagePath)
       ExifData = img._getexif()
       exif_info = ""
       if ExifData:
           for tag_id, tag_name in TAGS.items():
               if tag_id in ExifData:
                   tag_value = ExifData.get(tag_id)
                   exif_info += f"{tag_name}: {tag_value}\n"
                   
           ExifDisplay.config(state="normal")
           ExifDisplay.delete("1.0", tk.END)
           ExifDisplay.insert(tk.END, exif_info)
           ExifDisplay.config(state="disabled")
       else:
           ExifDisplay.config(state="normal")
           ExifDisplay.delete("1.0", tk.END)
           ExifDisplay.insert(tk.END, "No EXIF data found in the image.")
           ExifDisplay.config(state="disabled")
   except (FileNotFoundError, AttributeError):
       ExifDisplay.config(state="normal")
       ExifDisplay.delete("1.0", tk.END)
       ExifDisplay.insert(tk.END, "Error: Invalid image or image not found.")
       ExifDisplay.config(state="disabled")


def SelectImage():
    """Function to open a file dialog and set the selected image path in the entry."""
    ImagePath = filedialog.askopenfilename(
        filetypes=[("JPG File", "*.jpg"),
                   ("JPEG File", "*.jpeg"),
                   ("GIF File", "*.gif"),
                   ("PNG File","*.png")]
    )
    ImageFileEntry.config(state="normal")  # Enable the entry
    ImageFileEntry.delete(0, tk.END)  # Clear any previous content
    ImageFileEntry.insert(0, ImagePath)  # Insert the selected image path
    ImageFileEntry.config(state="disabled")  # Disable the entry to prevent editing



def Alert():
    messagebox.showinfo("Alert","File Saved")

def SaveFile():
    # Get the text from the entry field
    text = ExifDisplay.get("1.0", tk.END)
    
    # Check if the file already exists
    FileName= "image_log.txt"
    count = 1
    while os.path.exists(FileName):
        # If file exists, create another with an incremented number
        FileName= f"image_log_{count}.txt"
        count += 1
    
    # Write the text to the file
    with open(FileName, "w") as file:
        file.write(text)
        Alert()



# Create the main window
root = tk.Tk()
root.geometry('600x600')
root.resizable(False, False)
root.title("Exif Metadata Extractor")


# load and resize the background image
BackgroundImage = Image.open("images/Background2.png")  # Replace with your image path
ResizedImage = BackgroundImage.resize((600, 600))  # Adjust size as needed
BackgroundPhoto = ImageTk.PhotoImage(ResizedImage)

BackgroundLabel = tk.Label(root, image=BackgroundPhoto, border=False)
BackgroundLabel.place(x=0,y=0)


# Main label
MainLabel = tk.Label(root, text="Exif Metadata", font=('Times New Roman',14), fg='#FFFFFF', background="#000000")
MainLabel.place(x=10,y=10)


# Open the image using PIL
SelectButtonImage = Image.open("images/1.png")
# Resize the image
ResizedSelectButtonImag = SelectButtonImage.resize((80, 30))
# Convert the resized image to a PhotoImage object
LabelImageButton = ImageTk.PhotoImage(ResizedSelectButtonImag)

ImageSelectionButton = Button(root, image=LabelImageButton, bd=False,borderwidth=-10,border=False ,bg='black',highlightbackground='black',command=lambda:SelectImage())
ImageSelectionButton.place(x=40, y=50)


# Image file path display
ImageFileEntry = tk.Entry(root, width=45)
ImageFileEntry.place(x=160, y=55)


# Open the image using PIL
ExtractButtonImage = Image.open("images/2.png")
# Resize the image
ResizedExtractButtonImage = ExtractButtonImage.resize((80, 30))
# Convert the resized image to a PhotoImage object
LabelExtractButtonImage = ImageTk.PhotoImage(ResizedExtractButtonImage)

# Create a button with the label as the image
ExtractButton = Button(root, image=LabelExtractButtonImage, bd=False,borderwidth=-10,border=False ,bg='black',highlightbackground='black',command=lambda: ExtractExifData())
ExtractButton.place(x=40, y=90)

# Square box for displaying EXIF data
ExifDisplay = tk.Text(root, width=60, height=20)
ExifDisplay.place(x=40,y=130)



# Open the image using PIL
SaveInfo = Image.open("images/4.png")
# Resize the image
ResizedSaveInfoImage = SaveInfo.resize((70, 30))
# Convert the resized image to a PhotoImage object
LabelSaveInfoButton = ImageTk.PhotoImage(ResizedSaveInfoImage)


SaveButton = Button(root, image=LabelSaveInfoButton, bd=False, borderwidth=-10,bg='black', highlightbackground='black', command= lambda:SaveFile())
SaveButton.place(x=450, y=90)


# Open the image using PIL
ExitButtonImage = Image.open("images/3.png")
# Resize the image
ResizedExitButtonImage = ExitButtonImage.resize((70, 30))
# Convert the resized image to a PhotoImage object
LabelExitButton = ImageTk.PhotoImage(ResizedExitButtonImage)

# Create a button with the label as the image
ExitButton = Button(root, image=LabelExitButton, bd=False,borderwidth=-10,border=False ,bg='white',highlightbackground='white', command= lambda: root.destroy())
ExitButton.place(x=250, y=500)


root.mainloop()
