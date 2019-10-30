import tkinter as tk
import Cube_Visual as cv
import Cube_Creation as cb
import Basic_Layout as bl


class MainWindow(tk.Tk):
    # pretty smooth way of creating the tk.Frame in this class, without having to use self.
    def __init__(self, *args, **kwargs):

        # Attributes of the MainWindow
        tk.Tk.__init__(self, *args, **kwargs)
        self.attributes("-fullscreen", True)

        self.sc_width = self.winfo_width()
        self.sc_height = self.winfo_height()

        # Key-Binder for the MainWindow
        self.bind("<Shift-Escape>", self.stop)
        self.bind("<Escape>", self.resize)
        self.bind("<q>", self.toggle_fullscreen)

        # Important Arrays
        self.list_resize = []
        self.frames = {}

        # Basic Layout for the whole window

        self.basic_layer = bl.ScrollableCanvas(parent=self, controller=self)
        self.list_resize.append(self.basic_layer)

        #self.top_reiter = bl.Reiter(parent=self.basic_layer.get_frame(), controller=self, width=self.sc_width,
        #                            height=self.sc_height, color="BLACK")
        #self.bottom_display = bl.InnerFrame(parent=self.basic_layer.get_frame(), controller=self, width=self.sc_width,
         #                                   height=self.sc_height*2, color="GREEN")
        #self.top_reiter.pack(padx=(2, 2), pady=(0, 2))
        #self.bottom_display.pack()

        #self.list_resize.append(self.top_reiter)
        #self.list_resize.append(self.bottom_display)

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def stop(self, event=None):
        self.destroy()

    def toggle_fullscreen(self, event=None):
        try:
            if self.attributes("-fullscreen") == False:
                self.attributes("-fullscreen", True)
                self.update()
                self.update_sizes()
        except:
            print('Mistake!')

    def str_resize(self, factor=5/6):
        width = round(factor * self.winfo_screenwidth())
        height = round(factor * self.winfo_screenheight())

        position_x = str(round((1-factor)*self.winfo_screenwidth()/2))
        position_y = str(round((1-factor)*self.winfo_screenheight()/2))

        string_return = str(width) + 'x' + str(height) + '+' + position_x + '+' + position_y
        return string_return

    def resize(self, event=None):
        try:
            if self.attributes("-fullscreen") == True:
                self.attributes("-fullscreen", False)
                self.geometry(self.str_resize())
                self.update()
                self.update_sizes()
        except:
            print('Mistake!')

    def update_sizes(self):
        for i in range(0, len(self.list_resize)):
            self.list_resize[i].redraw()
            print('thats a try')



if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()

# button = tk.Button(self, text="Go to the start page",
# command=lambda: controller.show_frame("StartPage"))


# For keybinds it has to be in a method, so that it can be called without brackets
