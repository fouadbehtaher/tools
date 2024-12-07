import pandas as pd
import matplotlib.pyplot as plt

def temporal_analysis(data):
    df = pd.DataFrame(data, columns=['Timestamp', 'Traffic Volume'])
    plt.plot(df['Timestamp'], df['Traffic Volume'])
    plt.title("Network Traffic Over Time")
    plt.xlabel("Time")
    plt.ylabel("Traffic Volume")
    plt.show()
