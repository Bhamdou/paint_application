import tkinter as tk
from tkinter import colorchooser
from tkinter import filedialog
from PIL import Image

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Paint App")
        self.root.geometry("800x600")
        self.old_x = None
        self.old_y = None
        self.penwidth = 5
        self.color_fg = "black"
        self.color_bg = "white"
        self.eraser_on = False
        self.canvas = tk.Canvas(root, width=800, height=600, bg=self.color_bg, bd=5, relief='ridge', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        filemenu = tk.Menu(menu)
        colormenu = tk.Menu(menu)
        toolsmenu = tk.Menu(menu)
        menu.add_cascade(label='File',menu=filemenu)
        menu.add_cascade(label='Colors',menu=colormenu)
        menu.add_cascade(label='Tools',menu=toolsmenu)
        filemenu.add_command(label='Export As PNG', command=self.save_as_png)
        colormenu.add_command(label='Brush Color', command=self.change_fg)
        colormenu.add_command(label='Background Color', command=self.change_bg)
        toolsmenu.add_command(label='Brush Size', command=self.change_size)
        toolsmenu.add_command(label='Eraser', command=self.use_eraser)

    def paint(self, event):
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, 
                                    width=self.penwidth, fill=self.color_fg if not self.eraser_on else self.color_bg,
                                    capstyle=tk.ROUND, smooth=True)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

    def change_fg(self):  # changing the color of the pen
        self.color_fg=colorchooser.askcolor(color=self.color_fg)[1]

    def change_bg(self):  # changing the background color of the canvas
        self.color_bg=colorchooser.askcolor(color=self.color_bg)[1]
        self.canvas['bg'] = self.color_bg

    def change_size(self):
        self.penwidth = int(input("Enter the size of brush "))

    def use_eraser(self):
        self.eraser_on = not self.eraser_on

    def save_as_png(self):
        file_path = filedialog.asksaveasfilename(defaultextension='.png')
        if file_path:
            x=self.root.winfo_rootx()+self.canvas.winfo_x()
            y=self.root.winfo_rooty()+self.canvas.winfo_y()
            x1=x+self.canvas.winfo_width()
            y1=y+self.canvas.winfo_height()
            ImageGrab.grab().crop((x,y,x1,y1)).save(file_path)

root = tk.Tk()
PaintApp(root)
root.mainloop()
