#import requests
#url = 'https://api.scryfall.com/'
#r = requests.get(url, )
#print(r.text)
#print(r.status_code)

import json as js

import tkinter as tk
import png
from PIL import Image, ImageTk
import sys
import Loading as load
import requests
from io import BytesIO



class Frame:

    def __init__(self):



        self.background_ar = []






    def add_labels(self):
        tk.Label(self.root, text="First").grid(row=0)
        tk.Label(self.root, text="Second").grid(row=1)

    def add_color_frames(self):
        padx = (2.5, 2.5)
        pady = (2.5, 2.5)
        high = self.screen_height/8


        frame_top = tk.Frame(self.root, height=high, width=self.screen_width, bg="BLACK")

        vscrollbar = tk.Scrollbar(self, orient="VERTICAL")
        vscrollbar.pack(fill=Y, side="RIGHT", expand=False)

        canvas_bottom = tk.Canvas(self.root, height=self.screen_height-high, width=self.screen_width,
                                  yscrollcommand=vscrollbar.set)

        frame_top.pack(padx=padx, pady=pady)
        canvas_bottom.pack(padx=(20, 20), pady=pady)
        vscrollbar.config(command=canvas_bottom.yview)




        self.root.update()

        color_ar = [(255, 255, 102), (51, 51, 255), (32, 32, 32), (204, 0, 0), (76, 153, 0), (204, 204, 0), (160, 160, 160)]
        frame_ar = []

        width = round((canvas_bottom.winfo_width()/len(color_ar))-len(color_ar)*2*padx[0])
        hight = round(self.screen_height-high)

        for i in range(0, len(color_ar)):
            new_frame = tk.Frame(canvas_bottom, heigh=hight, width=width,
                                 bg="WHITE", highlightbackground=self.to_rgb(color_ar[i]),
                                 highlightcolor=self.to_rgb(color_ar[i]), highlightthickness=10)
            frame_ar.append(new_frame)
            frame_ar[i].grid(row=0, column=i, sticky="w", padx=padx, pady=pady)




    def to_rgb(self, rgb):
        return "#%02x%02x%02x" % rgb


    def create_rectangle(self, canvas, x1, y1, x2, y2, rgb, **kwargs):
        #alpha = int(kwargs.pop('alpha') * 255)
        image = Image.new('RGBA', (x2 - x1, y2 - y1), (rgb[0], rgb[1], rgb[2], 10))
        self.background_ar.append(ImageTk.PhotoImage(image))
        canvas.create_image(x1, y1, image=self.background_ar[-1], anchor='nw')
        canvas.create_rectangle(x1, y1, x2, y2, **kwargs)

if __name__ == '__main__':
    w = Frame()
    #w.image(250, 250, (25, 15, 255, 255))

    w.add_color_frames()
    w.root.mainloop()
    #print(sys.path[0])

baum = False
if baum == True:
    reiter_hight = self.screen_height / 25
    search_hight = self.screen_height / 15



    frame_reiter = tk.Frame(self.root, height=reiter_hight, width=self.screen_width, bg="BLACK")
    frame_search = tk.Frame(self.root, height=search_hight, width=self.screen_width, bg="GREY")

    frame_reiter.grid(row=0, column=0, columnspan=2, sticky="nw", padx=padx, pady=pady)
    frame_search.grid(row=1, column=0, columnspan=2, sticky="nw", padx=padx, pady=pady)

    color_ar = ["WHITE", "BLUE", "BLACK", "GREEN", "YELLOW", "GREY"]
    frame_ar = []
    for i in range(0, len(color_ar)):
        width = self.screen_width / len(color_ar)
        print(width)
        new_frame = tk.Frame(self.root, height=self.screen_height - search_hight - reiter_hight, width=width,
                             bg=color_ar[i])
        print(color_ar[i])
        frame_ar.append(new_frame)

    frame_ar[1].grid(row=2, column=0, sticky="w", padx=padx, pady=pady)
    frame_ar[2].grid(row=2, column=1, sticky="w", padx=padx, pady=pady)



    #################################################################################################


    def end_fullscreen(self, event=None):
        new_geometry = self.half_window()
        self.root.attributes("-fullscreen", False)
        self.root.geometry(new_geometry)
        return "break"


    def half_window(self):
        factor = 2 / 3
        self.screen_width = str(round(factor * self.root.winfo_screenwidth()))
        self.screen_height = str(round(factor * self.root.winfo_screenheight()))


        self.position_x = str(round((self.root.winfo_screenwidth() - factor * self.root.winfo_screenwidth()) / 2))
        self.position_y = str(round((self.root.winfo_screenheight() - factor * self.root.winfo_screenheight()) / 2))
        string_return = self.screen_width + 'x' + self.screen_height + '+' + self.position_x + '+' + self.position_y

        return string_return



    def stop(self, event=None):
        self.root.destroy()

        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)

        # Ok an dieser stelle ist es wichtig, dass man die Funktion nicht als self.funtkion() aufruft, was sie direkt ausfürhrt
        # sondern als self.funktion (ohne Klammer) aufruft, warum auch immer
        #self.root.bind("<q>", self.toggle_fullscreen)
        self.root.bind("<Escape>", self.end_fullscreen)
        self.root.bind("<Shift-Escape>", self.stop)
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()