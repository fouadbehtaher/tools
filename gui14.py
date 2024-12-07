import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class NetworkSecurityToolGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Security Monitoring Tool")

        self.label = tk.Label(self.root, text="Network Security Monitoring")
        self.label.pack()

        self.anomaly_button = tk.Button(self.root, text="Run Anomaly Detection", command=self.run_anomaly_detection)
        self.anomaly_button.pack()

        self.results_text = tk.Text(self.root, height=10, width=50)
        self.results_text.pack()

    def run_anomaly_detection(self):
        
        result = "Anomalies Detected!"  
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, result)

    def plot_graph(self, data):
        fig, ax = plt.subplots()
        ax.plot(data)
        ax.set_title("Network Traffic")
        ax.set_xlabel("Time")
        ax.set_ylabel("Traffic Volume")
        
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()

if __name__ == "__main__":
    root = tk.Tk()
    gui = NetworkSecurityToolGUI(root)
    root.mainloop()
