import json
import pandas as pd

def getDataFrame(path):
    with open(path, encoding='utf8') as json_file:
        datos = json.load(json_file)
        ids = []
        pregunta = []
        respuesta = []
        fechaEnvio = []
        fechaRespuesta = []

        for dato in datos:
            id = "dspId" in dato
            if id:
                ids.append(dato['dspId'])
            else:
                ids.append(None)
            preg = "idPregunta" in dato
            if preg:
                pregunta.append(dato['idPregunta'])
            else:
                pregunta.append(None)
            resp = "idRespuesta" in dato
            if resp:
                respuesta.append(dato['idRespuesta'])
            else:
                respuesta.append(None)
            fEnv = "fecEnvio" in dato
            if fEnv:
                fechaEnvio.append(dato['fecEnvio'])
            else:
                fechaEnvio.append(None)
            fResp = "fecRespuesta" in dato
            if fResp:
                fechaRespuesta.append(dato['fecRespuesta'])
            else:
                fechaRespuesta.append(None)

        df = pd.DataFrame()
        df['dspId'] = ids
        df['idPregunta'] = pregunta
        df['idRespuesta'] = respuesta
        df['fecEnvio'] = fechaEnvio
        df['fecRespuesta'] = fechaRespuesta
        return df

