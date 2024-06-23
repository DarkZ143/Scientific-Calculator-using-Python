#Coded by DarkZ 143.........................
import tkinter as tk
from math import *
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("DarkZ Calculator")
        self.root.geometry("390x500+300+80")
        self.root.configure(bg='black')

        self.equation = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry box
        input_frame = tk.Frame(self.root)
        input_frame.pack(expand=True, fill="both")

        input_field = tk.Entry(input_frame, textvariable=self.input_text,bg='black',fg='darkgreen', font=('arial', 26, 'bold'), bd=30, insertwidth=4, width=30, borderwidth=4)
        input_field.grid(row=0, column=0)

        btns_frame = tk.Frame(self.root)
        btns_frame.pack(expand=True, fill="both")

        buttons = [
            '7', '8', '9', '/', 'sqrt',
            '4', '5', '6', '*', 'pow',
            '1', '2', '3', '-', 'log',
            '0', '.', '=', '+', 'ln'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            if button != '':
                tk.Button(btns_frame, text=button, fg='darkgreen',font=('arial', 8, 'bold'), width=10, height=3, bd=0, bg='black', cursor="hand2", command=lambda x=button: self.btn_click(x)).grid(row=row_val, column=col_val, padx=1, pady=1)
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

        tk.Button(btns_frame, text='C', fg='red', width=10, height=3, bd=0, bg='black', cursor="hand2", command=self.clear).grid(row=row_val, column=col_val, padx=1, pady=1)
        tk.Label(root,text='______DarkZ Calculator_____', fg='darkgreen',bg='black', font=('arial', 10, 'bold')).pack()

    def btn_click(self, item):
        if item == "=":
            self.calculate()
        elif item == "sqrt":
            self.equation += "**0.5"
        elif item == "pow":
            self.equation += "**"
        elif item == "log":
            self.equation = f"log10({self.equation})"
        elif item == "ln":
            self.equation = f"log({self.equation})"
        else:
            self.equation += str(item)
        self.input_text.set(self.equation)

    def clear(self):
        self.equation = ""
        self.input_text.set("")

    def calculate(self):
        try:
            result = str(eval(self.equation))
            self.input_text.set(result)
            self.equation = result
        except:
            self.input_text.set("Error")
            self.equation = ""

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(0,0)
   

    calculator = Calculator(root)
    root.mainloop()
    #end of code................
