import tkinter as tk
import Cube_Visual as cv


class ScrollableCanvas(tk.Canvas):
    def __init__(self, parent, controller, y_range=2000):

        self.parent = parent
        self.parent.update()
        self.controller = controller

        self.y_range = y_range
        self.vsb = tk.Scrollbar(parent, orient="vertical", command=self.yview)
        self.vsb.pack(side="right", fill="y")
        self.vsb.update()

        tk.Canvas.__init__(self, parent, width=self.parent.winfo_width()-self.vsb.winfo_width(),
                           height=self.parent.winfo_height(), borderwidth=0, bg="BLUE", highlightthickness=0)
        self.pack(side="left", expand=False)
        self.pack_propagate(0)
        self.update()

        self.frame = tk.Frame(self, borderwidth=0, width=self.winfo_width(), height=y_range, highlightthickness=2, bg="GREEN")
        self.frame.pack(anchor="nw")
        self.configure(yscrollcommand=self.vsb.set)
        self.create_window((4,4), window=self.frame, anchor="nw")
        self.yview_moveto(0)
        self.frame.pack_propagate(0)

        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.bind_all("<MouseWheel>", self._on_mousewheel)

        self.reiter = cv.Reiter(self.frame, self.controller, "BLACK")
        self.reiter.pack()
        self.inner_frame = cv.InnerFrame(self.frame, self.controller, self.reiter, "RED")
        self.inner_frame.pack(pady=self.inner_frame.pady)



    def onFrameConfigure(self, event):
        #Reset the scroll region to encompass the inner frame
        self.configure(scrollregion=self.bbox("all"))

    def _on_mousewheel(self, event):
            self.yview_scroll(-1*event.delta, "units")

    def get_frame(self):
        return self.frame

    def redraw(self):
        self.parent.update()
        self.vsb.update()
        self.config(width=self.parent.winfo_width()-self.vsb.winfo_width(), height=self.parent.winfo_height(),
                    borderwidth=0, highlightthickness=0)
        self.update()
        self.frame.configure(borderwidth=0, width=self.winfo_width(), height=self.y_range, highlightthickness=2, bg="GREEN")
        self.frame.update()
        #print("window", self.controller.winfo_width())
        #print('canvas', self.winfo_width())
        #print('frame', self.frame.winfo_width())

        self.reiter.redraw()
        self.inner_frame.redraw()





    #def populate(self):
     #   '''Put in some fake data'''
      #  for row in range(50):
        #    tk.Label(self.frame, text="1" , width=3).grid(row=row, column=0)
         #   t="this is the second column for row 1"
          #  tk.Label(self.frame, text=t).grid(row=row, column=1)
           # tk.Label(self.frame, text="Tryy").grid(row=row, column=2)