import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk  # For image handling
from PIL.ExifTags import TAGS  # For extracting EXIF data


# Function to extract EXIF data from the selected image
def extract_exif_data():
   image_path = image_file_entry.get()
   try:
       img = Image.open(image_path)
       exif_data = img._getexif()
       exif_info = ""
       if exif_data:
           for tag_id, tag_name in TAGS.items():
               if tag_id in exif_data:
                   tag_value = exif_data.get(tag_id)
                   exif_info += f"{tag_name}: {tag_value}\n"
                   
           exif_display.config(state="normal")
           exif_display.delete("1.0", tk.END)
           exif_display.insert(tk.END, exif_info)
           exif_display.config(state="disabled")
       else:
           exif_display.config(state="normal")
           exif_display.delete("1.0", tk.END)
           exif_display.insert(tk.END, "No EXIF data found in the image.")
           exif_display.config(state="disabled")
   except (FileNotFoundError, AttributeError):
       exif_display.config(state="normal")
       exif_display.delete("1.0", tk.END)
       exif_display.insert(tk.END, "Error: Invalid image or image not found.")
       exif_display.config(state="disabled")

def select_image():
    """Function to open a file dialog and set the selected image path in the entry."""
    image_path = filedialog.askopenfilename(
        filetypes=[("JPG File", "*.jpg"),
                   ("JPEG File", "*.jpeg"),
                   ("GIF File", "*.gif"),
                   ("PNG File","*.png")]
    )
    image_file_entry.config(state="normal")  # Enable the entry
    image_file_entry.delete(0, tk.END)  # Clear any previous content
    image_file_entry.insert(0, image_path)  # Insert the selected image path
    image_file_entry.config(state="disabled")  # Disable the entry to prevent editing



    
# Create the main window
root = tk.Tk()
root.geometry('600x600')
root.resizable(False, False)
root.title("Exif Metadata Extractor")



head_font = ('Times New Roman', 14)


# load and resize the background image
load_image = Image.open("images/Background2.png")  # Replace with your image path
resized_image = load_image.resize((600, 600))  # Adjust size as needed
photo = ImageTk.PhotoImage(resized_image)

bg_label = tk.Label(root, image=photo, border=False)
bg_label.place(x=0,y=0)


# Main label
main_label = tk.Label(root, text="Exif Metadata", font=head_font, fg='#FFFFFF', background="#000000")
main_label.place(x=10,y=10)






# Image selection button
image_button = tk.Button(root, text="Select Image", command=lambda: select_image())
image_button.place(x=40, y=50)

# Image file path display
image_file_entry = tk.Entry(root, width=50)
image_file_entry.place(x=130, y=55)

# Extract button
extract_button = tk.Button(root, text="Extract EXIF Data", command=extract_exif_data)
extract_button.place(x=40,y=90)

# Square box for displaying EXIF data
exif_display = tk.Text(root, width=60, height=20)
exif_display.place(x=40,y=130)

# scrollbar = tk.Scrollbar(root, command=exif_display.yview)
# exif_display.config(yscrollcommand=scrollbar.set)
# scrollbar.pack(side=tk.RIGHT)
# exif_display.pack(side=tk.LEFT)


root.mainloop()
