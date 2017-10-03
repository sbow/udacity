# shaun_rainfall.py
# BartonPondRainGaugeData.csv
import csv
import plotly.plotly as py
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np
import plotly
plotly.tools.set_credentials_file(username='shaunb', \
                                  api_key='axSysQJfxBbrK6kvKol7')
# Create datahandler with pandas
import pandas as pd

# datetime - for date
from datetime import datetime

dates = []
rains = []

with open('BartonPondRainGaugeData.csv', 'rb') as csvfile:
    rainreader = csv.reader(csvfile, delimiter = ',')
 
    for entry in rainreader:
        date = entry[0]
        rain = entry[1]

        dates.append(date)
        rains.append(rain)

raintitle = rains.pop(0)
datetitle = dates.pop(0)

rainsfloat = np.array(rains) # convert str to float
rainsfloat = rainsfloat.astype(np.float)

def parseDates(rawDates):
    #date raw: 01/02/2017
    dtdates = []
    for date in rawDates:
        #dd, mm, yy = date.split("/")
        dtdates.append(
            datetime.strptime(date, "%m/%d/%Y")
        )
        #print(date)
    return dtdates

dtdates = parseDates(dates) # return datetime dates
print dtdates[0].strftime('First date %m, %d, %Y')

pddates = pd.to_datetime(dtdates)
df = pd.DataFrame(rainsfloat, index=pddates, columns=list('A'))
#print(df['20170801':'20170831'])   #example, get august 2017 items

print (df[0:3].T)


trace = go.Scatter(
    y = rainsfloat,
    mode = 'markers'
)

data = [trace]

#py.iplot(data, filename='basic-rainfall')
