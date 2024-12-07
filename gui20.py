import tkinter as tk
from tkinter import messagebox

def display_gui():
    root = tk.Tk()
    root.title("Network Security Tool")

    def show_alert():
        messagebox.showinfo("Alert", "Shenzhen anomaly detected!")

    tk.Label(root, text="Network Security Tool", font=("Arial", 20)).pack(pady=20)
    tk.Button(root, text="Run Anomaly Detection", command=show_alert).pack(pady=10)
    
    root.mainloop()
