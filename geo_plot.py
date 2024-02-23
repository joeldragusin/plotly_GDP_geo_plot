import chart_studio.plotly as py
#import plotly.plotly as py DOESN'T WORK ANYMORE!
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot

init_notebook_mode(connected=True)


df=pd.read_csv('2014_World_GDP.csv')
df.head()


data = dict(
	type='choropleth',
    locations=df['CODE'],
    z=df['GDP (BILLIONS)'],
    text=df['COUNTRY'],
    colorbar= {'title': 'GDP in Billions USD'}
    )


layout = dict(
	title='2014 Global GDP',
    geo=dict(
    	showframe=False,
    	projection_type='natural earth'
    	)
    )


choromap3=go.Figure(data=[data], layout=layout)
plot(choromap3)
