import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from Miniprojects.asset_management.asset_management import *


class AssetManagementGUI:
    def __init__(self, root, manager: AssetFileManager):
        self.root = root
        self.manager = manager
        self.current_directory = None
        self.current_dir_files = None
        self.current_file = None
        self.root.title("Asset Manager - " + manager.rootfolder)

        # Load your image file
        image_path =   # Replace with the path to your image
        self.images = \
            [Image.open(image_path + e) for e in ["kittens.jpg","froggy kitten.jpg"]]
        self.photo = ImageTk.PhotoImage
        self.photo = ImageTk.PhotoImage(self.images[0])

        # Create an image screen using a label
        self.image_label = tk.Label(root, image=self.photo)
        self.image_label.pack(side=tk.RIGHT, padx=10, pady=10)

        # Create buttons on the left side
        self.button_frame = ttk.Frame(root)
        self.button_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.button1 = ttk.Button(self.button_frame, text="Refresh", command=self.on_button1_click)
        self.button1.pack(pady=5)

        self.button2 = ttk.Button(self.button_frame, text="Button 2", command=self.on_button2_click)
        self.button2.pack(pady=5)

        self.button3 = ttk.Button(self.button_frame, text="Button 3", command=self.on_button3_click)
        self.button3.pack(pady=5)
    def refresh_directory(self):
        self.manager.generate_from_directory_data(reset=True)
        self.current_dir_files=manager.get_files_in_directory(self.current_directory)
        self.current_directory=cu

    def on_button1_click(self):
        # Define the action when Button 1 is clicked
        print("Button 1 clicked.")

    def on_button2_click(self):
        # Define the action when Button 2 is clicked
        print("Button 2 clicked.")

    def on_button3_click(self):
        # Define the action when Button 3 is clicked
        print("Button 3 clicked.")


if __name__ == "__main__":
    private_inputs = dict()
    private_inputs['testdir'] = "C:\\Projects\\py_miniprojects\\Miniprojects\\asset_management"
    PrivateInput.get_private_inputs(private_inputs)
    testdir = private_inputs["testdir"]
    manager = AssetFileManager(testdir)
    root = tk.Tk()
    app = AssetManagementGUI(root, manager)
    root.mainloop()


def main():
    return


if __name__ == "__main__":
    main()
