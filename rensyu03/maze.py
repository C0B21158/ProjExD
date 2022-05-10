
import maze_maker
import tkinter as tk
import tkinter.messagebox as tkm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def goal():
    tkm.showinfo("無","終わったんだｙ")
    root.destroy()


    
def main_proc():
    global cx ,cy , key , mx, my
    if key == "Up" and meiro[my-1][mx]==0:
        my -= 1
    if key == "Down" and meiro[my+1][mx]==0:
        my += 1
    if key == "Left" and meiro[my][mx-1]==0:
        mx -= 1
    if key == "Right" and meiro[my][mx+1]==0:
        mx += 1
    cx = mx*100
    cy = my*100
    
    canvas.coords("tori", cx+50, cy+50)
    if mx == 13 and my == 7:
        goal()
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    root.geometry("1500x900")

    canvas = tk.Canvas(root,width = "1500", height = "900" ,bg = "black")
    canvas.pack()

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    
    meiro = maze_maker.make_maze(15,9)
    maze_maker.show_maze(canvas, meiro)
    canvas.create_rectangle(100, 100, 200, 200, fill="Midnight Blue")
    canvas.create_rectangle(1300, 700, 1400, 800, fill="firebrick3")

    mx, my = 1,1
    cx = mx*100
    cy = my*100

    
    tori = tk.PhotoImage(file="c:/Users/admin/Documents/ProjExD_pub/fig/4.png")
    
 
    canvas.create_image(cx, cy, image =tori, tag = "tori")


    main_proc()
    root.mainloop()

