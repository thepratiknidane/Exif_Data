from tkinter import END

# TAGS dictionary from the PIL.ExifTags moduleU
# Used for interpreting Exif metadata
from PIL.ExifTags import TAGS
from PIL import Image

def ExtractExifData(ImagePath, ExifDisplay):
    try:
        # open the image file specified by ImagePath using the open() method of the Image class
        # creates an Image object representing the image
        img = Image.open(ImagePath)

        # retrieves the Exif metadata from the opened image using the _getexif()
        ExifData = img._getexif()

        # initializes an empty string exif_info to store the formatted Exif metadata
        exif_info = ""
        if ExifData:
            for tag_id, tag_name in TAGS.items():
                if tag_id in ExifData:
                    tag_value = ExifData.get(tag_id)
                    exif_info += f"{tag_name}: {tag_value}\n"

            #  lines configure the ExifDisplay text widget to enable editing temporarily        
            ExifDisplay.config(state="normal")
            ExifDisplay.delete("1.0", END)
            ExifDisplay.insert(END, exif_info)
            # It Disable the Editing
            ExifDisplay.config(state="disabled")
        else:

            #  This block sets the ExifDisplay to show a message indicating that no Exif data was found
            ExifDisplay.config(state="normal")
            ExifDisplay.delete("1.0", END)
            ExifDisplay.insert(END, "No EXIF data found in the image.")
            ExifDisplay.config(state="disabled")

    # handles exceptions that might occur during the execution of the code
    # such as if the file is not found or if there is an attribute error while processing the image
    # It sets the ExifDisplay to show an error message
    except (FileNotFoundError, AttributeError):
        ExifDisplay.config(state="normal")
        ExifDisplay.delete("1.0", END)
        ExifDisplay.insert(END, "Error: Invalid image or image not found.")
        ExifDisplay.config(state="disabled")
