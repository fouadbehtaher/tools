import plotly.express as px

def plot_network_data(data):
    fig = px.line(data, x='time', y='traffic', title='Network Traffic Over Time')
    fig.show()
