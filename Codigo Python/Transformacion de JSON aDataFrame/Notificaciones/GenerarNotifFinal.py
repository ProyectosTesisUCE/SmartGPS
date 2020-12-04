import pandas as pd
import pyNotificaciones.EliminarActNotif as delNotif
import pyNotificaciones.ObtenerActNotif as obtAct

#Leer archivos Base 2
df2 = pd.read_pickle("Ntf-V2.pkl")
dfUnDsp2 = pd.read_pickle("NtfDsp1060-V2.pkl")
dfTresDsp2 = pd.read_pickle("NtfDsp1061-1118-1451-V2.pkl")
dfFechas2 = pd.read_pickle("NtfFecha2020-02-03_2020-02-07-V2.pkl")

#Leer archivos Base 3
df3 = pd.read_pickle("Ntf-V3.pkl")
dfUnDsp3 = pd.read_pickle("NtfDsp1060-V3.pkl")
dfTresDsp3 = pd.read_pickle("NtfDsp1061-1118-1451-V3.pkl")
dfFechas3 = pd.read_pickle("NtfFecha2020-02-03_2020-02-07-V3.pkl")

#Eliminar los que actualizaron en base 2
dftresDsp2Final = dfTresDsp2[dfTresDsp2.dspId != 1061]
dftresDsp2Final = dftresDsp2Final[dftresDsp2Final.dspId != 1118]
df2Final = delNotif.deleteNotif(df2)
dfFechas2Final = delNotif.deleteNotif(dfFechas2)

#Obtener solo los que actualizaron app en base 3
r1 = dfTresDsp3.loc[:, 'dspId'] == 1061
s1 = dfTresDsp3.loc[r1]
r2 = dfTresDsp3.loc[:, 'dspId'] == 1118
s2 = dfTresDsp3.loc[r2]
dftresDsp3Final = pd.concat([s1, s2])
df3Final = obtAct.getNotif(df3)
dfFechas3Final = obtAct.getNotif(dfFechas3)

#Unir resultados de las bases
dfFinal = pd.concat([df2Final, df3Final])
dfTresDspFinal = pd.concat([dftresDsp2Final, dftresDsp3Final])
dfFechasFinal = pd.concat([dfFechas2Final, dfFechas3Final])

#Generar pkl y csv
dfFinal.to_csv('NtfTodoFinal.csv')
dfFinal.to_pickle('NtfTodoFinal.pkl')
dfUnDsp3.to_csv('NtfUnDspFinal.csv')
dfUnDsp3.to_pickle('NtfUnDspFinal.pkl')
dfTresDspFinal.to_csv('NtfTresDspFinal.csv')
dfTresDspFinal.to_pickle('NtfTresDspFinal.pkl')
dfFechasFinal.to_csv('NtfFechasFinal.csv')
dfFechasFinal.to_pickle('NtfFechasFinal.pkl')
