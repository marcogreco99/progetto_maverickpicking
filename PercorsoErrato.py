# Percorso Errato
# Università della Calabria - 2021/2022
# Authors: Marco Greco, Alessandro Covelli
# Contacts: mrcgreco@icloud.com, alessandrocovelli00.ac@gmail.com
import csv
from pyexpat import version_info
import re
import pm4py
import pandas as pd
from sympy import false, true

dizionario=None
event_log_filtrato=None
event_log=None
dizionario2=None
dizionario3=None
dizionario4=None

def initialize(fl):
    global dizionario, dizionario4, event_log_filtrato, event_log
    #creiamo il file di report
    #file_output_tracce = open("file_output_percorso.txt", "w")
    #file_output_tracce = open("file_output_percorso.txt", "a")

    #leggiamo il file csv e lo convertiamo in Dataframe
    event_log = pd.read_csv(fl, sep = ",", low_memory=false)

    #selezioniamo soltanto tre colonne: case id, posizione, attività
    event_log_filtrato = event_log.__getitem__(["Case ID", "POSIZIONE", "Activity"])

    dizionario = {} #dizionario contiene l'insieme dei case ID delle liste e per ognuno di esse il loro processamento senza le attività di aggancio, destination, delivery ecc.
    dizionario4 = {}

    cont = 0
    for index, rows in event_log_filtrato.iterrows():
        if rows["POSIZIONE"] != "-":
            try:
                if rows["Case ID"] not in dizionario:
                    dizionario[rows["Case ID"]] = [[(list(map(int,rows["POSIZIONE"].split(".")))), rows["Activity"]]]
                    dizionario4[rows["Case ID"]] = [rows["POSIZIONE"], rows["Activity"]]
                else:
                    dizionario[rows["Case ID"]].append([(list(map(int,rows["POSIZIONE"].split(".")))), rows["Activity"]])
                    dizionario4[rows["Case ID"]].append([rows["POSIZIONE"], rows["Activity"]])
            except Exception:
                cont+=1
                if cont == 1:
                    print("Attende prego")
                else:
                    pass




#la funzione check serve a rilevare se nel processamento delle liste l'operatore si è mosso in maneira errata

l2 =[] #contiene tutti i case Id errati rilevati dalla funzione check

def check(k,v,l):

    # v[i][0] = CORSIA-POSTO
    # v[i][0][0] = CORSIA
    # v[i][0][1] = POSTO
    # v[i][1] = ATTIVITA'
    for i in range(len(v)):
        if(v[i][1] == "SALTARIGA" or v[i][1] == "INEVASO" or v[i][1] == "PRELIEVO PARZIALE"):
            l.append(v[i][0])
        if(i!=0):
            temp = True
            if(v[i-1][0][0] > v[i][0][0]): # CORSIA MINORE DELLA PRECEDENTE
                temp = False
            elif(v[i-1][0][0] == v[i][0][0]): #CORSIA UGUALE
                if(v[i][0][0]%2==0 and v[i-1][0][1] < v[i][0][1]): # CORSIA PARI E POSTO MAGGIORE DEL PRECEDENTE
                    temp = False
                elif(v[i][0][0]%2==1 and v[i-1][0][1] > v[i][0][1]): # CORSIA DISPARI E POSTO MINORE DEL PRECEDENTE
                    temp = False
            if(temp == False and v[i][0] not in l and v[i][1] != "RIPRISTINO"):

                l2.append(k)
                return False
    return True

def checking():
    for k,v in dizionario.items():
        check(k,v,[])

def createDictionary2():
    global dizionario2

    dizionario2 = {} #è per la conversione da dataframe a dizionario

    for index, rows in event_log_filtrato.iterrows():
        if rows["Case ID"] not in dizionario2:
            dizionario2[rows["Case ID"]] = [[rows["POSIZIONE"], rows["Activity"]]]
        else:
            dizionario2[rows["Case ID"]].append([rows["POSIZIONE"], rows["Activity"]])


def attivitàPerLista(case):
    return dizionario2.get(str(case))

def createDictionary3():
    global dizionario3

    dizionario3 = {} #contiene le chiavi errate e i loro processamenti

    for i in l2:
        dizionario3[i] = dizionario2.get(i)

def extractFile(path):
    path = path.replace("\\", '/')
    path = re.sub("\"", "", path)
    #trasformiamo il dataframe in file csv
    df = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in dizionario3.items() ]))
    df.to_csv (path+"\\PercorsoErrato.csv", index = False, sep = ";")

    #creiamo un file csv completo
    df2 = pm4py.format_dataframe(event_log, case_id='Case ID', activity_key='Activity', timestamp_key='Start Timestamp')
    tracefilter_log_pos = pm4py.filter_event_attribute_values(df2, "Case ID", [l2[0]], level="case", retain=True)
    for i in range(1, len(l2)):
        tracefilter_log_pos2 = pm4py.filter_event_attribute_values(df2, "Case ID", [l2[i]], level="case", retain=True)
        tracefilter_log_pos = tracefilter_log_pos.merge(tracefilter_log_pos2, how='outer')
    tracefilter_log_pos.to_csv(path+"\\PercorsoErratoCompleto.csv", index = False, sep = ";")

def main(log,pathExport):
    initialize(log)
    checking()
    createDictionary2()
    createDictionary3()
    extractFile(pathExport)
    return dizionario3

def mainperlista(log,idlista):
    initialize(log)
    checking()
    createDictionary2()
    d={}
    d[idlista]=attivitàPerLista(idlista)
    print(d)
    return d

def mainperlog(log):
    initialize(log)
    #print(dizionario)
    return dizionario4


