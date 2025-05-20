"""
@Author: huoyufan
@Date: 2025/4/21 10:21
@File: Calculator.py
"""

import tkinter as tk
import math
import re

class Calculator:
    # initialization
    def __init__(self, root):
        self.root = root
        self.root.title("scientific calculator")
        self.create_widgets()

    def create_widgets(self):
        # create the input box
        self.entry = tk.Entry(self.root, font="Helvetica 20", borderwidth=3, justify='right')
        # give the input box a grid layout
        self.entry.grid(columnspan=5, padx=8, pady=8, sticky="nsew")

        buttons = [
            ['7', '8', '9', '÷', 'x²'],
            ['4', '5', '6', '*', 'x³'],
            ['1', '2', '3', '-', '√x'],
            ['0', '.', 'ln', '+', '∛x'],
            ['(', ')', 'AC', 'π', 'e'],
            ['sin', 'cos', 'tan', 'x!', '=']
        ]

        # create the button
        for r, row in enumerate(buttons):
            for c, char in enumerate(row):
                btn = tk.Button(self.root, text=char, font="Arial 18", width=5, height=2)
                btn.grid(row=r+1, column=c, sticky="nsew")
                btn.bind("<Button-1>", self.click)

        # auto stretch
        for i in range(len(buttons) + 1):
            # rowconfigure&columnconfigure: built-in method of a Tkinter container object.
            self.root.rowconfigure(i, weight=1)
        for j in range(5):
            self.root.columnconfigure(j, weight=1)


    # event is bind to the left click function
    def click(self, event):
        # get the value of the input box
        current = self.entry.get()
        # get the value of the button
        text = event.widget.cget("text")

        if text == "=":
            try:
                rep_dic = {
                    "÷": "/",
                    "π": "math.pi",
                    "e": "math.e",
                    "sin(": "math.sin(",
                    "cos(": "math.cos(",
                    "tan(": "math.tan(",
                    "²": "**2",
                    "³": "**3"
                }
                for k, v in rep_dic.items():
                    current = current.replace(k, v)

                current = re.sub(r"(\d+)!", r"math.factorial(\1)", current)
                current = re.sub(r'ln\(([^)]+)\)', r'math.log(\1)', current)

                result = eval(current)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif text == "AC":
            self.entry.delete(0, tk.END)
        elif text == 'x²':
            self.entry.insert(tk.END, "²")
        elif text == 'x³':
            self.entry.insert(tk.END, "³")
        elif text == '√x':
            self.entry.insert(tk.END, "** 0.5")
        elif text == '∛x':
            self.entry.insert(tk.END, "** (1/3)")
        elif text == 'π':
            self.entry.insert(tk.END, 'π')
        elif text == 'e':
            self.entry.insert(tk.END, 'e')
        elif text == 'sin':
            self.entry.insert(tk.END, 'sin(')
        elif text == 'cos':
            self.entry.insert(tk.END, 'cos(')
        elif text == 'tan':
            self.entry.insert(tk.END, 'tan(')
        elif text == 'x!':
            self.entry.insert(tk.END, '!')
        elif text == 'ln':
            self.entry.insert(tk.END, 'ln(')
        else:
            self.entry.insert(tk.END, text)

