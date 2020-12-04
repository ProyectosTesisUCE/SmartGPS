import pandas as pd
import pyPosicion.ConvertDataFrame as dfC
from os import listdir

ruta = 'D:/tmp/Posicion base 3'
a=1
t = True
dx = pd.DataFrame()
while t:
    arc = "data"+str(a)+" - v3.json"
    t = arc in listdir(ruta)
    if t == False: break
    x = dfC.getDataFrame(ruta+"/"+arc)
    dx = pd.concat([dx, x])
    a += 1
y = dx.drop_duplicates()
print(y)
# Generar csv del dataframe
y.to_pickle('dfV3.pkl')
y.to_csv('dfV3.csv')
