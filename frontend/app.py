import tkinter as tk

def pickup_handler():
    print("picked up")

def dropoff_handler():
    print("dropped off")

root = tk.Tk()

root.title("Birdie Fix")
root.geometry("1920x1080")

pickup_button = tk.Button(root, text="Pickup", width=25, command=pickup_handler)
dropoff_button = tk.Button(root, text="Drop Off", width=25, command=dropoff_handler)
pickup_button.pack()
dropoff_button.pack()
root.mainloop()
