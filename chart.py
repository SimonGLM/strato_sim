import pandas as pd

flights = pd.read_csv("flight.csv",skiprows=1)
flights=flights.apply(slice(2,-1))
flight1=flights.loc["b'Simulation #'"=='b"1.0"']

import plotly.express as px

fig = px.line_mapbox(flight1, lat="lat", lon="lon", color="State", zoom=3, height=300)

fig.update_layout(mapbox_style="stamen-terrain", mapbox_zoom=4, mapbox_center_lat = 41,
    margin={"r":0,"t":0,"l":0,"b":0})

fig.show()

slice()
