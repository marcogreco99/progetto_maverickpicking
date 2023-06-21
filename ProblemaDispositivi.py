# ProblemaDispositivi
# Università della Calabria - 2021/2022
# Authors: Marco Greco, Alessandro Covelli
# Contacts: mrcgreco@icloud.com, alessandrocovelli00.ac@gmail.com
import pandas as pd
from sympy import false, true
import re
from pm4py.algo.filtering.pandas.attributes import attributes_filter

dizionario = None
file_output_tracce = None
event_log=None

def initializeOutput(inputp,outputp):
    global dizionario, file_output_tracce

    inputp = inputp.replace("\\", '/')
    inputp = re.sub("\"", "", inputp)

    outputp = outputp.replace("\\", '/')
    outputp = re.sub("\"", "", outputp)

    file_output_tracce = open(outputp+"\\file_output_dispositivi.txt", "w") #creiamo il file di report
    file_output_tracce = open(outputp+"\\file_output_dispositivi.txt", "a")



def filtra(inputp):
    global event_log,dizionario

    inputp = inputp.replace("\\", '/')
    inputp = re.sub("\"", "", inputp)

    event_log = pd.read_csv(inputp, sep = ",", low_memory=false)

    event_log_filtrato = event_log.__getitem__(["Resource", "Activity", "Start Timestamp", "Case ID"])

    dizionario = {}

    for index, rows in event_log_filtrato.iterrows():
        if rows["Resource"] not in dizionario:
            dizionario[rows["Resource"]] = [[rows["Activity"], rows["Start Timestamp"], rows["Case ID"]]]
        else:
            dizionario[rows["Resource"]].append([rows["Activity"], rows["Start Timestamp"], rows["Case ID"]])

def check(k, v):
    global file_output_tracce
    numero_agganci = 0
    numero_richiesteAgganci = 0
    numero_richiestelogIn_logOut = 0
    numero_logIn = 0
    numero_logOut = 0
    for i in range(len(v)):
        if v[i][0] == "AGGANCIO":
            if v[i][2] != "0":
                numero_agganci+=1
        if v[i][0] == "RICHIESTA AGGANCIO":
            numero_richiesteAgganci+=1
        if v[i][0] == "RICHIESTA LOG IN/LOG OUT":
            numero_richiestelogIn_logOut+=1
        if v[i][0] == "LOG IN":
            numero_logIn+=1
        if v[i][0] == "LOG OUT":
            numero_logOut+=1
    if numero_richiesteAgganci > numero_agganci:
        file_output_tracce.write(str(("Risorsa: " + str(k), "Numero agganci: " + str(numero_agganci), "Numero richieste agganci: " + str(numero_richiesteAgganci))))
        file_output_tracce.write("\n")
    if numero_richiestelogIn_logOut > numero_logIn + numero_logOut:
        file_output_tracce.write(str(("Risorsa: " + str(k), "Numero login/logout: " + str(numero_logIn + numero_logOut),
                                      "Numero richieste login/logout: " + str(numero_richiestelogIn_logOut))))
        file_output_tracce.write("\n")
    if numero_logIn != numero_logOut:
        file_output_tracce.write(str(("Risorsa: " + str(k), "Numero log in: " + str(numero_logIn), "Numero log out: " + str(numero_logOut))))
        file_output_tracce.write("\n")


def getDictionary():
    global dizionario
    return dizionario

def checking():
    global file_output_tracce
    for k, v in dizionario.items():
        check(k, v)
    file_output_tracce.close()

def mainFile(inputp,outputp):
    initializeOutput(inputp,outputp)
    filtra(inputp)
    checking()

def mainOutput(inputp):
    filtra(inputp)
    return getDictionary()

