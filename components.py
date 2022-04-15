import tkinter as tk
from tkinter import filedialog
from tkinter.messagebox import showerror
import tkinter.ttk as ttk
from PIL import ImageTk, Image			# Image processing
from RealtimeObjectMeasurement import App
from utils import cv2_to_image
import os


class initRootMenu(tk.Menu):
    def winResize(self, winDim):
        self.master.winWidth = winDim.split("x")[0]
        self.master.geometry(winDim)

    def menuLoadWidgets(self):
        self.master.config(menu=self)

        self.rootMenuFile = tk.Menu(self.master, tearoff=0)
        self.add_cascade(label="File", menu=self.rootMenuFile)
        self.rootMenuFile.add_command(label="Exit\t\t\t\t\t(Alt+F4)", command=self.master.destroy)
        self.rootMenuFile.add_command(label="Contact", command=lambda event: super(initRootMenu, self).openWebsite("http://psaurav1290.github.io"))

        self.rootMenuResize = tk.Menu(self.master, tearoff=0)
        self.add_cascade(label="Resize", menu=self.rootMenuResize)
        self.rootMenuResize.add_command(label="Wide", command=lambda event: self.winResize("1500x1010"))
        self.rootMenuResize.add_command(label="Narrow", command=lambda event: self.winResize("800x1010"))

    def __init__(self, master=None):
        super().__init__()
        self.master = master
        self.menuLoadWidgets()


class initRootNotebook(ttk.Notebook):
    """
    Creates a tabbed Notebook of frames
    """

    def notebookLoadWidgets(self):
        self.rootOriginalImageTab = initRootNbTab(self, "Realtime")
        # self.rootTabShopping = initRootNbTab(self, "Intermediate Processing")

    def __init__(self, master):
        super().__init__()
        self.master = master
        self.pack(expand=1, fill="both")
        self.enable_traversal()
        self.notebookLoadWidgets()


class initRootNbTab (ttk.Frame):
    def tabLoadWidgets(self):

        self.tabImage = ImageTk.PhotoImage(Image.open(f"images/{self.tabName.replace(' ','-')}-tab-image-1200x220-01.png"))
        self.tabImageLabel = ttk.Label(self, image=self.tabImage)
        self.tabImageLabel.pack(side="top", ipadx=0, ipady=0, padx=0, pady=0)

        self.tabInputPane = initTabInputPane(self)
        self.tabConfigPane = initTabConfigPane(self)
        self.tabImagePane = initTabImagePane(self)

    def __init__(self, master=None, tabName="Tab"):
        super().__init__()
        self.master = master
        self.master.add(self, text=tabName)
        self.tabName = tabName
        self.tabLoadWidgets()


class initTabInputPane(ttk.Frame):
    _default = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample_image.jpg")
    _current = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample_image.jpg")

    def clearInputField(self, override=0):
        if self.clearInputFieldFlag or override:
            self.tabInputField.delete(0, 'end')
            self.clearInputFieldFlag = 0

    def open_image(self):
        input_text = self.tabInputField.get()
        if not input_text or input_text == self._current:
            filetypes = filetypes = (
                ('Image Files', ('*.jpg', '*.png', '*.jpeg')),
                ('All files', '*.*')
            )
            input_text = filedialog.askopenfilename(title='Open files', initialdir=self._default, filetypes=filetypes)

        if not input_text:
            input_text = self._current
        elif os.path.exists(input_text):
            pass
            # self.master.master.master._file_path = input_text
        else:
            showerror(
                title="Invalid File Path",
                message=f"File not found:\n{input_text}\nPath set to default."
            )
            input_text = self._current

        self.clearInputField(1)
        self.tabInputField.insert(0, input_text)
        self._current = input_text

    def inputPaneLoadWidgets(self):

        self.entryStyle = ttk.Style()
        self.entryStyle.map("Custom.TEntry", foreground=[('!focus', 'grey')])
        self.tabInputField = ttk.Entry(self, width=80, font=("Calibri", 15), style="Custom.TEntry")
        self.tabInputField.insert(0, self._default)
        self.tabSearchIconImage = ImageTk.PhotoImage(Image.open("images/search-icon-image-disabled-80x80.png"))
        self.tabSearchIcon = ttk.Button(self, image=self.tabSearchIconImage, style="searchIcon.TLabel", command=lambda event: self.open_image())
        self.clearInputFieldFlag = 1
        self.tabInputField.bind("<Button-1>", lambda event: self.clearInputField())
        self.tabInputField.pack(side="left", padx=40, pady=0, ipadx=0, ipady=8)
        self.tabSearchIcon.pack(side="left", padx=40, pady=0, ipadx=0, ipady=10)

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(side="top", ipadx=0, ipady=0, padx=10, pady=0)
        self.inputPaneLoadWidgets()

class initTabConfigPane(ttk.Frame):
    _width = 455
    _height = 305

    def set_sheet_size(self):
        self._width = int(self.tabWidthField.get())
        self._height = int(self.tabHeightField.get())
        self.master.master.master._file_path = self.master.tabInputPane._current
        
    def get_sheet_size(self):
        return (self._width, self._height)

    def inputPaneLoadWidgets(self):
        self.entryStyle = ttk.Style()
        self.entryStyle.map("Custom.TEntry", foreground=[('!focus', 'grey')])
        self.tabSizeLabel = ttk.Label(self, text="Set Refrence Sheet Size (width x height)    ", font=("Calibri", 12))
        self.tabWidthField = ttk.Entry(self, width=10, font=("Calibri", 12), style="Custom.TEntry")
        self.tabWidthField.insert(0, "455")
        self.tabWidthLabel = ttk.Label(self, text="mm     X    ", font=("Calibri", 12))
        self.tabHeightField = ttk.Entry(self, width=10, font=("Calibri", 12), style="Custom.TEntry")
        self.tabHeightField.insert(0, "305")
        self.tabHeightLabel = ttk.Label(self, text="mm", font=("Calibri", 12))
        self.tabSetSizeButton = ttk.Button(self, text="Get Image", command=lambda event: self.set_sheet_size())

        self.tabSizeLabel.pack(side="left", padx=10, pady=0, ipadx=0, ipady=8)
        self.tabWidthField.pack(side="left", padx=10, pady=0, ipadx=0, ipady=8)
        self.tabWidthLabel.pack(side="left", padx=10, pady=0, ipadx=0, ipady=8)
        self.tabHeightField.pack(side="left", padx=10, pady=0, ipadx=0, ipady=8)
        self.tabHeightLabel.pack(side="left", padx=10, pady=0, ipadx=0, ipady=8)
        self.tabSetSizeButton.pack(side="left", padx=80, pady=0, ipadx=0, ipady=10)

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(side="top", ipadx=0, ipady=0, padx=10, pady=0)
        self.inputPaneLoadWidgets()


class initTabImagePane(ttk.Frame):

    def imagePaneLoadWidgets(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.originalImageLabel = ttk.Label(self)
        self.originalImageLabel.grid(column=0, row=0, padx=5, pady=20, sticky="W")
        self.finalImageLabel = ttk.Label(self)
        self.finalImageLabel.grid(column=1, row=0, padx=5, pady=20, sticky="E")

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(side="top", ipadx=0, ipady=0, padx=10, pady=0)
        self.imagePaneLoadWidgets()
