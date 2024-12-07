import tkinter as tk

class ToolGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Network Security Tool")
        self.master.geometry("500x500")

        self.label = tk.Label(self.master, text="Network Security Tool", font=("Helvetica", 16))
        self.label.pack()

        self.run_button = tk.Button(self.master, text="Run Anomaly Detection", command=self.run_anomaly_detection)
        self.run_button.pack()

    def run_anomaly_detection(self):
        print("Running anomaly detection...")
