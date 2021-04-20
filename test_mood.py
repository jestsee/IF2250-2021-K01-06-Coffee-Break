from mood import editMoodDatabase, editJournalDatabase, NextSection, getJournal, getTheDataFromDay
import datetime
import sqlite3
import pytest

today = datetime.date.today()

def test_editMoodDatabase():
    conn = sqlite3.connect('mood.db')
    editMoodDatabase("Happy")
    conn = sqlite3.connect('mood.db')
    sql = "Select * from jurnal where date=?"
    c = conn.cursor()
    strDay = str(today)
    val = (strDay,)
    c.execute(sql,val)
    rows = c.fetchall()
    if(len(rows)>0):
        x = rows[0]
        assert x[2]=="Happy"

def test_editJournalDatabase():
    conn = sqlite3.connect('mood.db')
    editJournalDatabase("Jurnal")
    conn = sqlite3.connect('mood.db')
    sql = "Select * from jurnal where date=?"
    c = conn.cursor()
    strDay = str(today)
    val = (strDay,)
    c.execute(sql,val)
    rows = c.fetchall()
    if(len(rows)>0):
        x = rows[0]
        assert x[3]=="Jurnal"

def test_NextSection1():
    conn = sqlite3.connect('mood.db')
    c = conn.cursor()
    c.execute("SELECT COUNT (*) from jurnal")
    num_row_before = c.fetchone()[0]
    NextSection("Happy")
    c.execute("SELECT COUNT (*) from jurnal")
    num_row_after = c.fetchone()[0]
    assert num_row_after == num_row_before + 1
    conn.commit()
    conn.close()

def test_NextSection2():
    conn = sqlite3.connect('mood.db')
    NextSection("Happy")
    conn = sqlite3.connect('mood.db')
    sql = "Select * from jurnal where date=?"
    c = conn.cursor()
    strDay = str(today)
    val = (strDay,)
    c.execute(sql,val)
    rows = c.fetchall()
    x = rows[0]
    assert x[2]=="Happy"

def test_getJournal():
    conn = sqlite3.connect('mood.db')
    getJournal("Jurnal")
    conn = sqlite3.connect('mood.db')
    sql = "Select * from jurnal where date=?"
    c = conn.cursor()
    strDay = str(today)
    val = (strDay,)
    c.execute(sql,val)
    rows = c.fetchall()
    x = rows[0]
    assert x[3]!="null"

def test_getJournal2():
    conn = sqlite3.connect('mood.db')
    getJournal("Jurnal")
    conn = sqlite3.connect('mood.db')
    sql = "Select * from jurnal where date=?"
    c = conn.cursor()
    strDay = str(today)
    val = (strDay,)
    c.execute(sql,val)
    rows = c.fetchall()
    x = rows[0]
    assert x[3]=="Jurnal"