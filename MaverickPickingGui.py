# MaverickPickingGui
# Università della Calabria - 2021/2022
# Authors: Marco Greco
# Contacts: mrcgreco@icloud.com
from tkinter import *
from tkinter import font as tkFont
from tkinter import filedialog as fd
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
from tkinter.ttk import Treeview
from sympy import false
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import re
import pm4py
import shutil
import os
if os.path.exists('C:/Program Files (x86)/Graphviz2.38/bin'):
    os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin'
import PickError
import PercorsoErrato
import ProblemaDispositivi
import warehouse_animation2

employee_list = []
root = Tk()
root.title("Maverick Picking - Progetto PAC2000A")

root.resizable(False, False)

w = root.winfo_screenheight() - 250
h = root.winfo_screenheight() - 250

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)

ciao=0

root.geometry('%dx%d+%d+%d' % (w, h, x, y))

font1 = tkFont.Font(family='Helvetica', size=int(20 / w), weight='bold')
font2 = tkFont.Font(family='Helvetica', size=int(10 / w), weight='normal')
filename = ""
name = [" "]
directoryname = ""
dictionary3={}

quantità_prelevata = None
quantità_richiesta = None
event_log = None
colonne = None
lists = None
l=None

frm = Frame(root, bg="orange")
frm.pack(expand=1, fill="both")

canvas1 = None
labelfile = None


def importFile():
    global filename, separatore, labelfile, name
    filename = fd.askopenfilename()
    if filename == "":
        return
    e = verificaErratoPrelievo(filename)
    if e == 1:
        mb.showerror(title="Error", message="File errato o separatore diverso da \",\"")
        filename = ""
    name = filename.split(sep="/")
    labelfile.config(text="File importato: " + name[name.__len__() - 1])


def verificaErratoPrelievo(filename):
    global event_log, colonne, lists

    try:

        percorso_file = filename
        separatore = ","
        percorso_file = percorso_file.replace("\\", '/')
        percorso_file = re.sub("\"", "", percorso_file)
        event_log = pd.read_csv(percorso_file, sep=separatore, low_memory=false)
    except Exception:
        return 1

    colonne = event_log.columns.tolist()
    lists = event_log['Case ID'].tolist()

    print(colonne)


def exportfile():
    global directoryname
    directoryname = fd.askdirectory()
    PickError.exportResults(directoryname, quantità_richiesta, quantità_prelevata, event_log)

def exportfileoriginali(df):
    try:
        dfg, start_activities, end_activities = pm4py.discover_dfg(df)
        dn = fd.askdirectory()
        if dn == "":
            return
        dn = dn.replace("\\", '/')
        dn = re.sub("\"", "", dn)
        mb.showwarning(title="Attendere",message="Attendere fino alla comparsa del grafo delle dipendenze ")
        pm4py.view_dfg(dfg, start_activities, end_activities)
        pm4py.save_vis_dfg(dfg, start_activities, end_activities, file_path=dn+"\\PickError.png")
    except Exception:
        mb.showerror(title="Graphviz2.38 not installed",message="Assicurarsi di aver installato Graphviz v.2.38 e che il suo percorso corrisponda al seguente :\n C:/Program Files (x86)/Graphviz2.38/bin")

def exportfilecorretti(df):
    global l
    try:
        #df_filtrato è il file originale senza le tracce errate
        df_filtrato = pm4py.filter_event_attribute_values(df, "Case ID", [l[0]], level="case", retain=False)
        for i in range(1, len(l)):
            df_filtrato = pm4py.filter_event_attribute_values(df_filtrato, "Case ID", [l[i]], level="case", retain=False)
        dn = fd.askdirectory()
        if dn =="":
            return
        dn = dn.replace("\\", '/')
        dn = re.sub("\"", "", dn)
        mb.showwarning(title="Attendere",message="Attendere fino alla comparsa del grafo delle dipendenze ")
        df_filtrato.to_csv(dn+"\\PickErrorTracceCorrette.csv", index=False, sep = ";")
        dfg2, start_activities2, end_activities2 = pm4py.discover_dfg(df_filtrato)
        pm4py.view_dfg(dfg2, start_activities2, end_activities2)
        pm4py.save_vis_dfg(dfg2, start_activities2, end_activities2, file_path=dn+"\\PickErrorTracceCorrette.png")
    except Exception:
        mb.showerror(title="Graphviz2.38 not installed",message="Assicurarsi di aver installato Graphviz v.2.38 e che il suo percorso corrisponda al seguente :\n C:/Program Files (x86)/Graphviz2.38/bin")

def exportfileerrati(df):
    global l
    try:
        df_filtrato2 = pm4py.filter_event_attribute_values(df, "Case ID", [l[0]], level="case", retain=True)
        for i in range(1, len(l)):
            df_filtrato2a = pm4py.filter_event_attribute_values(df, "Case ID", [l[i]], level="case", retain=True)
            df_filtrato2 = df_filtrato2.merge(df_filtrato2a, how='outer')
        dn = fd.askdirectory()
        if dn == "":
            return
        dn = dn.replace("\\", '/')
        dn = re.sub("\"", "", dn)
        mb.showwarning(title="Attendere",message="Attendere fino alla comparsa del grafo delle dipendenze ")
        df_filtrato2.to_csv(dn+"\\PickErroTracceNonCorrette.csv", index = False, sep = ";")
        dfg3, start_activities3, end_activities3 = pm4py.discover_dfg(df_filtrato2)
        pm4py.view_dfg(dfg3, start_activities3, end_activities3)
        pm4py.save_vis_dfg(dfg3, start_activities3, end_activities3, file_path=dn+"\\PickErrorTracceNonCorrette.png")
    except Exception:
        mb.showerror(title="Graphviz2.38 not installed",message="Assicurarsi di aver installato Graphviz v.2.38 e che il suo percorso corrisponda al seguente :\n C:/Program Files (x86)/Graphviz2.38/bin")


def Homepage():
    global filename, labelfile, name, ciao

    for widget in frm.winfo_children():
        widget.destroy()

    ciao=0

    Tk.update(root)

    titolo = Label(frm, text="MAVERICK PICKING", bg="orange", fg="#CD0E0E",
                   font=tkFont.Font(family='Cambria', size=int(50 / w - w / 12), weight='bold'))
    descr = Label(frm, text="PAC2000A - MARCO GRECO E ALESSANDRO COVELLI - UNICAL", bg="orange", fg="#CD0E0E",
                  font=tkFont.Font(family='Fixedsys', size=int(w / 60), weight='bold'))

    titolo.pack(side=TOP, pady=(h / 10, 0))
    descr.pack(side=BOTTOM)

    buttonFrame = Frame(frm, bg="")
    buttonFrame.place(in_=frm, anchor="c", relx=.5, rely=.5)

    btn1 = Button(buttonFrame, text="Import Csv", command=lambda: importFile(), height=2, width=45, font=font1,
                  bg="Yellow")
    btn1.grid(row=0, column=0)
    btn2 = Button(buttonFrame, text="Pick Error", command=lambda: PickErrorMain(), height=2, width=45, font=font1,
                  bg="Yellow")
    btn2.grid(row=1, column=0, pady=(10, 0))
    btn3 = Button(buttonFrame, text="Path Error & Emulation", command=lambda:PathErrorMain(), height=2, width=45, font=font1, bg="Yellow")
    btn3.grid(row=2, column=0, pady=(10, 0))
    btn4 = Button(buttonFrame, text="Devices error", command=lambda:mainProblemaDispositivi(), height=2, width=45, font=font1, bg="Yellow")
    btn4.grid(row=3, column=0, pady=(10, 0))
    labelfile = Label(buttonFrame, text="File importato: " + name[name.__len__() - 1], bg="orange",
                      font=tkFont.Font(family='Helvetica', size=int(w / 50), weight='bold'))
    labelfile.grid(row=4, column=0, pady=(10, 0))


def drawCanvas():
    global canvas1
    canvasFrame = Frame(frm, bg="")
    canvasFrame.place(in_=frm, anchor="c", relx=.5, rely=.5)
    canvas1 = Canvas(canvasFrame, width=400, height=300, bg="orange")
    canvas1.place(relx=0.5, rely=0.5, anchor=CENTER)
    canvas1.pack()


def checkPickError(el, variable, variable2):
    global quantità_richiesta, quantità_prelevata

    quantità_richiesta = variable.get()
    quantità_prelevata = variable2.get()
    mb.showwarning(title="Loading",message="ATTENDERE PREGO... ANCHE SE NON RISPONDE NON CHIUDERE IL PROGRAMMA!!")
    showResults(el)


def showResults(el):
    for widget in frm.winfo_children():
        widget.destroy()
    global employee_list, quantità_prelevata, quantità_richiesta, l

    drawCanvas()
    l=[]
    canvas1['width'] = 570
    canvas1['height'] = 570
    canvas1['highlightthickness'] = 0

    tableFrame = Frame(canvas1)

    tree = Treeview(tableFrame, selectmode='browse', height=20)
    tree.pack(side='top')

    vscrollbar = Scrollbar(tableFrame, orient=VERTICAL)
    vscrollbar.pack(side=RIGHT, fill=Y)
    vscrollbar.config(command=tree.yview)
    tree.config(yscrollcommand=vscrollbar.set)

    tree.pack(side=LEFT, expand=True, fill=BOTH)

    tree["column"] = (
    "Indice Riga", "Case id", "Operazione", "Risorsa", "Timestamp", "Risorse Richieste", "Risorse Prelevate")
    tree['show'] = 'headings'

    tree.column("Indice Riga", width=65, anchor='c')
    tree.heading("Indice Riga", text="INDICE RIGA")
    tree.column("Case id", width=62, anchor='c')
    tree.heading("Case id", text="CASE ID")
    tree.column("Operazione", width=75, anchor='c')
    tree.heading("Operazione", text="OPERAZIONE")
    tree.column("Risorsa", width=60, anchor='c')
    tree.heading("Risorsa", text="RISOSRSA")
    tree.column("Timestamp", width=133, anchor='c')
    tree.heading("Timestamp", text="TIMESTAMP")
    tree.column("Risorse Richieste", width=79, anchor='c')
    tree.heading("Risorse Richieste", text="Q.RICHIESTA")
    tree.column("Risorse Prelevate", width=81, anchor='c')
    tree.heading("Risorse Prelevate", text="Q.PRELEVATA")

    for index, rows in el.iterrows():

        try:
            if int(str(rows[quantità_prelevata])) > int(str(rows[quantità_richiesta])):
                tree.insert("", 'end',
                            values=(str(index + 2), str(rows["Case ID"]), str(rows["Activity"]), str(rows["Resource"]),
                                    str(rows["Start Timestamp"]), str(rows[quantità_richiesta]),
                                    str(rows[quantità_prelevata])))
                l.append(str(rows["Case ID"]))

        except Exception:
            # print("Riga "+str(index)+ " non contiene un numero")
            print(h)


    #df è il file originale con le colonne rinominate
    df = pm4py.format_dataframe(el, case_id='Case ID', activity_key='Activity', timestamp_key='Start Timestamp')

    canvas1.create_window((1, 1), window=tableFrame, anchor=("nw"))

    home = Button(frm, text="Torna alla Home", command=lambda: Homepage(), height=1, width=35, font=font2,
                  bg="Yellow")
    home.pack(side=BOTTOM, pady=(0, 3))

    export = Button(frm, text="Grafo delle dipendenze - Tracce errate", command=lambda: exportfileerrati(df), height=1, width=35, font=font2,
                    bg="Yellow")
    export.pack(side=BOTTOM, pady=(0, 0))

    export2 = Button(frm, text="Grafo delle dipendenze - Tracce corrette", command=lambda: exportfilecorretti(df), height=1, width=35, font=font2,
                    bg="Yellow")
    export2.pack(side=BOTTOM, pady=(0, 0))

    export3 = Button(frm, text="Grafo delle dipendenze - Tracce originali", command=lambda: exportfileoriginali(df), height=1, width=35, font=font2,
                bg="Yellow")
    export3.pack(side=BOTTOM, pady=(0, 0))



    ris = Label(frm, text="Sono presenti " + str(len(tree.get_children())) + " errori", bg="orange",
                font=tkFont.Font(family='Helvetica', size=int(w / 50), weight='bold'))
    if h > 900:
        ris.pack(side=BOTTOM, pady=(0, (h / 4) - (h / 30) - 40))
    else:
        ris.pack(side=BOTTOM, pady=(0, 6))


def drawEntities(el):
    l2 = Label(canvas1, text="Inserisci il campo della colonna qtà. richiesta:", bg="orange")
    l2.grid(row=0, column=0)
    variable = StringVar(canvas1)
    try:
        variable.set(colonne[0])  # default value
    except Exception:
        print(colonne[0])
    w = OptionMenu(canvas1, variable, *colonne)
    # w.pack()
    w.grid(row=1, column=0)

    l3 = Label(canvas1, text="Inserisci il campo della colonna qtà. prelevata:", bg="orange")
    l3.grid(row=2, column=0)
    variable2 = StringVar(canvas1)
    try:
        variable2.set(colonne[0])  # default value
    except Exception:
        print(colonne[0])
    w2 = OptionMenu(canvas1, variable2, *colonne)
    # w.pack()
    w2.grid(row=3, column=0)
    button = Button(canvas1, text="Start", command=lambda: checkPickError(el, variable, variable2), height=1, width=25,
                    font=font2,
                    bg="Yellow")
    button2 = Button(canvas1, text="Torna alla Home", command=lambda: Homepage(), height=1, width=25,
                    font=font2,
                    bg="Yellow")


    button.grid(row=4, column=0)
    button2.grid(row=5,column=0)

    canvas1.create_window(200, 80, window=l2)
    canvas1.create_window(200, 110, window=w)
    canvas1.create_window(200, 140, window=l3)
    canvas1.create_window(200, 170, window=w2)
    canvas1.create_window(200, 220, window=button)
    canvas1.create_window(200, 260, window=button2)


def PickErrorMain():
    global filename,event_log
    if filename == "":
        mb.showerror(title="File Error", message="Importare prima il file csv")
        return
    event_log2=event_log
    indexNames = event_log2[(event_log2['Activity'] == "RIPRISTINO") |
                           (event_log2['Activity'] == "LOG IN") |
                           (event_log2['Activity'] == "LOG OUT") |
                           (event_log2['Activity'] == "RICHIESTA LOG IN/LOG OUT") |
                           (event_log2['Activity'] == "RICHIESTA AGGANCIO") |
                           (event_log2['Activity'] == "RESP_REFDATA")].index
    event_log2 = event_log2.drop(indexNames, inplace=False)

    for widget in frm.winfo_children():
        widget.destroy()
    drawCanvas()
    drawEntities(event_log2)


def PathErrorMain():
    if filename == "":
        mb.showerror(title="File Error", message="Importare prima il file csv")
        return

    for widget in frm.winfo_children():
        widget.destroy()

    Tk.update(root)

    buttonFrame = Frame(frm, bg="")
    buttonFrame.place(in_=frm, anchor="c", relx=.5, rely=.5)

    btn1 = Button(buttonFrame, text="Start & Export files", command=lambda: startAndExport(), height=2, width=45, font=font1,
                  bg="Yellow")
    btn1.grid(row=0, column=0)
    btn3 = Button(buttonFrame, text="Emulation by List", command=lambda:emulationbylist(), height=2, width=45, font=font1, bg="Yellow")
    btn3.grid(row=1, column=0, pady=(10, 0))
    btn4 = Button(buttonFrame, text="Torna alla home", command=lambda:Homepage(), height=2, width=45, font=font1, bg="Yellow")
    btn4.grid(row=2, column=0, pady=(10, 0))
    btn5 = Button(buttonFrame, text="Read me", command=lambda:mb.showinfo(title="Read me", message="Start & Exporting file: Trova "
                                                                                                   "le liste che effettuano percorsi errati e li salva su file"
                                                                                                   "\nPath Error Emulation: Emula il percorso degli operatori "
                                                                                                   "delle liste errate (effettuare prima lo start & exporting file)"
                                                                                                   "\nEmulation by List: emula il percorso dell'operatore della lista scelta"), height=2, width=8, font=font1, bg="Yellow")
    btn5.grid(row=4, column=0, pady=(70, 0))


def outputPath():
    global canvas1,dictionary3

    for widget in frm.winfo_children():
        widget.destroy()


    drawCanvas()

    canvas1['width'] = 570
    canvas1['height'] = 570
    canvas1['highlightthickness'] = 0

    tableFrame=Frame(canvas1)

    tree = Treeview(tableFrame, selectmode='browse', height=20)
    tree.pack(side='top')

    vscrollbar = Scrollbar(tableFrame, orient=VERTICAL)
    vscrollbar.pack(side=RIGHT, fill=Y)
    vscrollbar.config(command=tree.yview)
    tree.config(yscrollcommand=vscrollbar.set)

    tree.pack(side=LEFT, expand=True, fill=BOTH)

    tree["column"] = (
        "caseidlisteerrate")
    tree['show'] = 'headings'

    tree.column("caseidlisteerrate", width=556, anchor='c')
    tree.heading("caseidlisteerrate", text="CASE ID LISTE ERRATE")

    for k in dictionary3:
        tree.insert("",'end',values=(str(k)))

    canvas1.create_window((1, 1), window=tableFrame, anchor=("nw"))

    home = Button(frm, text="Torna alla Home", command=lambda: Homepage(), height=1, width=35, font=font2,
                  bg="Yellow")
    home.pack(side=BOTTOM, pady=(0, 3))

    export = Button(frm, text="Path Error Emulation", command=lambda: PathErrorEmulation(), height=1, width=35, font=font2,
                    bg="Yellow")
    export.pack(side=BOTTOM, pady=(0, 0))


def startAndExport():
    global dictionary3,ciao
    mb.showinfo(title="Seleziona directory",message="Selezionare directory dove salvare i files di output")
    pathE = fd.askdirectory()
    if pathE == "":
        return
    mb.showwarning(title="Loading",message="ATTENDERE PREGO... ANCHE SE NON RISPONDE NON CHIUDERE IL PROGRAMMA!!")
    dictionary3=PercorsoErrato.main(filename,pathE)
    mb.showinfo(title="Loading Completed", message="Caricamento completato")
    outputPath()
    ciao=1

def PathErrorEmulation():
    global dictionary3, ciao
    if ciao==0:
        mb.showerror(title="Error", message="Effettuare prima Start & Export Files")
        return
    warehouse_animation2.main(dictionary3)
    ciao=0

def emulationbylist():
    global lists
    idlist=sd.askstring(title="Input List",prompt="Inserisci ID lista")
    if idlist=="":
        return
    if idlist in lists:
        mb.showwarning(title="Loading",message="ATTENDERE PREGO... ANCHE SE NON RISPONDE NON CHIUDERE IL PROGRAMMA!!")
        di=PercorsoErrato.mainperlista(filename,idlist)
    else:
        mb.showerror(title="Error",message="Non è presente nessuna lista con questo Case ID")
        return

    warehouse_animation2.main(di)
    idlist=None

def mainProblemaDispositivi():
    global filename
    if filename == "":
        mb.showerror(title="File Error", message="Importare prima il file csv")
        return

    for widget in frm.winfo_children():
        widget.destroy()

    Tk.update(root)

    buttonFrame = Frame(frm, bg="")
    buttonFrame.place(in_=frm, anchor="c", relx=.5, rely=.5)

    btn1 = Button(buttonFrame, text="Start", command=lambda:startdispositivi() , height=2, width=45, font=font1,
                  bg="Yellow")
    btn1.grid(row=0,column=0)
    btn2 = Button(buttonFrame, text="Torna alla Home", command=lambda:Homepage() , height=2, width=45, font=font1,
                  bg="Yellow")
    btn2.grid(row=1,column=0, pady=(10, 0))

def showResultsDevices(d):
    global canvas1

    for widget in frm.winfo_children():
        widget.destroy()


    drawCanvas()

    canvas1['width'] = 570
    canvas1['height'] = 570
    canvas1['highlightthickness'] = 0

    tableFrame=Frame(canvas1)

    tree = Treeview(tableFrame, selectmode='browse', height=20)
    tree.pack(side='top')

    vscrollbar = Scrollbar(tableFrame, orient=VERTICAL)
    vscrollbar.pack(side=RIGHT, fill=Y)
    vscrollbar.config(command=tree.yview)
    tree.config(yscrollcommand=vscrollbar.set)

    tree.pack(side=LEFT, expand=True, fill=BOTH)

    tree["column"] = (
        "Risorsa", "Agganci", "Agganci richiesti", "N.login", "N.logout", "N.login/logout", "Login/logout richiesti")
    tree['show'] = 'headings'

    tree.column("Risorsa", width=65, anchor='c')
    tree.heading("Risorsa", text="RISORSA")
    tree.column("Agganci", width=62, anchor='c')
    tree.heading("Agganci", text="AGGANCI")
    tree.column("Agganci richiesti", width=113, anchor='c')
    tree.heading("Agganci richiesti", text="AGGANCI RICHIESTI")
    tree.column("N.login", width=55, anchor='c')
    tree.heading("N.login", text="N.LOGIN")
    tree.column("N.logout", width=67, anchor='c')
    tree.heading("N.logout", text="N.LOGOUT")
    tree.column("N.login/logout", width=84, anchor='c')
    tree.heading("N.login/logout", text="N.LOGIN/OUT")
    tree.column("Login/logout richiesti", width=110, anchor='c')
    tree.heading("Login/logout richiesti", text="LOGIN/OUT RICHIESTI")


    for k, v in d.items():
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
            tree.insert("",'end',values=(str(k),str(numero_agganci),str(numero_richiesteAgganci),"-","-","-","-"))
        if numero_richiestelogIn_logOut > numero_logIn + numero_logOut:
            tree.insert("",'end',values=(str(k),"-","-","-","-",str(numero_logIn + numero_logOut),str(numero_richiestelogIn_logOut)))
        if numero_logIn != numero_logOut:
            tree.insert("",'end',values=(str(k),"-","-",str(numero_logIn),str(numero_logOut),"-","-"))

    canvas1.create_window((1, 1), window=tableFrame, anchor=("nw"))

    home = Button(frm, text="Torna alla Home", command=lambda: Homepage(), height=1, width=35, font=font2,
                      bg="Yellow")
    home.pack(side=BOTTOM, pady=(0, 3))

    export = Button(frm, text="Export files", command=lambda: exportdispositivi(), height=1, width=35, font=font2,
                    bg="Yellow")
    export.pack(side=BOTTOM, pady=(0, 0))

    print("DEBUGGGGGGGG")



def exportdispositivi():
    mb.showinfo(title="Seleziona directory",message="Selezionare directory dove salvare i files di output")
    pathE = fd.askdirectory()
    if pathE=="":
        return
    mb.showwarning(title="Loading",message="ATTENDERE PREGO... ANCHE SE NON RISPONDE NON CHIUDERE IL PROGRAMMA!!")
    ProblemaDispositivi.mainFile(filename,pathE)
    mb.showinfo(title="Loading Completed", message="Caricamento completato")

def startdispositivi():
    mb.showwarning(title="Loading",message="ATTENDERE PREGO... ANCHE SE NON RISPONDE NON CHIUDERE IL PROGRAMMA!!")
    diz = ProblemaDispositivi.mainOutput(filename)
    showResultsDevices(diz)


Homepage()

root.mainloop()
