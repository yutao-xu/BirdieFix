import tkinter as tk
from tkinter import ttk
from open_door import open_door

t = 0
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs,)
        self.title("Birdie Fix")
        self.geometry("1280x720")
        self.tension = None
        self.string = None
        self.phone_number = None

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Homepage, ChooseTension, ChooseString, EnterNumber, ConfirmationPage, Checkout):
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

        tensions = []
        for i in range(19, 30):
            tensions.append(i + 1)
        
        tension = ttk.Combobox(self, values=tensions)
        tension.grid(row=1, column=4, padx=10, pady=10)

        back_button = ttk.Button(self, text="Back", command=lambda: controller.show_frame(Homepage))
        back_button.grid(row=2, column=4, padx=10, pady=10)

        next_button = ttk.Button(self, text="Next", command=lambda: self.next(controller, tension.get()))
        next_button.grid(row=2, column=8, padx=10, pady=10)
    
    def next(self, controller, tension):
        controller.tension = int(tension)
        controller.frames[ConfirmationPage].update_tension()
        controller.show_frame(ChooseString)
        

class ChooseString(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Choose A String")
        label.grid(row=0, column=4, padx=10, pady=10)

        strings = ["BG 80", "BG 90", "BG 100", "BG 110", "BG 120"]

        string = ttk.Combobox(self, values=strings)
        string.grid(row=1, column=4, padx=10, pady=10)

        back_button = ttk.Button(self, text="Back", command=lambda: controller.show_frame(ChooseTension))
        back_button.grid(row=2, column=4, padx=10, pady=10)

        next_button = ttk.Button(self, text="Next", command=lambda: self.next(controller, string.get()))
        next_button.grid(row=2, column=8, padx=10, pady=10)

    def next(self, controller, string):
        controller.string = string
        controller.frames[ConfirmationPage].update_string()
        controller.show_frame(EnterNumber)

class EnterNumber(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = ttk.Label(self, text="Enter Your Phone Number")
        label.grid(row=0, column=4, padx=10, pady=10)

        phone_number = ttk.Entry(self)
        phone_number.grid(row=1, column=4, padx=10, pady=10)

        back_button = ttk.Button(self, text="Back", command=lambda: controller.show_frame(ChooseString))
        back_button.grid(row=2, column=4, padx=10, pady=10)

        next_button = ttk.Button(self, text="Next", command=lambda: self.next(controller, phone_number.get()))
        next_button.grid(row=2, column=8, padx=10, pady=10)
    
    def next(self, controller, phone_number):
        controller.phone_number = int(phone_number)
        controller.frames[ConfirmationPage].update_phone_number()
        controller.show_frame(ConfirmationPage)

class ConfirmationPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        
        label = ttk.Label(self, text="Confirmation")
        label.grid(row=0, column=4, padx=10, pady=10)

        self.tension_label = ttk.Label(self)
        self.tension_label.grid(row=1, column=4, padx=10, pady=10)

        self.string_label = ttk.Label(self)
        self.string_label.grid(row=2, column=4, padx=10, pady=10)

        self.phone_number_label = ttk.Label(self)
        self.phone_number_label.grid(row=3, column=4, padx=10, pady=10)

        checkout_button = ttk.Button(self, text="Checkout", command=lambda: controller.show_frame(Checkout))
        checkout_button.grid(row=4, column=8, padx=10, pady=10)
    
    def update_tension(self):
        self.tension_label.config(text=f"Tension: {self.controller.tension} lbs")

    def update_string(self):
        self.string_label.config(text=f"String: {self.controller.string}")
    
    def update_phone_number(self):
        self.phone_number_label.config(text=f"Phone Number: {self.controller.phone_number}")

class Checkout(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # test buttons
        open_button = ttk.Button(self, text="Open Door", command=open_door)
        open_button.grid(row=0, column=4, padx=10, pady=10)

        back_button = ttk.Button(self, text="Start Over", command=lambda: controller.show_frame(Homepage))
        back_button.grid(row=1, column=4, padx=10, pady=10)

app = App()
app.mainloop()