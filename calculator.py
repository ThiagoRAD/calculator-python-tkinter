import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("300x400")
        self.resizable(False, False)
        self.expression = ""
        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self, font=("Arial", 24), borderwidth=2, relief="ridge", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('÷', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('x', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('+', 4, 3), ('=', 4, 2)
        ]

        for (text, row, col) in buttons:
            if text == '=':
                btn = tk.Button(self, text=text, font=("Arial", 18), command=self.calculate, height=2, width=5)
            else:
                btn = tk.Button(self, text=text, font=("Arial", 18), command=lambda t=text: self.on_button_click(t), height=2, width=5)
            btn.grid(row=row, column=col, padx=5, pady=5)

        # Make columns expand equally
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'x':
            self.expression += '*'
        elif char == '÷':
            self.expression += '/'
        else:
            self.expression += str(char)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
            self.expression = result
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")
            self.expression = ""

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
