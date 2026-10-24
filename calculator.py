import tkinter #UI library
import math
button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]# operators
top_symbols = ["AC", "+/-", "%"]# functions

row_count = len(button_values) # 5
column_count = len(button_values[0]) # 4

color_light_gray = '#D4D4D2'
color_black = '#1C1C1C'
color_dark_gray = '#505050'
color_orange = '#FF9500'
color_white = 'white'

# window setup
window = tkinter.Tk() # creates the window
window.title("Calculator") # assigns title to window
window.resizable(False, False) # this makes it so user cant drag the size of the window width, height


frame = tkinter.Frame(window) # placing frame inside the window
label = tkinter.Label(frame, text="0", font=("Arial", 45), background=color_black,
                      foreground=color_white, anchor="e", width=column_count) # frame is the parent and then you add properties, "e" moves the label east

label.grid(row=0, column=0, columnspan=column_count, sticky="we") # "spans from west to east"
for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30),
                                width=column_count-1, height=1,
                                command=lambda value=value: button_clicked(value))
        if value in top_symbols:
            button.config(foreground=color_black, background=color_light_gray)
        elif value in right_symbols:
            button.config(foreground=color_white, background=color_orange)
        else:
            button.config(foreground=color_white, background=color_dark_gray)
        button.grid(row=row+1, column=column)
frame.pack()

# A+B, A-B, A*B, A/B
A = "0"
operator = None
B = None

def clear_all():
    global A, B, operator
    A = "0"
    operator = None
    B = None

def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)
def button_clicked(value):
    global right_symbols, top_symbols, label, A, B, operator # prevents local variables

    if value in right_symbols: # operator symbols and =
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_decimal(numA - numB)
                elif operator == "×":
                    label["text"] = remove_zero_decimal(numA * numB)
                elif operator == "÷":
                    label["text"] = remove_zero_decimal(numA / numB)
                clear_all()
        elif value in "+-×÷": #500 +, *
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"
            operator = value
    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"
        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)
        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)
    else:
        # digits or decimal or sq rt
        if value == ".":
            if value not in label["text"]: # prevents .. or 56.6.
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0": # 0 replace 0 with a number like 5 instead of doing 05
                label["text"] = value
            else:
                label["text"] += value # append digit
        elif value == "√":
            result = math.sqrt(float(label["text"]))
            label["text"] = remove_zero_decimal(result)



# center the window
window.update() # updates height and width properties
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

# format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop() # program continues running so window stays open