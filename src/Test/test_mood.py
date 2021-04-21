from Backend.mood import editMoodDatabase, editJournalDatabase, NextSection, getJournal
import sys
import os
import datetime
import sqlite3
import pytest

dir_path = os.path.dirname(os.path.realpath(__file__))
file_db = dir_path+'\..\Backend\storage.db'

today = datetime.date.today()

def test_NextSection1():
    conn = sqlite3.connect(file_db)
    c = conn.cursor()
    c.execute("SELECT COUNT (*) from jurnal")
    num_row_before = c.fetchone()[0]
    print(num_row_before)
    NextSection("Happy")
    c.execute("SELECT COUNT (*) from jurnal")
    num_row_after = c.fetchone()[0]
    rows = c.fetchall()
    conn.commit()
    conn.close()
    if(len(rows)>0):
        assert num_row_after == num_row_before + 1

def test_NextSection2():
    conn = sqlite3.connect(file_db)
    c = conn.cursor()
    sql = "Select * from jurnal where date=?"
    strDay = str(today)
    val = (strDay,)
    c.execute(sql,val)
    conn.commit()
    rows=c.fetchall()
    if(len(rows)<=0):
        NextSection("Happy")
        sql = "Select * from jurnal where date=?"
        strDay = str(today)
        val = (strDay,)
        c.execute(sql,val)
        conn.commit()
        rows=c.fetchall()
        if(len(rows)>0):
            x = rows[0]
            assert x[2]=="Happy"
    conn.close()


def test_getJournal():
    conn = sqlite3.connect(file_db)
    getJournal("Jurnal")
    conn = sqlite3.connect(file_db)
    sql = "Select * from jurnal where date=?"
    c = conn.cursor()
    strDay = str(today)
    val = (strDay,)
    c.execute(sql,val)
    rows = c.fetchall()
    conn.commit()
    conn.close()
    if(len(rows)>0):
        x = rows[0]
        assert x[3]!="null"


def test_getJournal2():
    conn = sqlite3.connect(file_db)
    getJournal("Jurnal")
    conn = sqlite3.connect(file_db)
    sql = "Select * from jurnal where date=?"
    c = conn.cursor()
    strDay = str(today)
    val = (strDay,)
    c.execute(sql,val)
    rows = c.fetchall()
    conn.commit()
    conn.close()
    if(len(rows)>0):
        x = rows[0]
        assert x[3]=="Jurnal"


def test_editMoodDatabase():
    conn = sqlite3.connect(file_db)
    editMoodDatabase("Sad")
    conn = sqlite3.connect(file_db)
    sql = "Select * from jurnal where date=?"
    c = conn.cursor()
    strDay = str(today)
    val = (strDay,)
    c.execute(sql,val)
    rows = c.fetchall()
    conn.commit()
    conn.close()
    if(len(rows)>0):
        x = rows[0]
        assert x[2]=="Sad"

def test_editJournalDatabase():
    conn = sqlite3.connect(file_db)
    editJournalDatabase("JurnalX")
    conn = sqlite3.connect(file_db)
    sql = "Select * from jurnal where date=?"
    c = conn.cursor()
    strDay = str(today)
    val = (strDay,)
    c.execute(sql,val)
    rows = c.fetchall()
    conn.commit()
    conn.close()
    if(len(rows)>0):
        x = rows[0]
        assert x[3]=="JurnalX"



