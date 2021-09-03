import tkinter as tk
def handler():
            try: 
                 num=int(num)
                 print(num)
                 if num%2==0:

                          label.config (text=f"given num is even")
                 else:
                           label.config (text=f"given num is odd")
            except Exception as e :
                           label.config (text=f"given num is non digit ")
root=tk.Tk()
box=tk.Entry(root)
btn=tk.Button(root,text="submit",fg="yellow",bg="red",command=handler)
box.grid(row=0,column=0)
btn.grid(row=0,column=1)
label=tk.Label(root,text="")
label.grid(row=1,column=0)
root.mainloop()