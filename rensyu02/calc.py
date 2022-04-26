import tkinter as tk
import tkinter.messagebox as tkm

jj = 0
def button_click(event):
    button=event.widget
    num = button["text"]
    #tkm.showinfo(txt, f"{num}のボタンがクリックされました")
    entry.insert(tk.END, num)
    button["background"] = "red"

def eq_click(event):
    get = entry.get()
    ans = eval(get)
    entry.delete(0, tk.END)
    entry.insert(tk.END, ans)

def ac_click(a):
    entry.delete(0, tk.END)
 

if __name__ == "__main__":
    r,c = 1,1
    cl = "white"
    root = tk.Tk()
    root.title("電卓")
    root.geometry("400x500")
    entry = tk.Entry(root , 
                     justify = "right",
                     width = 10,
                     font=("Times New Roman",40)
                     )
    entry.grid(row=0, column=0, columnspan=4)

    
    for i, num in enumerate(range(9,-1,-1), 1):
        button = tk.Button(root, text=num, font=("Times New Roman",30) ,background = cl)
        button.bind("<1>", button_click)
        button.grid(row = r, column= c, padx = 10, pady = 10)
        if (i)%3 == 0:
            r += 1
            c = 0
        c += 1
        button = tk.Button(root, text = "+",font=("Times New Roman",30))
        button.bind("<1>", button_click)
        button.grid(row = r, column= c, padx = 10, pady = 10)
        
        button = tk.Button(root, text = "-",font=("Times New Roman",30))
        button.bind("<1>", button_click)
        button.grid(row = 4, column= 3, padx = 10, pady = 10)

        button = tk.Button(root, text = "=",font=("Times New Roman",30))
        button.bind("<1>", eq_click)
        button.grid(row = 4, column= 4, padx = 10, pady = 10)
    
        button = tk.Button(root, text = "AC",font=("Times New Roman",25))
        button.bind("<1>", ac_click)
        button.grid(row = 3, column= 4, padx = 10, pady = 10)
    

    root.mainloop()