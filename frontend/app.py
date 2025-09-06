import tkinter as tk
from open_door import open_door

def pickup_handler():
    print("picked up")

def dropoff_handler():
    print("dropped off")

root = tk.Tk()

root.title("Birdie Fix")
root.geometry("1920x1080")

pickup_button = tk.Button(root, text="Open", width=25, command=pickup_handler)
dropoff_button = tk.Button(root, text="Drop Off", width=25, command=dropoff_handler)
pickup_button.pack()
dropoff_button.pack()

# sample for test
open_button = tk.Button(root, text="Open", width=25, command=open_door)
open_button.pack()
root.mainloop()
