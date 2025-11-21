# Author: Joseph Kracht
# Last Modified: 11/20/2025
# Title: MPG Calculator

import tkinter

class MyGUI:
    def __init__(self):
        # Create the main window`
        self.main_window = tkinter.Tk()

        # Create the first input frame
        self.input_1_frame = tkinter.Frame(self.main_window)

        self.label_1 = tkinter.Label(self.input_1_frame, text="Number of gallons your car holds:")
        self.label_1.pack(side="left")

        self.text_box_1 = tkinter.Text(self.input_1_frame, height=1, width=5,)
        self.text_box_1.pack(side="left")

        # Create the second input frame
        self.input_2_frame = tkinter.Frame(self.main_window)

        self.label_2 = tkinter.Label(self.input_2_frame, text="Number of miles your car can drive with one tank of gas:")
        self.label_2.pack(side="left")

        self.text_box_2 = tkinter.Text(self.input_2_frame, height=1, width=5,)
        self.text_box_2.pack(side="left")

        # Create the button
        self.button = tkinter.Button(self.main_window, height=1, width=10, text="Calculate MPG", command=self.on_button_click)

        # Pack everything
        self.input_1_frame.pack(padx=10, pady=5)
        self.input_2_frame.pack(padx=10, pady=5)
        self.button.pack(padx=10, pady=5)

        # create an empty label
        self.mpg_label = tkinter.Label(self.main_window)

        # Enter the main loop
        tkinter.mainloop()

    def on_button_click (self):
        # Set the label to mpg
        mpg = float(self.text_box_2.get("1.0", "end-1c")) / float(self.text_box_1.get("1.0", "end-1c"))
        self.mpg_label.config(text="Your Car gets " + str(mpg) + " MPG")
        self.mpg_label.pack(pady=10, padx=10)

# Create an instance of the window
my_gui = MyGUI()
