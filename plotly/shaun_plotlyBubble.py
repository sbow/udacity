# shaun_plotlyBubbly.py - plotly plugin examle, bubble chart on map
# ebola cases
# actually.. that didn't work, requires panda..
# so simpler output
# to view, its stored in my plotly cloud drive:
# shaun_bowman@hotmail.com
# Mon347terminal
# https://plot.ly/organize/home/

import plotly
plotly.tools.set_credentials_file(username='shaunb', \
                                  api_key='axSysQJfxBbrK6kvKol7')

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_ebola.csv')
df.head()

cases = []
colors = ['rgb(239,243,255)','rgb(189,215,231)','rgb(107,174,214)','rgb(33,113,181)']
months = {6:'June',7:'July',8:'Aug',9:'Sept'}

for i in range(6,10)[::-1]:
    cases.append(go.Scattergeo(
            lon = df[ df['Month'] == i ]['Lon'], #-(max(range(6,10))-i),
            lat = df[ df['Month'] == i ]['Lat'],
            text = df[ df['Month'] == i ]['Value'],
            name = months[i],
            marker = dict(
                size = df[ df['Month'] == i ]['Value']/50,
                color = colors[i-6],
                line = dict(width = 0)
            )
        )
    )

cases[0]['text'] = df[ df['Month'] == 9 ]['Value'].map('{:.0f}'.format).astype(str)+' '+\
    df[ df['Month'] == 9 ]['Country']
cases[0]['mode'] = 'markers+text'
cases[0]['textposition'] = 'bottom center'

inset = [
    go.Choropleth(
        locationmode = 'country names',
        locations = df[ df['Month'] == 9 ]['Country'],
        z = df[ df['Month'] == 9 ]['Value'],
        text = df[ df['Month'] == 9 ]['Country'],
        colorscale = [[0,'rgb(0, 0, 0)'],[1,'rgb(0, 0, 0)']],
        autocolorscale = False,
        showscale = False,
        geo = 'geo2'
    ),
    go.Scattergeo(
        lon = [21.0936],
        lat = [7.1881],
        text = ['Africa'],
        mode = 'text',
        showlegend = False,
        geo = 'geo2'
    )
]

layout = go.Layout(
    title = 'Ebola cases reported by month in West Africa 2014<br> \
Source: <a href="https://data.hdx.rwlabs.org/dataset/rowca-ebola-cases">\
HDX</a>',
    geo = dict(
        resolution = 50,
        scope = 'africa',
        showframe = False,
        showcoastlines = True,
        showland = True,
        landcolor = "rgb(229, 229, 229)",
        countrycolor = "rgb(255, 255, 255)" ,
        coastlinecolor = "rgb(255, 255, 255)",
        projection = dict(
            type = 'Mercator'
        ),
        lonaxis = dict( range= [ -15.0, -5.0 ] ),
        lataxis = dict( range= [ 0.0, 12.0 ] ),
        domain = dict(
            x = [ 0, 1 ],
            y = [ 0, 1 ]
        )
    ),
    geo2 = dict(
        scope = 'africa',
        showframe = False,
        showland = True,
        landcolor = "rgb(229, 229, 229)",
        showcountries = False,
        domain = dict(
            x = [ 0, 0.6 ],
            y = [ 0, 0.6 ]
        ),
        bgcolor = 'rgba(255, 255, 255, 0.0)',
    ),
    legend = dict(
           traceorder = 'reversed'
    )
)

fig = go.Figure(layout=layout, data=cases+inset)
py.iplot( fig, validate=False, filename='West Africa Ebola cases 2014' )
