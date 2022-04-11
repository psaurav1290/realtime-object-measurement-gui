from ttkthemes import themed_tk
import ctypes
from PIL import ImageTk, Image

from components import initRootMenu, initRootNotebook
from RealtimeObjectMeasurement import App
from utils import cv2_to_image
import os


class initRoot(themed_tk.ThemedTk):
    _file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"sample_image.jpg")

    def rootLoadWidgets(self):
        self.rootMenu = initRootMenu(self)
        self.rootNotebook = initRootNotebook(self)

    def __init__(self):
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
        super().__init__()
        self.set_theme("plastik")
        self.geometry("1500x1030+100+0")
        self.title("Realtime Object Measurement")
        self.iconbitmap("favicon.ico")
        self.winWidth = 1500
        self.rootLoadWidgets()


def update_frames(root, app):
    i = 0
    for img in app.get_image(root._file_path):
        img = ImageTk.PhotoImage(cv2_to_image(img))
        if i == 0:
            root.rootNotebook.rootOriginalImageTab.tabImagePane.originalImageLabel.image = img
            root.rootNotebook.rootOriginalImageTab.tabImagePane.originalImageLabel.configure(image=img)
        else:
            root.rootNotebook.rootOriginalImageTab.tabImagePane.finalImageLabel.image = img
            root.rootNotebook.rootOriginalImageTab.tabImagePane.finalImageLabel.configure(image=img)
        i += 1

    # Callback after given time
    root.after(1000, lambda: update_frames(root, app))


if __name__ == "__main__":
    app = App()
    root = initRoot()
    root.after(10, lambda: update_frames(root, app))
    root.mainloop()
