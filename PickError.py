# PickError
# Università della Calabria - 2021/2022
# Authors: Marco Greco, Alessandro Covelli
# Contacts: mrcgreco@icloud.com, alessandrocovelli00.ac@gmail.com
from pyexpat import version_info
import re


def exportResults(path, richiesta, prelevata, event_log):

    path = path.replace("\\", '/')
    path = re.sub("\"", "", path)
    file_output_tracce = open(path + "\\file_output.txt", "w")  # creiamo il file di report
    file_output_tracce = open(path + "\\file_output.txt", "a")


    for index, rows in event_log.iterrows():
        try:

            if int(str(rows[prelevata])) > int(str(rows[richiesta])):
                file_output_tracce.write(str(index + 2))
                file_output_tracce.write(" , ")
                file_output_tracce.write(str(rows["Case ID"]))
                file_output_tracce.write(" , ")
                file_output_tracce.write(str(rows["Activity"]))
                file_output_tracce.write(" , ")
                file_output_tracce.write(str(rows["Resource"]))
                file_output_tracce.write(" , ")
                file_output_tracce.write(str(rows["Start Timestamp"]))
                file_output_tracce.write(" , ")
                file_output_tracce.write(str(rows[richiesta]))
                file_output_tracce.write(" , ")
                file_output_tracce.write(str(rows[prelevata]))
                file_output_tracce.write("\n")
        except Exception:
            print("Riga " + str(index) + " non contiene un numero")

