'''
    Python file to process the Psychologist related processing on the database
'''

import sqlite3
import uuid
import os
from datetime import datetime

dir_path = os.path.dirname(os.path.realpath(__file__))
backendSrc = dir_path + "/storage.db"

__addPsychologistSQL = """
    INSERT INTO psikolog VALUES (
        :nama, :asal_kota
    )
"""

__searchPsychologist = """
    SELECT nama 
    FROM psikolog
    WHERE nama LIKE ':nama%'
"""

def addPsychologist(nama, asal_kota) : 
    conn = sqlite3.connect(backendSrc)
    c = conn.cursor()
    c.execute(__addPsychologistSQL, {
        'nama' : nama,
        'asal_kota' : asal_kota
    })  

    #Commit changes
    conn.commit()

    #Close connection
    conn.close()

def searchPsychologist(nama) : 
    conn = sqlite3.connect(backendSrc)
    c = conn.cursor()
    c.execute(__addPsychologistSQL, {
        'nama' : nama
    })  

    #Commit changes
    conn.commit()

    #Close connection
    conn.close()