from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("output.csv")

fig = px.line(df, x="Date", y='Sales')

fig.update_layout(
    title=dict(
        text = 'Pink Morsel Sales 2018 - 2022'
    ),
    yaxis=dict(
        title=dict(
            text = 'Sales ($)'
        )
    )
)

fig.add_annotation(x='2021-01-15',
                   y=1900,
                   text = "Price rise",
                   showarrow = True,)

fig.add_vline(x='2021-01-15')

app.layout = html.Div([
    dcc.Graph(id="graph", figure=fig),
])


if __name__ == '__main__':
    app.run(debug=True)