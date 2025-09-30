import plotly.express as px
import plotly.io as pio  # needed only outside Jupyter (IDLE/console) to force plots to show

# Force browser rendering
pio.renderers.default = "browser"

# Load example dataset
tips = px.data.tips()

# Create scatter plot
fig = px.scatter(
    tips,
    x="total_bill",
    y="tip",
    color="sex",
    title="Scatter Plot of Tips vs Total Bill"
)

fig.show()