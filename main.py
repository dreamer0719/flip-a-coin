import random
import tkinter as tk 

root = tk.Tk()
root.title("Head or Tails")
root.geometry("300x75")

output = ''

def click():
    global output
    output = random.choice(["Heads", "Tails"])
    Label.config(text=output)


#Display button
click_me_btn = tk.Button(root, text="Flip a coin", command=lambda: click())
click_me_btn.place(relx = 0.5, rely = 0.5)
click_me_btn.config (command=click, width=15, height=1, font=("Arial", 14))
click_me_btn.pack(anchor='center')

#Display result
Label = tk.Label(root, font=("Arial", 14))
Label.config(width=15, height=1)
Label.pack()

root.resizable(False, False)
root.mainloop()