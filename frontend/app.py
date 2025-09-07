import tkinter as tk
from tkinter import ttk
from open_door import open_door

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs,)
        self.title("Birdie Fix")
        self.geometry("1280x720")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Homepage, ChooseTension, ChooseString, EnterNumber):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(Homepage)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Homepage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = ttk.Label(self, text="Birdie Fix")
        label.grid(row=0, column=4, padx=10, pady=10)

        dropoff_button = ttk.Button(self, text="Pickup", command=lambda: controller.show_frame(ChooseTension))
        dropoff_button.grid(row=1, column=4, padx=10, pady=10)

        pickup_button = ttk.Button(self, text="String New Racket", command=lambda: controller.show_frame(ChooseTension))
        pickup_button.grid(row=1, column=8, padx=10, pady=10)

class ChooseTension(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = ttk.Label(self, text="Choose a Tension")
        label.grid(row=0, column=4, padx=10, pady=10)

        entry = ttk.Entry(self)
        entry.grid(row=1, column=4, padx=10, pady=10)
        
        back_button = ttk.Button(self, text="Back", command=lambda: controller.show_frame(Homepage))
        back_button.grid(row=2, column=4, padx=10, pady=10)

        next_button = ttk.Button(self, text="Next", command=lambda: controller.show_frame(ChooseString))
        next_button.grid(row=2, column=4, padx=10, pady=10)

class ChooseString(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = ttk.Label(self, text="Choose a String")
        label.grid(row=0, column=4, padx=10, pady=10)

        back_button = ttk.Button(self, text="Back", command=lambda: controller.show_frame(ChooseTension))
        back_button.grid(row=1, column=4, padx=10, pady=10)

        next_button = ttk.Button(self, text="Next", command=lambda: controller.show_frame(EnterNumber))
        next_button.grid(row=2, column=4, padx=10, pady=10)

class EnterNumber(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = ttk.Label(self, text="Enter Your Phone Number")
        label.grid(row=0, column=4, padx=10, pady=10)

        back_button = ttk.Button(self, text="Back", command=lambda: controller.show_frame(ChooseString))
        back_button.grid(row=1, column=4, padx=10, pady=10)

        open_button = ttk.Button(self, text="Open Door", command=open_door)
        open_button.grid(row=2, column=4, padx=10, pady=10)

app = App()
app.mainloop()