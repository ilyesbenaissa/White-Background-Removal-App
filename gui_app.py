from ctypes.wintypes import SIZE
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title("Remove Background")
        self.geometry("500x330")
        self.resizable(False, False)
        self.create_widgets()
        self.configure(bg='#2d2d2d')
        #add menu bar in the window
        self.create_menu()
    # create all the widgets
    def create_widgets(self):
        self.create_label()
        self.create_button()
        self.create_entry()

    # loop the window
    def run(self):
        self.mainloop()

    def create_label(self):
        # change the label text color to white grey
        self.label = ttk.Label(self, text="Select an image to remove its background", foreground="white", background="#2d2d2d")
        #make the label background transparent
        self.label.configure(background='#2d2d2d')
        self.label.pack(pady=20)

    # a entry to show the path of the image
    def create_entry(self):
        self.entry = ttk.Entry(self, width=50)
        self.entry.pack(pady=20)

    # a button to select the image
    def select_image(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                                   filetypes=(("png files", "*.png"), ("all files", "*.*")))
        self.entry.insert(0, self.filename)

    # the menu bar in the window

    def create_menu(self):
        self.menu = Menu(self)
        self.config(menu=self.menu)
        self.file_menu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Exit", command=self.destroy)
        #adding a help cascade in the menu bar
        self.help_menu = Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        #adding a How to use and About in the help cascade
        self.help_menu.add_command(label="How to Use ?", command=self.show_tips)
        self.help_menu.add_command(label="About", command=self.show_about)

    #defining show about function
    def show_about(self):
        messagebox.showinfo("About", "This app is created by Ilyes BENAISSA \n ilyes0benaissa@gmail.com")

    def show_tips(self):
        messagebox.showinfo("How to Use", "  1- Click on Select Image\n  2- Choose an Image with white Background\n  3- Click on Remove Background\n\nNote:The output path will be shown in box after Background is removed")

    #calling the file removebackground.py
    def remove_background(self):
        from functions import removebackgroud
        try:
            removebackgroud.RemoveBackground(self.filename)
            self.show_message()
        except:
            messagebox.showerror("Error", "Please select a file")
        
    #button to call the function remove_background
    def create_button(self):
        self.button = ttk.Button(self, text="Select Image", command=self.select_image)
        self.button.pack(pady=20)
        self.button = ttk.Button(self, text="Remove Background", command=self.remove_background)
        self.button.pack(pady=20)
        self.button = ttk.Button(self, text="View Image", command=self.view_image)
        self.button.pack(pady=20)
  
    def show_message(self):
        messagebox.showinfo("Info", "The background is successfully removed")
        #print the new file name path
        messagebox.showinfo("Info","Path: "+ os.path.splitext(self.filename)[0] + "_no_bg.png")


    # a button to view the image in a new box
    def view_image(self):
        from PIL import ImageTk, Image
        try:
            self.image = ImageTk.PhotoImage(Image.open(self.filename))
            self.panel = Label(self, image=self.image)
            self.panel.pack(pady=20)
            self.newWindow = Toplevel(self)
            self.newWindow.title("Image")
            self.newWindow.resizable(True, True)
            self.newWindow.geometry("500x500")
            self.image = Image.open(self.filename)
            self.image = self.image.resize((500, 500), Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(self.image)
            self.newWindow.configure(bg="#2d2d2d")
            self.panel = Label(self.newWindow, image=self.image)
            self.panel.pack(pady=20)
        except:
            messagebox.showerror("Error", "Please select a file")

        

if __name__ == "__main__":
    window = Window()
    window.run()