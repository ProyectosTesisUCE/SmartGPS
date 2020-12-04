import pandas as pd
from geopy import Point
from geopy.distance  import distance
import datetime, locale
from datetime import datetime, date, timedelta
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score

#***Funcion para filtrar coordenada y así obtener solo los datos
#***de la universidad

def filtroCoord(df):

    horaActual = datetime.now()
    print(horaActual)

    #Eliminar registros con coordenadas vacías
    df = df.dropna(subset=['dspLatitude', 'dspLongitude'])
    df = df.drop(['Unnamed: 0'], axis=1)
    #Eliminar registros que no se encuentren dentro de los limites de la universidad
    df = df.drop(df[((df['dspLatitude'] >= -0.19425) | (df['dspLatitude'] <= -0.20341)) | (
                (df['dspLongitude'] >= -78.49805) | (df['dspLongitude'] <= -78.51377))].index)

    return df

#***Funcion para eliminar datos de prueba, es decir datos anteriores
#***A la fecha en la que empezo la recoleccion de los estudiantes

def filtroFecha(df):

    horaActual = datetime.now()
    print(horaActual)
    #Fecha de inicio para la recoleccion de datos
    fecha_final = datetime.strptime('2019-12-16', '%Y-%m-%d')
    #Elimnacion de columna autogenerada
    df = df.drop(['Unnamed: 0.1'], axis=1)
    #Eliminar registros vacios en las fecha
    df = df.dropna(subset=['dspFechUp'])
    df = df.dropna(subset=['dspFechIn'])
    #Eliminar registros anteriores a la fecha indicada
    df = df.drop(df[df['dspFechUp'] <= str(fecha_final)].index)
    #Eliminar registros duplicados en base al dispositivo la fecha de ingreso de dato
    df = df.drop_duplicates(['dspId', 'dspFechIn'], keep='first')
    #Reseteo indice del dataframe
    df = df.reset_index(drop=True)
    #Obtener cantidad de nulos por columna
    dfNulos = df[
        ['dspGrsX', 'dspGrsY', 'dspGrsZ', 'dspTemp', 'dspWeather', 'dspActivity', 'dspAclX', 'dspAclY', 'dspAclZ', 'dspNumSatel',
         'dspBattery', 'dspStCount', 'dspVeloc', 'dspLatitude', 'dspLongitude']]
    cantidad_nulos = dfNulos.isnull().sum()
    asd = round((cantidad_nulos / df['dspId'].count()) * 100, 2)
    mio = pd.DataFrame(asd)
    print(mio)
    mio.to_csv("nulosDatosFiltrado.csv")
    return df

#***Funcion para separar fechas, calcular distancia geodesica, diferencia
#***de fechas (actual - anterior) y primer etiquetado de movimiento

def distanciaTiempo(df):

    horaActual = datetime.now()
    print(horaActual)

    distanciaMovimiento = 30

    locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

    df = df.dropna(subset=['dspFechUp'])
    df = df.dropna(subset=['dspFechIn'])
    df["dspFechIn"] = pd.to_datetime(df["dspFechIn"])
    df["dspFechUp"] = pd.to_datetime(df["dspFechUp"])

    df["anioIn"] = df["dspFechIn"].dt.strftime("%Y")
    df["mesIn"] = df["dspFechIn"].dt.strftime("%m")
    df["diaIn"] = df["dspFechIn"].dt.strftime("%d")
    df["horaaIn"] = df["dspFechIn"].dt.strftime("%H")
    df["minutoIn"] = df["dspFechIn"].dt.strftime("%M")
    df["segundoIn"] = df["dspFechIn"].dt.strftime("%S")

    df["dia_semana"] = df["dspFechIn"].dt.strftime('%A')

    df["fechaIn"] = df["dspFechIn"].dt.strftime("%Y-%m-%d")
    df["horaIn"] = df["dspFechIn"].dt.strftime("%H:%M:%S")
    df["fechaUp"] = df["dspFechUp"].dt.strftime("%Y-%m-%d")
    df["horaUp"] = df["dspFechUp"].dt.strftime("%H:%M:%S")

    df = df.sort_values(by=['dspId', 'dspFechIn'], ascending=[True, True])
    df = df.reset_index(drop=True)

    ###Calcular la distancia geodesica
    df['point'] = df.apply(lambda row: Point(latitude=row['dspLatitude'], longitude=row['dspLongitude']), axis=1)
    df['point_next'] = df['point'].shift(1)
    df.loc[df['point_next'].isna(), 'point_next'] = None
    df['distGeo'] = df.apply(lambda row: distance(row['point'],
                            row['point_next']).km * 1000 if row['point_next'] is not None else float(0), axis=1)
    df = df.drop('point', axis=1)
    df = df.drop('point_next', axis=1)

    ###Calcular la diferencia de tiempo
    df['horaPiv'] = df['horaIn'].shift(1)
    df.loc[df['horaPiv'].isna(), 'horaPiv'] = None
    df['difTiempo'] = df.apply(lambda row: (
                pd.to_datetime(row['horaIn'], format="%H:%M:%S") - pd.to_datetime(row['horaPiv'],
                            format="%H:%M:%S")).seconds if row['horaPiv'] is not None else float(0), axis=1)
    df = df.drop('horaPiv', axis=1)

    # Consideracion en cambio de día o dispositivo
    df['fechaPiv'] = df['fechaIn'].shift(1)
    df.loc[df['fechaPiv'].isna(), 'fechaPiv'] = None
    df['dspPiv'] = df['dspId'].shift(1)
    df.loc[df['dspPiv'].isna(), 'dspPiv'] = None
    df.loc[(df['fechaIn'] != df['fechaPiv']) | (df['dspId'] != df['dspPiv']), 'distGeo'] = 0.0
    df.loc[(df['fechaIn'] != df['fechaPiv']) | (df['dspId'] != df['dspPiv']), 'difTiempo'] = 0.0
    df = df.drop('fechaPiv', axis=1)
    df = df.drop('dspPiv', axis=1)

    # Calcular la media de la distancia geodesica
    df['distGeo1'] = df['distGeo'].shift(1)
    df.loc[df['distGeo1'].isna(), 'distGeo1'] = None
    df['distGeo2'] = df['distGeo'].shift(-1)
    df.loc[df['distGeo2'].isna(), 'distGeo2'] = 0.0
    df['mediaDistGeod'] = df.apply(lambda row: (row['distGeo'] + row['distGeo1']) / 2 if row['distGeo2'] == 0.0 else (
        (row['distGeo'] + row['distGeo1'] + row['distGeo2']) / 3 if row['distGeo'] != 0.0 else float(0)), axis=1)
    df = df.drop('distGeo1', axis=1)
    df = df.drop('distGeo2', axis=1)

    # Calcular tiempo acumulado (horaUp - horaIn)
    df['tiempoAcumulado'] = df.apply(lambda row: (pd.to_datetime(row['horaUp'], format="%H:%M:%S")
                                    - pd.to_datetime(row['horaIn'], format="%H:%M:%S")).seconds, axis=1)

    # Llenar vacíos y recategorizar el clima
    df['dspAclX'].fillna(1000, inplace=True)
    df['dspAclY'].fillna(1000, inplace=True)
    df['dspAclZ'].fillna(1000, inplace=True)
    df['dspNumSatel'].fillna(-1, inplace=True)
    df['dspStCount'].fillna(-1, inplace=True)
    df['dspBattery'].fillna(-1, inplace=True)
    df['dspVeloc'].fillna(-1, inplace=True)
    df['dspWeather'].fillna(-1, inplace=True)

    df['newWeather'] = df['dspWeather']
    df['newWeather'] = df['newWeather'].replace({"Clear": 1, "Clouds": 2, "Fog": 3, "Mist": 4,
                                             "Smoke": 5, "Drizzle": 6, "Rain": 7, "Thunderstorm": 8})

    return df

#***Funcion para categorizar el nivel de bateria, clima,
#***velocidad y el contador de pasos

def prediccionActividad(df):

    horaActual = datetime.now()
    print(horaActual)

    # Localizamos los datos vacios y los guardamos en un dataframe
    actNaN = df['dspActivity'].isnull()
    act4 = df['dspActivity'] == 4
    datosAPredecir = df.loc[actNaN]
    datosAPredecir2 = df.loc[act4]
    dataPredic = pd.concat([datosAPredecir, datosAPredecir2])

    # Elegimos las columnas que se utilizaran de la data con vacios
    Xvacios = dataPredic[['dspAclX', 'dspAclY', 'dspAclZ', 'dspNumSatel', 'dspLatitude', 'dspLongitude',
                           'horaaIn', 'dspStCount', 'dspBattery', 'dspVeloc', 'newWeather']]

    # Eliminamos la data con vacios del dataframe general
    df = df.dropna(subset=['dspActivity'])
    df = df.drop(df[df['dspActivity'] == 4].index)

    # Elegimos las columnas de entrada y la columna de salida
    X = df[['dspAclX', 'dspAclY', 'dspAclZ', 'dspNumSatel', 'dspLatitude', 'dspLongitude', 'horaaIn',
            'dspStCount', 'dspBattery', 'dspVeloc', 'newWeather']]
    y = df['dspActivity']

    # Sacamos el 10% para pruebas y el 90% para el entrenamiento
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=30)

    # Elegimos el modelo y lo ajustamos
    rfc = RandomForestClassifier(n_estimators=100, random_state=0)
    rfc.fit(X_train, y_train)

    # Realizamos la prediccion de la data de prueba y calculamos la precision
    y_pred = rfc.predict(X_test)
    precision = precision_score(y_test, y_pred, average='micro')

    # Predecimos los datos que tienen vacios
    vacios_pred = rfc.predict(Xvacios)

    # Creamos una nueva columna para almacenar la actividad
    df['newActivity'] = y
    dataPredic['newActivity'] = vacios_pred
    df = pd.concat([df, dataPredic])

    df = df.sort_index()

    # df.to_csv("df3PrediccionNuevaActividad.csv")
    print("Precision del modelo Actividad")
    print(precision)

    return df

#***Modelo Random Forest para predecir la actividad, teniendo como variables
#***de entrada latitud, longitud, contador de pasos, batería, clima y velocidad

def etiquetaMovimiento(df):

    horaActual = datetime.now()
    print(horaActual)

    df['movDist'] = int(1)

    # Variables
    distanciaMovimiento = 40.0
    # distanciaMovimiento2 = 7.0
    tiempoQuieto = 30

    # df.loc[(df['newActivity2'] == 3.0) & ((df['mediaDistGeod'] < distanciaMovimiento) | (tiempoQuieto <= df['tiempoAcumulado'])), 'movDist'] = int(0)
    df.loc[(df['newActivity'] == 3.0), 'movDist'] = int(0)
    df.loc[(df['newActivity'] != 3.0) & (df['newActivity'] != 2.0) & (df['newActivity'] != 0.0) & (
                df['newActivity'] != 1.0) & ((tiempoQuieto <= df['tiempoAcumulado']) | (
                df['mediaDistGeod'] < distanciaMovimiento)), 'movDist'] = int(0)
    df.to_csv('dfDataFinal.csv')

    return df

#***Calculamos un nuevo movimiento considerando la actividad predecida anteriormente, usando
#***la diferencia de tiempo (up - in) y una distancia que varia dependiendo de la acitvidad

def prediccionTemperatura(df):

    horaActual = datetime.now()
    print(horaActual)

    # Localizamos los datos vacios y los guardamos en un dataframe
    actNaN = df['dspTemp'].isnull()
    datosAPredecir = df.loc[actNaN]

    # Elegimos las columnas que se utilizaran de la data con vacios
    Xvacios = datosAPredecir[['dspAclX', 'dspAclY', 'dspAclZ', 'dspNumSatel', 'dspLatitude', 'dspLongitude',
                          'horaaIn', 'dspStCount', 'dspBattery', 'dspVeloc', 'newWeather', 'newActivity']]

    # Eliminamos la data con vacios del dataframe general
    df = df.dropna(subset=['dspTemp'])

    # Elegimos las columnas de entrada y la columna de salida
    X = df[['dspAclX', 'dspAclY', 'dspAclZ', 'dspNumSatel', 'dspLatitude', 'dspLongitude', 'horaaIn',
            'dspStCount', 'dspBattery', 'dspVeloc', 'newWeather', 'newActivity']]
    y = df['dspTemp']

    # Sacamos el 10% para pruebas y el 90% para el entrenamiento
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=30)

    # Elegimos el modelo y lo ajustamos
    rfc = RandomForestClassifier(n_estimators=100, random_state=0)
    rfc.fit(X_train, y_train)

    # Realizamos la prediccion de la data de prueba y calculamos la precision
    y_pred = rfc.predict(X_test)
    precision = precision_score(y_test, y_pred, average='micro')

    # Predecimos los datos que tienen vacios
    vacios_pred = rfc.predict(Xvacios)

    # Creamos una nueva columna para almacenar la actividad
    df['newTemp'] = y
    datosAPredecir['newTemp'] = vacios_pred
    df = pd.concat([df, datosAPredecir])

    df = df.sort_index()

    # df.to_csv("df3PrediccionNuevaActividad.csv")
    print("Precision del modelo Temperatura")
    print(precision)

    return df

#***Aqui hacemos uso de las notificaciones para ello solo tomamos aquellas con
#***la pregunta 1 y calculamos la diferencia de tiempo entre envio y respuesta

def eliminarPocosDatos(df):

    horaActual = datetime.now()
    print(horaActual)

    dsp = df["dspId"].unique()
    cont = 0
    piv = pd.DataFrame()
    for i in dsp:
        r1 = df.loc[:, 'dspId'] == i
        s1 = df.loc[r1]
        fechas = s1["fechaIn"].unique()
        for x in fechas:
            r2 = s1.loc[:, 'fechaIn'] == x
            s2 = pd.DataFrame()
            s2 = s1.loc[r2]
            s2 = s2.reset_index(drop=True)
            if s2['dspId'].count() > 50:
                piv = pd.concat([piv, s2])
            else:
                cont = cont + 1

    piv = piv.reset_index(drop=True)
    print(cont)

    horaActual = datetime.now()
    print(horaActual)

    return piv

#***Aqui se une al dataframe de posicion dos columnas de la data de las notificaciones que son
#***la respuesta y la diferencia de tiempo, tiendo en cuenta las fechas en ambos datafrmes

def sumaTiempo(df):

    horaActual = datetime.now()
    print(horaActual)

    acumulador = 0.0
    sumaTiempo = []

    for y in range(0, len(df)):
        if y != len(df) - 1:
            if (df['movDist'][y] != df['movDist'][y + 1]) | \
                    (df['fechaIn'][y] != df['fechaIn'][y + 1]) | \
                    (df['dspId'][y] != df['dspId'][y + 1]) | \
                    (df['difTiempo'][y + 1] > 7200.0):
                acumulador = acumulador + df['difTiempo'][y] + df['tiempoAcumulado'][y]
                sumaTiempo.append(acumulador)
                acumulador = 0.0
            else:
                acumulador = acumulador + df['difTiempo'][y]
                if df['difTiempo'][y] > 7200.0:
                    acumulador = acumulador - df['difTiempo'][y]
                sumaTiempo.append(0.0)
        else:
            acumulador = acumulador + df['difTiempo'][y] + df['tiempoAcumulado'][y]
            sumaTiempo.append(acumulador)
            acumulador = 0.0

    df['sumaTiempo'] = sumaTiempo

    return df

def etiquetaViajes(df):
    viaje = []

    cont = 1
    tiempoQuieto = 0.0
    tiempoMovimiento = 0.0

    horaActual = datetime.now()
    print(horaActual)

    fin = len(df)

    for y in range(0, fin):
        if df['fechaIn'][y] != df['fechaUp'][y]:
            df = df.drop([y], axis=0)
        else:
            if (df['distGeo'][y] == 0.0) & (df['difTiempo'][y] == 0.0) & (df['mediaDistGeod'][y] == 0.0):
                cont = 1
                tiempoQuieto = 0.0
                tiempoMovimiento = 0.0
                viaje.append(cont)
            else:
                if tiempoQuieto >= 3600.0:
                    cont = cont + 1
                    viaje.append(cont)
                    tiempoQuieto = 0.0
                    tiempoMovimiento = 0.0
                else:
                    if y != fin - 1:
                        if ((df['movDist'][y] == 0) & (df['sumaTiempo'][y] >= 3600.0)) | (
                                df['difTiempo'][y + 1] >= 7200.0):
                            viaje.append(cont)
                            cont = cont + 1
                            tiempoQuieto = 0.0
                            tiempoMovimiento = 0.0
                        else:
                            if (df['movDist'][y] == 0) & (df['sumaTiempo'][y] != 0.0):
                                tiempoQuieto = tiempoQuieto + df['sumaTiempo'][y]
                                viaje.append(cont)
                            elif (df['movDist'][y] == 1) & (df['sumaTiempo'][y] != 0.0):
                                tiempoMovimiento = tiempoMovimiento + df['sumaTiempo'][y]
                                viaje.append(cont)
                            else:
                                viaje.append(cont)
                    else:
                        if (df['movDist'][y] == 0) & (df['sumaTiempo'][y] >= 3600.0):
                            viaje.append(cont)
                            cont = cont + 1
                            tiempoQuieto = 0.0
                            tiempoMovimiento = 0.0
                        else:
                            if (df['movDist'][y] == 0) & (df['sumaTiempo'][y] != 0.0):
                                tiempoQuieto = tiempoQuieto + df['sumaTiempo'][y]
                                viaje.append(cont)
                            elif (df['movDist'][y] == 1) & (df['sumaTiempo'][y] != 0.0):
                                tiempoMovimiento = tiempoMovimiento + df['sumaTiempo'][y]
                                viaje.append(cont)
                            else:
                                viaje.append(cont)

    df['etiquetaViaje'] = viaje

    df = df.reset_index(drop=True)

    df.to_csv("dfDataViajes.csv")

    horaActual = datetime.now()
    print(horaActual)

#***Aqui hacemos uso de las notificaciones para ello solo tomamos aquellas con
#***la pregunta 1 y calculamos la diferencia de tiempo entre envio y respuesta

def limpiarDatosNotificacion(df):

    df["fecEnvio"].fillna("2020-01-30 18:23:10", inplace=True)

    df["fecRespuesta"] = pd.to_datetime(df["fecRespuesta"])
    df["fecEnvio"] = pd.to_datetime(df["fecEnvio"])

    df["fechaRsp"] = df["fecRespuesta"].dt.strftime("%Y-%m-%d %H:%M")

    prgUno = df['idPregunta'] == str(1)
    dfUno = df.loc[prgUno]
    dfUno = dfUno.drop(['Unnamed: 0'], axis=1)

    delDupli = dfUno.drop_duplicates(['dspId', 'fechaRsp'], keep='first')

    delDupli["difTiempo"] = (delDupli["fecRespuesta"] - delDupli["fecEnvio"]).dt.total_seconds()

    return delDupli

#***Aqui se une al dataframe de posicion dos columnas de la data de las notificaciones que son
#***la respuesta y la diferencia de tiempo, tiendo en cuenta las fechas en ambos datafrmes

def unionDataFrame(dfP, dfN):
    dfP["dspFechIn"] = pd.to_datetime(dfP["dspFechIn"])
    dfP["fechaPiv"] = dfP["dspFechIn"].dt.strftime("%Y-%m-%d %H:%M")

    dfN["fecRespuesta"] = pd.to_datetime(dfN["fecRespuesta"])
    dfN["fechaPiv2"] = dfN["fecRespuesta"].dt.strftime("%Y-%m-%d %H:%M")
    dfN["fechaPiv3"] = dfN["fecRespuesta"].dt.strftime("%Y-%m-%d")

    dsp = dfP["dspId"].unique()

    piv = pd.DataFrame()
    for i in dsp:
        rPo = dfP.loc[:, 'dspId'] == i
        sPo = dfP.loc[rPo]
        rNo = dfN.loc[:, 'dspId'] == i
        sNo = dfN.loc[rNo]
        fechas = sPo["fechaIn"].unique()
        for x in fechas:
            rPo2 = sPo.loc[:, 'fechaIn'] == x
            sPo2 = pd.DataFrame()
            sPo2 = sPo.loc[rPo2]
            sPo2 = sPo2.reset_index(drop=True)

            rNo2 = sNo.loc[:, 'fechaPiv3'] == x
            sNo2 = pd.DataFrame()
            sNo2 = sNo.loc[rNo2]
            sNo2 = sNo2.reset_index(drop=True)

            if sPo2.empty:
                print(str(i) + " - " + str(x))
            else:
                resp = []
                difTiemp = []
                for y in range(0, len(sPo2)):
                    if sNo2.empty:
                        resp.append("")
                        difTiemp.append("")
                    else:
                        for j in range(0, len(sNo2)):
                            a = datetime.strptime(sPo2["fechaPiv"][y], "%Y-%m-%d %H:%M")
                            b = datetime.strptime(sNo2["fechaPiv2"][j], "%Y-%m-%d %H:%M")
                            if a == b:
                                resp.append(sNo2["idRespuesta"][j])
                                difTiemp.append(sNo2["difTiempo"][j])
                                break
                        if y == len(resp):
                            resp.append("")
                            difTiemp.append("")
                sPo2["idRespuesta"] = resp
                sPo2["difTiemNotif"] = difTiemp
                piv = pd.concat([piv, sPo2])
    piv = piv.reset_index(drop=True)
    piv = piv.drop(['fechaPiv'], axis=1)

    piv.to_csv('dfPosicionNotificacion.csv')

    return piv

dfP = pd.read_csv("C:/Users/xaviz/PycharmProjects/dataFrame/Uniones/dataFrame Posicion Final/dfTodoFinal.csv")
dfN = pd.read_csv("C:/Users/xaviz/PycharmProjects/dataFrame/Uniones/DataFrameNotificacionesFinal/NtfTodoFinal.csv")

#***Funcion de filtro coordenadas
df = filtroCoord(dfP)
#***Funcion de filtro fecha
df = filtroFecha(df)
#***Llamamos a la primera funcion
df = distanciaTiempo(df)
#***Llamamos a la segunda funcion
df = prediccionActividad(df)
#***Llamamos a la tercera funcion
df = etiquetaMovimiento(df)
#***Llamamos a la cuarta funcion
df = prediccionTemperatura(df)
#***Llamamos a la quinta funcion
df = eliminarPocosDatos(df)
#***Llamamos a la sexta funcion
df = sumaTiempo(df)
#***Colocamos la etiqueta de viajes
df = etiquetaViajes(df)
#***Limpiamos los datos de las notificaciones
dfN = limpiarDatosNotificacion(dfN)
#***Union de los dataframes
df = unionDataFrame(df, dfN)
print("Fin")