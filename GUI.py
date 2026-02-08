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
    
    #function that runs whenever a button is clicked 
    def button_click(self, text):
        #checks if the button clicked is 0-9
        if text in "0123456789":
            #adds it to display
            self.add_number(text)
        #checks if it was a decimal point and adds it to display
        elif text == ".":
            self.add_decimal()
        #checks if it was plus, minus, multiply or divide 
        elif text in "+-*/":
            #saves operation 
            self.set_operation(text)
        #checks if the = button was clicked
        elif text == "=":
            #if it was, it does the calculatins
            self.calculate()
        #if the clear button was clicked
        elif text == "C":
            #it resets everything back to 0
            self.clear()
        #if the square root was clickedit calculated the squareroot of the number
        elif text == "√":
            self.square_root()
        #if square was clicked it squares the number entered
        elif text == "x²":
            self.square()
        #if any trig operations were clicked it does the calculations
        elif text in ["sin", "cos", "tan", "arcsin", "arccos", "arctan"]:
            self.trig_function(text)
    
    #function for when a number is clicked 
    def add_number(self, num):
        #checks if display needs to be cleared or if it shows 0 
        if self.reset_display or self.current_input == "0":
           #replaces whatever is on the screen with the new number, so if it
            #displays 0and the user clicks 4, it will show 4 not 04
            self.current_input = num
            #the number the user clicks will get added instead of being replaced or reset
            self.reset_display = False
        #if display doesnt need resetting and isnt 0 
        else:
            #add the number to the end
            self.current_input += num
        #update screen to show the current number
        self.update_display(self.current_input)

    #function for decimal point
    def add_decimal(self):
        #checks if decimal point alreaad exists
        if "." not in self.current_input:
            #if decimal point doesnt exist add one
            self.current_input += "."
        #update screen 
        self.update_display(self.current_input)
    
    #function that runs when operation buttons are clicked 
    def set_operation(self, op):
        #saves the currrent number on the screen as the first number and converts it to float
        self.first_num = float(self.current_input)
        #saves which operation the user chose to do like plus or minus
        self.operation = op
        #screen gets cleared when next number is clicked 
        self.reset_display = True
    
    #function that handles calculations 
    def calculate(self):
        #if user entered a number or picked an operation 
        if self.operation and self.first_num is not None:
            #tries to perform the calculation if it doesnt work it wont crash
            try:
                #gets second number user entered
                second_num = float(self.current_input)
                #checks which operation the user clicked on
                if self.operation == "+":
                    result = self.calc.addition(self.first_num, second_num)
                elif self.operation == "-":
                    result = self.calc.subtraction(self.first_num, second_num)
                elif self.operation == "*":
                    result = self.calc.multiplication(self.first_num, second_num)
                elif self.operation == "/":
                    #if the second number is 0 it shows error
                    if second_num == 0:
                        messagebox.showerror("Cannot divide by zero")
                        return
                    
                    result = self.calc.division(self.first_num, second_num)
                    
                #shows answer on the screen
                self.current_input = str(result)
                self.update_display(self.current_input)
                #clears everthing so its ready for next calculation
                self.first_num = None
                self.operation = None
                #display will clear when user enters new number
                self.reset_display = True
            
            #if something goes wrong it shows error instead of crashing
            except Exception as e:
                messagebox.showerror("Error", str(e))
    
    #function for the C button
    def clear(self):
        #resets current number to 0
        self.current_input = "0"
        #erases first number and operation
        self.first_num = None
        self.operation = None
        #updates the screen so the calculator displays 0 
        self.update_display("0")
    
    #function that runs when user clicks on sqaure root
    def square_root(self):
        try:
            #gets number on screen and turns it into float 
            value = float(self.current_input)
            #sends it to the square_root function in the Calc_Class so it does the math
            result = self.calc.square_root(value)
            #if theres an error  it shows popup
            if result == "error":
                messagebox.showerror("Cannot  square root negative number")
            #if it wasnt negative it continues
            else:
                #turns the number to string so it can be displayed 
                self.current_input = str(result)
                self.update_display(self.current_input)
                self.reset_display = True
        except Exception as e:
            messagebox.showerror("Error", str(e))

    #function for squaring numbers
    def square(self):
        try:
            #turns number into float
            value = float(self.current_input)
            #sends it to the square function in Calc_Class
            result = self.calc.square(value)
            self.current_input = str(result)
            self.update_display(self.current_input)
            self.reset_display = True
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    #function for trig operations 
    def trig_function(self, func):
        try:
            value = float(self.current_input)
            
            #checks if user clicked sin button
            if func == "sin":
                #if user clicked on sin it calcualtes sine of the number 
                result = self.calc.sin(value)
            elif func == "cos":
                result = self.calc.cos(value)
            elif func == "tan":
                result = self.calc.tan(value)
            elif func == "arcsin":
                result = self.calc.arcsin(value)
            elif func == "arccos":
                result = self.calc.arccos(value)
            elif func == "arctan":
                result = self.calc.arctan(value)
            #turn answer into string to display 
            self.current_input = str(result)
            self.update_display(self.current_input)
            self.reset_display = True
        #shows error message if anything failed
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    #function starts calculator 
    def run(self):
        #keeps window open until user closes it 
        self.window.mainloop()
