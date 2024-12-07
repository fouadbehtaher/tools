import tkinter as tk
from tkinter import messagebox

class NetworkSecurityToolGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Security Tool")
        self.root.geometry("600x400")

        self.label = tk.Label(root, text="Network Security Monitoring")
        self.label.pack()

        self.run_button = tk.Button(root, text="Run Analysis", command=self.run_analysis)
        self.run_button.pack()

    def run_analysis(self):
        messagebox.showinfo("Analysis", "Analysis is running...")
