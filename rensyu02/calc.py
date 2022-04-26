
import tkinter as tk
import tkinter.messagebox as tkm
def button_click(event):
    btn=event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"{num}のボタンがクリックされました")

if __name__ == "__main__":
    r,c = 0,1
    root = tk.Tk()
    root.title("tk")
    root.geometry("300x450")
    for i, num in enumerate(range(9,-1,-1), 1):
        button = tk.Button(root, text=num, font=("Times New Roman",30))
        btn.bind("<1>", button_click)
        button.grid(row = r, column= c, padx = 10, pady = 10)
        if (i)%3 == 0:
            r += 1
            c = 0
        c += 1


    root.mainloop()