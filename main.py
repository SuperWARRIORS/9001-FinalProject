"""
@Author: huoyufan
@Date: 2025/4/21 10:22
@File: main.py
"""

import tkinter as tk
from Calculator import Calculator
import math

def main():
    # Define an empty window;
    # call the Calculator to show the layout of teh Calculator;
    # keep the window running until we stop it.
    root = tk.Tk()
    Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
