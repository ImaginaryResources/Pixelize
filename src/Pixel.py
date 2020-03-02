
# @Author:ImaginaryResources
# @Date: 2019-03-15 11:10:41
# @Last Modified by:ImaginaryResources
# @Last Modified time:2019-03-16 18:14:24

from tkinter import ttk
from tkinter import Tk
from tkinter import Button
from tkinter import Label
from tkinter import Entry
from tkinter import filedialog
from PIL import Image


class Main(Tk):
    def __init__(self):
        super(Main, self).__init__()
        self.title("Pixelize")
        self.geometry('346x346')
        self.resizable(width=False, height=False)
        self.wm_iconbitmap('pixelize.ico')

    def fileButton(self):
        # Calls the fileHandler function
        button = Button(self, text="Select File", command=self.fileHandler)
        button.config(height=5, width=48)
        button.place(x=0, y=25)

    def pixelizeButton(self):
        # Calls the pixelize function
        button = Button(self, text="Pixelize!", command=self.pixelize)
        button.config(height=5, width=48)
        button.place(x=0, y=250)

    def userInput(self):
        # Displays the entry box
        ttk.Label(self, text="# of pixels to skip",
                  font=('Arial', 10)).place(x=0, y=125)
        self.entry = Entry(self, font=('Arial', 30), width=15)
        self.entry.place(x=5, y=150)
        self.entry.focus_set()

    def fileHandler(self):
        global gFileName, gImg

        path = filedialog.askopenfilename(initialdir="/", title="Select Image", filetypes=(
            ("Image Files", "*.jpg *.png"), ("All Files", "*.*")))
        # Splits path and gets the last item
        fileName = path.split("/")[-1]

        try:
            img = Image.open(path)
        except:
            Label(self, text="Invalid Image",
                  font=('Arial', 10), fg="red").place(x=0, y=0)
        else:
            Label(self, text="Image Selected: " +
                  fileName, font=('Arial', 10), fg="blue").place(x=0, y=0)
            gFileName = fileName
            gImg = img

    def loadingBar(self):
        self.progressbar = ttk.Progressbar(
            self, orient='horizontal', length=340, mode='determinate')
        self.progressbar.place(x=3, y=225)

    def pixelize(self):
        try:
            # Get's user input from entry box
            skipBy = int(self.entry.get())
            if skipBy < 1:
                skipBy = 1
        except ValueError:
            print("Not an Int")
        else:
            width, height = gImg.size
            pixels = gImg.load()

            newImg = Image.new('RGBA', (width, height))
            newPix = newImg.load()

            # num of x iterations is max
            self.progressbar["maximum"] = width/skipBy

            for x in range(0, width, skipBy):
                for y in range(0, height, skipBy):
                    for r in range(skipBy):
                        for c in range(skipBy):
                            try:
                                newPix[x + r, y + c] = pixels[x, y]
                            except IndexError:
                                pass

                self.progressbar["value"] += 1
                self.progressbar.update()

            newImg.show()
            newImg.save(gFileName.split(".")[0] + str(skipBy) + ".png")

            self.progressbar["value"] = 0

    def multi(self):
        for i in range(100):
            skipBy = i + 1

            width, height = gImg.size
            pixels = gImg.load()

            newImg = Image.new('RGBA', (width, height))
            newPix = newImg.load()

            for x in range(0, width, skipBy):
                for y in range(0, height, skipBy):
                    for r in range(skipBy):
                        for c in range(skipBy):
                            try:
                                newPix[x + r, y + c] = pixels[x, y]
                            except IndexError:
                                pass

            newImg.save(gFileName.split(".")[0] + str(skipBy) + ".png")


window = Main()
window.fileButton()
window.userInput()
window.loadingBar()
window.pixelizeButton()
window.mainloop()
