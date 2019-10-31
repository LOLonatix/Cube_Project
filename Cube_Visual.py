import tkinter as tk


class Reiter(tk.Frame):

    def __init__(self, parent, controller, color, x_frame=5, y_frame=5):
        self.parent = parent
        self.parent.update()
        tk.Frame.__init__(self, self.parent, height=100-y_frame,
                          width=round(self.parent.winfo_width())-x_frame,
                          bg=color, highlightthickness=0, borderwidth=0)

        self.controller = controller
        self.x_frame = x_frame
        self.y_frame = y_frame

    def redraw(self):
        self.parent.update()
        #print(self.parent.winfo_width())
        self.config(width=self.parent.winfo_width()-self.x_frame)
        self.update()
        # hier rein das redrawen der Komponenten, die eine Ebene tiefer liegen


class InnerFrame(tk.Frame):

    def __init__(self, parent, controller, partner, color, y_frame=5):
        parent.update()
        partner.update()
        tk.Frame.__init__(self, parent, height=parent.winfo_height()-partner.winfo_height(), width=parent.winfo_width(),
                          bg=color)
        self.parent = parent
        self.controller = controller
        self.partner = partner
        self.y_frame = y_frame
        self.pady = (4, 0)

    def redraw(self):
        self.parent.update()
        self.partner.update()
        self.config(width=self.parent.winfo_width(),
                    height=self.parent.winfo_height()-self.partner.winfo_height()-self.y_frame)
        self.update()
        # hier rein das redrawen der Komponenten, die eine Ebene tiefer liegen
