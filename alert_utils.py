from tkinter import messagebox

def Alert():
    messagebox.showinfo("Alert", "File Saved")



# from tkinter import messagebox
# import os

# def Alert(file_path):
#     message = f"File saved at:\n{file_path}"
#     result = messagebox.askyesno("Alert", message + "\n\nOpen file location?")
#     if result:
#         folder_path = os.path.dirname(file_path)
#         os.startfile(folder_path)  # Opens the file location

