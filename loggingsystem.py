import os
import csv
from config.config import LOGSYSTEM_PATH, DEBUG

def writeLog(row1, row2, row3, row4, row5, row6, row7):
    '''write or create csv file'''

    with open(LOGSYSTEM_PATH, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow([row1,
                         row2, 
                         "=\"" + row3 + "\"", # converting to correct format for float values
                         "=\"" + row4 + "\"", 
                         "=\"" + row5 + "\"", 
                         row6, 
                         row7])

def logging():
    '''logging system | create'''

    if not os.path.isfile(LOGSYSTEM_PATH):
        if DEBUG: print("creating new csv file..")
        writeLog("Nr.", "Portionsmenge", "Kcal", "Fett", "Zucker", "Zeit", "Datum")
    else:
        print("logfile already exists")