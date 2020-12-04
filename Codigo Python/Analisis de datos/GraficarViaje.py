import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
from pyproj import Transformer
import mplleaflet
import geopandas
from IPython.display import display, Image

df = pd.read_csv("dfPosicionViajes.csv")

#Ingresar id dispositivo
dsp = 1060
#Ingresar año
anio = 2020
#Ingresar mes
mes = 1
#Ingresar dia
dia = 15
#Ingresar numero de viaje
viaje = 1

#***Filtro dispositivo
r1 = df.loc[:, 'dspId'] == dsp
df2 = df.loc[r1]
#***Filtro año
r1 = df2.loc[:, 'anioIn'] == anio
df2 = df2.loc[r1]
#***Filtro mes
r1 = df2.loc[:, 'mesIn'] == mes
df2 = df2.loc[r1]
#***Filtro dia
r1 = df2.loc[:, 'diaIn'] == dia
df2 = df2.loc[r1]
#***Filtro viaje
r1 = df2.loc[:, 'etiquetaViaje'] == viaje
df2 = df2.loc[r1]
#***Eliminar puntos quieto
r1 = df2['varGrafico'].isnull()
df2 = df2.loc[r1]
#***Calculo de tiempo
r1 = df2['sumaTiempo'] != 0.0
tiempo = df2.loc[r1]
#Movimiento
r1 = tiempo['movDist'] == 1
tiempoMov = tiempo[r1]
#Quito
r1 = tiempo['movDist'] == 0
tiempoQuiet = tiempo[r1]

tiempoTotalMov = tiempoMov['sumaTiempo'].sum()
tiempoTotalQuiet = tiempoQuiet['sumaTiempo'].sum()

print("Tiempo de movimiento:", round(tiempoTotalMov/60, 0), "minutos")
print("Tiempo de quieto:", round(tiempoTotalQuiet/60, 0), "minutos")


transformer = Transformer.from_crs('epsg:4269','epsg:4326',always_xy=True)
points = list(zip(df2['dspLongitude'], df2['dspLatitude']))
coordsWgs = np.array(list(transformer.itransform(points)))
df2['newLon'] = coordsWgs[:, 0]
df2['newLat'] = coordsWgs[:, 1]

line_plot_fig, line_plot_ax = plt.subplots(figsize=(12,9))
##line_plot_ax.plot(df2['newLon'], df2['newLat'], 'blue', linewidth=3)
line_plot_ax.plot(df2['newLon'], df2['newLat'], 'r.')
#plt.show()
#mplleaflet.display(fig=line_plot_fig)
mplleaflet.show(fig=line_plot_fig, path='map.html')
