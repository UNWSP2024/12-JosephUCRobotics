# Author: Joseph Kracht
# Last Modified: 11/20/2025
# Title: Auto Shop

import tkinter

class MyGUI:
    def __init__(self):
        # Create the main window`
        self.main_window = tkinter.Tk()

        # Create the checkboxes
        self.checkbox_frame = tkinter.Frame(self.main_window)
        self.left_frame = tkinter.Frame(self.checkbox_frame)

        self.checkbutton_1_var = tkinter.BooleanVar()
        self.checkbutton_1 = tkinter.Checkbutton(self.left_frame, text="Oil Change", variable=self.checkbutton_1_var)
        self.checkbutton_1.pack()

        self.checkbutton_2_var = tkinter.BooleanVar()
        self.checkbutton_2 = tkinter.Checkbutton(self.left_frame, text="Lube Job", variable=self.checkbutton_2_var)
        self.checkbutton_2.pack()

        self.checkbutton_3_var = tkinter.BooleanVar()
        self.checkbutton_3 = tkinter.Checkbutton(self.left_frame, text="Radiator Flush", variable=self.checkbutton_3_var)
        self.checkbutton_3.pack()

        self.checkbutton_4_var = tkinter.BooleanVar()
        self.checkbutton_4 = tkinter.Checkbutton(self.left_frame, text="Transmission Fluid", variable=self.checkbutton_4_var)
        self.checkbutton_4.pack()

        self.left_frame.pack(side="left")

        self.right_frame = tkinter.Frame(self.checkbox_frame)

        self.checkbutton_5_var = tkinter.BooleanVar()
        self.checkbutton_5 = tkinter.Checkbutton(self.right_frame, text="Inspection", variable=self.checkbutton_5_var)
        self.checkbutton_5.pack()

        self.checkbutton_6_var = tkinter.BooleanVar()
        self.checkbutton_6 = tkinter.Checkbutton(self.right_frame, text="Muffler Replacement", variable=self.checkbutton_6_var)
        self.checkbutton_6.pack()

        self.checkbutton_7_var = tkinter.BooleanVar()
        self.checkbutton_7 = tkinter.Checkbutton(self.right_frame, text="Tire Rotation", variable=self.checkbutton_7_var)
        self.checkbutton_7.pack()

        self.right_frame.pack(side="left")


        # Create the button
        self.button = tkinter.Button(self.main_window, height=1, width=10, text="Calculate Price", command=self.on_button_click)

        # Pack everything
        self.checkbox_frame.pack()
        self.button.pack(padx=10, pady=5)

        # create an empty label
        self.price_label = tkinter.Label(self.main_window)

        # Enter the main loop
        tkinter.mainloop()

    def on_button_click (self):
        # Calculate the price label
        price = 0
        if self.checkbutton_1_var.get():
            price += 30
        if self.checkbutton_2_var.get():
            price += 20
        if self.checkbutton_3_var.get():
            price += 40
        if self.checkbutton_4_var.get():
            price += 100
        if self.checkbutton_5_var.get():
            price += 35
        if self.checkbutton_6_var.get():
            price += 200
        if self.checkbutton_7_var.get():
            price += 20


        # Display the price
        self.price_label.config(text="The total price to do the selected work is $" + str(price))
        self.price_label.pack(pady=10, padx=10)

# Create an instance of the window
my_gui = MyGUI()
