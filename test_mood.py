from mood import editMoodDatabase, editJournalDatabase, NextSection, getJournal
import sqlite3
import pytest

today = datetime.date.today()

def test_editMoodDatabase():
    conn = sqlite3.connect('mood.db')
    c = conn.cursor()
    record = c.fetchall()
    editMoodDatabase("Happy")
    c.execute("SELECT * from jurnal where date = " + today)
    assert c.fetchone()[2]=="Happy"
    conn.commit()
    conn.close()

def test_editJournalDatabase():
    conn = sqlite3.connect('mood.db')
    c = conn.cursor()
    record = c.fetchall()
    editJournalDatabase("Jurnal")
    c.execute("SELECT * from jurnal where date = " + today)
    assert c.fetchone()[3]=="Jurnal"
    conn.commit()
    conn.close()

def test_NextSection():
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

def test_getJournal():
    conn = sqlite3.connect('mood.db')
    c = conn.cursor()
    getJournal("Jurnal")
    c.execute("SELECT * from jurnal where date = " + today)
    assert c.fetchone()[3]!=null
    conn.commit()
    conn.close()