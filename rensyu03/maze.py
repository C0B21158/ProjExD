import tkinter as tk

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    root.geometry("1500x900")

    canvas = tk.Canvas(root,width = "1500", height = "900" ,bg = "black")
    canvas.pack()

    tori = tk.PhotoImage(file="c:/Users/admin/Documents/ProjExD_pub/fig/4.png")
    cx ,cy = 300 ,400
    canvas.create_image(cx, cy, image =tori, tag = "tori")
    
    key = ""
    root.bind("<KeyPress>", key_down)

    root.bind("<KeyRelease>", key_up)
    
    root.mainloop()





