import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("300x400")

        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Entry widget to display the current expression
        entry = tk.Entry(self.master, textvariable=self.result_var, font=("Arial", 24), bd=10, insertwidth=2, width=14, justify="right")
        entry.grid(row=0, column=0, columnspan=4)

        # Buttons for digits and operators
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(self.master, text=text, font=("Arial", 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

    def on_button_click(self,value):
        if value == 'C':
            self.result_var.set('')
        elif value == '=':
            try:
                result = str(eval(self.result_var.get()))
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error","Invalid expression")
        else:
            current_expression = self.result_var.get()
            self.result_var.set(current_expression + value)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
