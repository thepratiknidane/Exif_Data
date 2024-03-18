from tkinter import filedialog
from os import path
from alert_utils import Alert

def SelectImage(ImageFileEntry):
    ImagePath = filedialog.askopenfilename(
        filetypes=[
                   ("JPG File", "*.jpg"),
                   ("JPEG File", "*.jpeg"),
                   ("GIF File", "*.gif"),
                   ("PNG File","*.png"),

            #    ("All Files", "*.*")  # Optionally, include an option to show all files
    ]
    )

    # configure the ImageFileEntry entry widget to enable editing temporarily

    ImageFileEntry.config(state="normal")
    ImageFileEntry.delete(0, "end")
    ImageFileEntry.insert(0, ImagePath)
    ImageFileEntry.config(state="disabled")

def SaveFile(ExifDisplay):
    text = ExifDisplay.get("1.0", "end-1c")
    FileName = "image_log.txt"
    count = 1
    while path.exists(FileName):
        FileName = f"image_log_{count}.txt"
        count += 1
    with open(FileName, "w") as file:
        file.write(text)
        Alert()
        
        
