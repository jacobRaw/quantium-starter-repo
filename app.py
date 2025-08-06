from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("output.csv")
df = df.sort_values(by="Date")

# north_df = df[df['Region'] == 'north']
# east_df = df[df['Region'] == 'east']
# south_df = df[df['Region'] == 'south']
# west_df = df[df['Region'] == 'west']

def create_figure(df):
    fig = px.line(df, x="Date", y='Sales', 
                  line_group='Region', 
                  color = 'Region',
                  color_discrete_map={
                      'north': 'red',
                      'east': 'green',
                      'south': 'blue',
                      'west': 'orange'

                    })
    fig.update_layout(
        yaxis=dict(
            title=dict(
                text = 'Sales ($)'
            )
        )
    )
    return fig

fig = create_figure(df)

app.layout = html.Div([
    html.H1(
        children='Pink Morsel Sales 2018 - 2022',
        style={
            'textAlign': 'center',
        }
    ),
    html.Div([
        html.Label('Region'),
        dcc.RadioItems(
            options=['north', 'east', 'south', 'west', 'all'],
            value='all',
            id='region-radio',
            inline=True
        ),
    ],
    style={
        'textAlign': 'center'
    }),
    dcc.Graph(id="graph", figure=fig),
])

# the id is the html component from the layout we are 'watching'
# the component_property is the part of the component the 'property' we are watching for the
# input then we are changing for the output
@callback(
    Output(component_id='graph', component_property='figure'),
    Input(component_id='region-radio', component_property='value')
)
def update_region(region):
    if region == 'all':
        new_fig = create_figure(df)
        return new_fig
    else:
        new_df = df[df['Region'] == region]
        new_fig = create_figure(new_df)
        return new_fig


if __name__ == '__main__':
    app.run(debug=True)