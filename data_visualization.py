import plotly.graph_objects as go

def plot_security_risk(security_level):
    levels = ['Low', 'Medium', 'High']
    values = [20, 50, 80] if security_level == "Secure" else [80, 50, 20]
    
    fig = go.Figure(
        data=[go.Bar(x=levels, y=values, marker_color=['green', 'yellow', 'red'])]
    )
    fig.update_layout(title="Security Risk Level",
                      xaxis_title="Risk Level",
                      yaxis_title="Percentage",
                      template="plotly_dark")
    fig.show()
