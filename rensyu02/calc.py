
import tkinter as tk
import tkinter.messagebox as tkm
from turtle import right
def button_click(event):
    button=event.widget
    txt = button["text"]
    tkm.showinfo(txt, f"{num}のボタンがクリックされました")

if __name__ == "__main__":
    r,c = 1,1
    root = tk.Tk()
    root.title("tk")
    root.geometry("300x450")
    entry = tk.Entry(root , 
                     justify = "right",
                     width = 10,
                     font=("Times New Roman",40)
                     )
    entry.grid(row=0, column=0, clumnspan=4)

    for i, num in enumerate(range(9,-1,-1), 1):
        button = tk.Button(root, text=num, font=("Times New Roman",30))
        button.bind("<1>", button_click)
        button.grid(row = r, column= c, padx = 10, pady = 10)
        if (i)%3 == 0:
            r += 1
            c = 0
        c += 1


    root.mainloop()