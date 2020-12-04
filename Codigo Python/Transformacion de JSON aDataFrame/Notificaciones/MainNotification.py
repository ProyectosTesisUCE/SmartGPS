import pyNotificaciones.ConvertDataFrameNotif as dfC

#Notificaciones base 2
ruta2 = 'D:/tmp/Notificaciones base 2'
arcNtf2 = "notificaciones - v2.json"
arcNtfUnDsp2 = "notificaciones 1060 - v2.json"
arcNtfTresDsp2 = "notificaciones 1061-1118-1451 - v2.json"
arcNtfFechas2 = "notificaciones 2020-02-03_2020-02-07 - v2.json"
#Obtener DataFrame de base 2
xNtf2 = dfC.getDataFrame(ruta2+"/"+arcNtf2)
xNtfUnDsp2 = dfC.getDataFrame(ruta2+"/"+arcNtfUnDsp2)
xNtfTresDsp2 = dfC.getDataFrame(ruta2+"/"+arcNtfTresDsp2)
xNtfFechas2 = dfC.getDataFrame(ruta2+"/"+arcNtfFechas2)
#Generar archivos csv y pkl base 2
xNtf2.to_csv('Ntf-V2.csv')
xNtf2.to_pickle('Ntf-V2.pkl')
xNtfUnDsp2.to_csv('NtfDsp1060-V2.csv')
xNtfUnDsp2.to_pickle('NtfDsp1060-V2.pkl')
xNtfTresDsp2.to_csv('NtfDsp1061-1118-1451-V2.csv')
xNtfTresDsp2.to_pickle('NtfDsp1061-1118-1451-V2.pkl')
xNtfFechas2.to_csv('NtfFecha2020-02-03_2020-02-07-V2.csv')
xNtfFechas2.to_pickle('NtfFecha2020-02-03_2020-02-07-V2.pkl')

#Notificaciones base 3
ruta3 = 'D:/tmp/Notificaciones base 3'
arcNtf3 = "notificaciones - v3.json"
arcNtfUnDsp3 = "notificaciones 1060 - v3.json"
arcNtfTresDsp3 = "notificaciones 1061-1118-1451 - v3.json"
arcNtfFechas3 = "notificaciones 2020-02-03_2020-02-07 - v3.json"
#Obtener DataFrame de base 3
xNtf3 = dfC.getDataFrame(ruta3+"/"+arcNtf3)
xNtfUnDsp3 = dfC.getDataFrame(ruta3+"/"+arcNtfUnDsp3)
xNtfTresDsp3 = dfC.getDataFrame(ruta3+"/"+arcNtfTresDsp3)
xNtfFechas3 = dfC.getDataFrame(ruta3+"/"+arcNtfFechas3)
#Generar archivos csv y pkl base 3
xNtf3.to_csv('Ntf-V3.csv')
xNtf3.to_pickle('Ntf-V3.pkl')
xNtfUnDsp3.to_csv('NtfDsp1060-V3.csv')
xNtfUnDsp3.to_pickle('NtfDsp1060-V3.pkl')
xNtfTresDsp3.to_csv('NtfDsp1061-1118-1451-V3.csv')
xNtfTresDsp3.to_pickle('NtfDsp1061-1118-1451-V3.pkl')
xNtfFechas3.to_csv('NtfFecha2020-02-03_2020-02-07-V3.csv')
xNtfFechas3.to_pickle('NtfFecha2020-02-03_2020-02-07-V3.pkl')
