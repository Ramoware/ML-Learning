import plotly.express as px
import plotly.io as pio  # needed only outside Jupyter (IDLE/console) so plots display
pio.renderers.default = "browser"  # open plots in browser (interactive)

# Sample data
df = px.data.iris()  # famous Iris dataset

# Scatter plot
fig = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="species",
    size="petal_length",
    title="Plotly Example: Iris Scatterplot"
)

fig.show()
