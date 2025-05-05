import tkinter as tk
from tkinter import messagebox

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x420")

        # Entry widget to display input and results
        self.display = tk.Entry(root, width=20, font=('Arial', 16), bd=5, insertwidth=2, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Button layout with Backspace
        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', '←'
        ]

        # Create and place buttons
        row = 1
        col = 0
        for button in self.buttons:
            cmd = lambda x=button: self.click(x)
            tk.Button(root, text=button, width=5, height=2, font=('Arial', 14), command=cmd).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def click(self, char):
        if char == 'C':
            self.display.delete(0, tk.END)
        elif char == '←':
            current_text = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, current_text[:-1])
        elif char == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero!")
                self.display.delete(0, tk.END)
            except Exception:
                messagebox.showerror("Error", "Invalid input!")
                self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, char)

# Create and run the GUI
root = tk.Tk()
app = CalculatorGUI(root)
root.mainloop()
