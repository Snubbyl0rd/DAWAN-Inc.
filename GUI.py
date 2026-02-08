#import tkinter library to create GUI
import tkinter as tk
#import messagebox from tkinter to show error popup
from tkinter import messagebox
#import calculator class 
from Calc_Class import Calculator

#create a class for GUI 
class CalculatorGUI:

    def __init__(self):
        #create the main window
        self.window = tk.Tk()
        #set the window title as calculator
        self.window.title("Calculator")
        #set window size
        self.window.geometry("400x600")
        #set the background color to dark gray
        self.window.configure(bg="#2B2B2B")
        #create instance of calculator class
        self.calc = Calculator()
        #Variable to store what the user is currently typing
        self.current_input = "0"
        #Variable to store the first number
        self.first_num = None
        #variable to store the operation
        self.operation = None
        #determines if display should be cleared or not
        self.reset_display = False
        #calls method and creates display
        self.create_display()
        #creates all buttons
        self.create_buttons()
    #function is made that creates the calculator screen
    def create_display(self):
        #creates a label widget
        self.display = tk.Label(
            #
            self.window,
            #sets starting text to 0 so when the user opens the calc they see 0 
            text="0",
            #sets font of the text
            font=("Arial", 24, "bold"),
            #sets background color to dark gray
            bg="#1E1E1E",
            #makes text color white
            fg="white",
            #sets the numbers to the right side
            anchor="e",
            #20 pixels of space on the left and right in display
            padx=20,
            #20 pixels of space on the top and bottom in display
            pady=20
        )
        #add display to the actual window
        self.display.pack(fill="both", padx=10, pady=10)
    #function to update the display and takes value as input
    def update_display(self, value):
        #changes display screen to show value 
        self.display.config(text=value)
        
     #function that creates all the buttons
    def create_buttons(self):
        #creates a container to hold all the scientific operation buttons 
        #this way they can be moved and aligened easily
        scientific_frame = tk.Frame(self.window, bg="#2B2B2B")
        #places the frame on the actual window with 5 pixels of space above and below
        scientific_frame.pack(pady=5)
        
        #a list of lists for the layout of the scientific buttons
        scientific_buttons = [
            ["sin", "cos", "tan"],
            ["arcsin", "arccos", "arctan"],
            ["√", "x²", "C"]
        ]
        #for loop through rows from scientific_buttons list
        for row in range(3):
            #for loop through columns from scientific_buttons list
            for col in range(3):
                #get the button name from the list
                text = scientific_buttons[row][col]
                #conditional statement to make the C button a different shade of blue
                if text == 'C':
                    bg_color = "#21618C"
                    fg_color = "white"
                #all the other buttons are the same color
                else:
                    bg_color = "#1A5490"
                    fg_color = "white"
                #makes each button
                button = tk.Button(
                    #puts it inside the scientific frame
                    scientific_frame,
                    #gets the text of the button
                    text=text,
                    #sets font style and size
                    font=("Arial", 12),
                    #sets the width and height of the button
                    width=8,
                    height=2,
                    #button color
                    bg=bg_color,
                    #text color
                    fg=fg_color,
                    #when u click a button it runs button_click with the button name
                    command=lambda t=text: self.button_click(t)
                )
                #puts the button into a grid format with rows and column
                button.grid(row=row, column=col, padx=5, pady=5)
                
        #creates container for the number and other operations buttons
        button_frame = tk.Frame(self.window, bg="#2B2B2B")
        #adds it to the window 
        button_frame.pack(pady=10)
        #creates a list for the numbers and simple operations 
        buttons = [
            ["7",  "8",  "9",  "/"],
            ["4",  "5",  "6",  "*"],
            ["1",  "2",  "3",  "-"],
            ["0",  ".",  "=",  "+"]
        ]
        # for loop through rows from buttons list
        for row in range(4):
            #for loop through column from buttons list
            for col in range(4):
                #gets the button name from the list
                text = buttons[row][col]
                #checks if the button is number or decimal point and changes color
                if text in "0123456789.":
                    bg_color = "#85C1E9"
                    fg_color = "white"
                # if its = it changes it to a different color
                elif text == "=":
                    bg_color = "#3498DB"
                    fg_color = "white"
                #if its anything else it gets a different color
                else:
                    bg_color = "#2874A6"
                    fg_color = "white"
                #
                button = tk.Button(
                    button_frame,
                    text=text,
                    font=("Arial", 14),
                    width=5,
                    height=2,
                    bg=bg_color,
                    fg=fg_color,
                    #runs the button_click
                    command=lambda t=text: self.button_click(t)
                )
                #puts the button into a grid format with rows and column
                button.grid(row=row, column=col, padx=5, pady=5)

