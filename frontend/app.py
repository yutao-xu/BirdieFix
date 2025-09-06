import tkinter as tk
from open_door import open_door

def pickup_handler():
    print("picked up")

def dropoff_handler():
    print("dropped off")

root = tk.Tk()

root.title("Birdie Fix")
root.geometry("1920x1080")

pickup_button = tk.Button(root, text="Pick Up", height=5, width=20, command=pickup_handler)
dropoff_button = tk.Button(root, text="Drop Off", height=5, width=20, command=dropoff_handler)
pickup_button.pack()
dropoff_button.pack()

# sample for test
open_button = tk.Button(root, text="Open", height=5, width=20, command=pickup_button)
open_button.pack()
root.mainloop()
