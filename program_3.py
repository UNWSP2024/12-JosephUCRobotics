# Author: Joseph Kracht
# Last Modified: 11/20/2025
# Title: Auto Shop

import tkinter

class MyGUI:
    def __init__(self):
        # Create the main window`
        self.main_window = tkinter.Tk()

        # Create the checkboxes
        self.radio_frame = tkinter.Frame(self.main_window)

        self.radiobutton_var = tkinter.IntVar()
        self.radiobutton_var.set(1)
        self.checkbutton_1 = tkinter.Radiobutton(self.radio_frame, text="Daytime (6:00 A.M. through 5:59 P.M.)", variable=self.radiobutton_var, value=1)
        self.checkbutton_1.pack()

        self.checkbutton_2 = tkinter.Radiobutton(self.radio_frame, text="Evening (6:00 P.M.  through 11:59 P.M.)", variable=self.radiobutton_var, value=2)
        self.checkbutton_2.pack()

        self.checkbutton_3 = tkinter.Radiobutton(self.radio_frame, text="Off-Peak (midnight through 5:59 P.M.) ", variable=self.radiobutton_var, value=3)
        self.checkbutton_3.pack()

        # Create the minutes input
        self.minutes_frame = tkinter.Frame(self.main_window)
        self.minutes_label = tkinter.Label(self.minutes_frame, text="Length of call in minutes:")
        self.minutes = tkinter.Entry(self.minutes_frame, width=5)
        self.minutes.insert(0,"0")

        self.minutes_label.pack(side="left")
        self.minutes.pack(side="left")

        # Create the button
        self.button = tkinter.Button(self.main_window, height=1, width=10, text="Calculate Price", command=self.on_button_click)

        # Pack everything
        self.radio_frame.pack()
        self.minutes_frame.pack()
        self.button.pack(padx=10, pady=5)

        # create an empty label
        self.price_label = tkinter.Label(self.main_window)

        # Enter the main loop
        tkinter.mainloop()

    def on_button_click (self):
        # Calculate the price label;
        if self.radiobutton_var.get() == 1:
            price_per_minute = 0.02
        elif self.radiobutton_var.get() == 2:
            price_per_minute = 0.12
        else:
            price_per_minute = 0.05


        # Display the price
        self.price_label.config(text="The total price is $" + str(price_per_minute*int(self.minutes.get())))
        self.price_label.pack(pady=10, padx=10)

# Create an instance of the window
my_gui = MyGUI()
