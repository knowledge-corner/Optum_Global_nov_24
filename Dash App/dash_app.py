from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import mpgdata

# Load Data
df = mpgdata.get_data()
drop_down_list = mpgdata.np.insert(df.origin.unique(), 0, "All")

# Create App object
app = Dash()

app.layout = [
    html.H1(children='MPG Analysis', style={'textAlign':'center', 'color': 'darkslategray'}),
    dcc.Dropdown(drop_down_list, value = 'All', id='dropdown-selection', 
                 clearable = False,
                 style={'width': '50%', 'margin-bottom': '20px', 'margin-left': '10px'}),
    dcc.Graph(id='bar_fig'),
    dcc.Graph(id='scatter_fig'),
    dcc.Graph(id='box_fig'),
]

@callback(
    Output('bar_fig', 'figure'),
    Output('scatter_fig', 'figure'),
    Output('box_fig', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):

    dff = df if value == "All" else df[df.origin==value]

    bar_fig = px.histogram(data_frame=dff, x="origin", y = "horsepower", histfunc="avg", template="simple_white", color = "origin",
            title = "Bar Chart: Average Horsepower by Origin", labels = {"origin" : "", "horsepower" : ""})
    bar_fig.update_layout(yaxis_title = "")

    scatter_fig = px.scatter(data_frame=dff, x="horsepower", y = "mpg", template="simple_white", color = "origin", 
            title = "Scatter Plot: MPG vs. Weight by Origin", labels = {"mpg" : "MPG", "horsepower" : "Horsepower"})

    box_fig = px.box(data_frame=dff, x="origin", y = "mpg", template="simple_white", color = "origin", 
            title = "Box Plot: MPG Distribution by Origin", labels = {"mpg" : "", "origin" : ""})


    return bar_fig, scatter_fig, box_fig

if __name__ == '__main__':
    app.run(debug=True)


