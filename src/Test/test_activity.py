import sys
import os.path
from Frontend.Components.Activity import show_all_act, show_top3_act, add_activity, get_detail_act, randomize_recommendation
from Frontend.typeDefs.activity_list import activity_list
import sqlite3
import pytest
import tkinter as tk

dir_path = os.path.dirname(os.path.realpath(__file__))
file_db = dir_path+'\..\Backend\storage.db'

#Testing using PyTest
def test_show_top3_act():
    #Create or connect database activity
    conn = sqlite3.connect(file_db)

    #Create cursor
    c = conn.cursor()

    #Menghitung jumlah record
    c.execute("SELECT COUNT(*) from activity")
    num_row = c.fetchone()[0]

    if (num_row == 0):
        assert show_top3_act() == "Belum ada aktivitas yang dilakukan"
    else:
        #Mengetes bener tidak current activitesnya hanya ditampilkan < 3
        assert show_top3_act().count("\n") <= 3

def test_show_all_act():
    #Create or connect database activity
    conn = sqlite3.connect(file_db)

    #Create cursor
    c = conn.cursor()

    #Menghitung jumlah record
    c.execute("SELECT COUNT(*) from activity")
    num_row = c.fetchone()[0]

    if (num_row == 0):
        assert show_all_act() == "Tidak ada riwayat aktivitas"
    else:
        #Mengetes bener tidak yang ditampilkan itu semua aktivitas yang sudah tercatat
        assert (show_all_act().count("\n") == num_row)

def test_add_activity():
    #Create or connect database activity
    conn = sqlite3.connect(file_db)

    #Create cursor
    c = conn.cursor()

    #Mendapatkan record terakhir dari tabel activity
    c.execute("SELECT * from activity ORDER BY activityId desc LIMIT 1")
    last_record_before = c.fetchall()

    #Menambahkan sebuah record
    add_activity(0)

    #Mengecek apakah record sudah ditambahkan
    #Mendapatkan record terakhir dari tabel activity
    c.execute("SELECT * from activity ORDER BY activityId desc LIMIT 1")
    last_record_after = c.fetchall()

    assert last_record_after != last_record_before

    #Menghapus record yang ditambah untuk testing
    c.execute("DELETE FROM activity WHERE activityId = (SELECT MAX(activityId) FROM activity)")

    #Commit changes
    conn.commit()

    #Close connection
    conn.close()

def test_get_detail_act():
    assert get_detail_act(0) == activity_list()[0][0] + '\n' + activity_list()[0][1] + '\n'

def test_randomize_recommendation():
    before = randomize_recommendation()
    after = randomize_recommendation()

    assert before != after