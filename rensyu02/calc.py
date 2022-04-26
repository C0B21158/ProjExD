from pynput import keyboard
import tkinter as tk
import tkinter.messagebox as tkm
def button_click(event):
    button=event.widget
    num = button["text"]
    #tkm.showinfo(txt, f"{num}のボタンがクリックされました")
    entry.insert(tk.END, num )

def eq_click(event):
    get = entry.get()
    ans = eval(get)
    entry.delete(0, tk.END)
    entry.insert(tk.END, ans)

if __name__ == "__main__":
    r,c = 1,1
    root = tk.Tk()
    root.title("tk")
    root.geometry("400x500")
    entry = tk.Entry(root , 
                     justify = "right",
                     width = 10,
                     font=("Times New Roman",40)
                     )
    entry.grid(row=0, column=0, columnspan=4)
    
    if keyboard.is_pressed("q"):
            for i, num in enumerate(range(9,-1,-1), 1):
                button = tk.Button(root, text=num, font=("Times New Roman",30), background="blue")
                button.bind("<1>", button_click)
                button.grid(row = r, column= c, padx = 10, pady = 10)
                if (i)%3 == 0:
                    r += 1
                    c = 0
                c += 1
                button = tk.Button(root, text = "+",font=("Times New Roman",30))
                button.bind("<1>", button_click)
                button.grid(row = r, column= c, padx = 10, pady = 10)
        
                button = tk.Button(root, text = "=",font=("Times New Roman",30))
                button.bind("<1>", eq_click)
                button.grid(row = 4, column= 4, padx = 10, pady = 10)


    for i, num in enumerate(range(9,-1,-1), 1):
        button = tk.Button(root, text=num, font=("Times New Roman",30))
        button.bind("<1>", button_click)
        button.grid(row = r, column= c, padx = 10, pady = 10)
        if (i)%3 == 0:
            r += 1
            c = 0
        c += 1
        button = tk.Button(root, text = "+",font=("Times New Roman",30))
        button.bind("<1>", button_click)
        button.grid(row = r, column= c, padx = 10, pady = 10)
        
        button = tk.Button(root, text = "=",font=("Times New Roman",30))
        button.bind("<1>", eq_click)
        button.grid(row = 4, column= 4, padx = 10, pady = 10)
    
    

    root.mainloop()