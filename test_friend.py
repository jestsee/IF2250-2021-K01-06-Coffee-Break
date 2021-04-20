from userSDK import *
import pytest
from user import user

def test_add_user():
    nama = "test"
    dom = "dimana aja boleh"
    hobi = "fangirling"
    u = user(nama,dom,hobi)
    add_user(u)

    # get user yang baru ditambahkan
    usertemp = get_user_by_id(get_last_row_id())
    temp = user(usertemp[1],usertemp[2],usertemp[3])

    # cek sama atau engga
    assert u==temp

    # hapus user yang baru ditambahkan
    c = cursor()
    with c.connection:
        c.execute('DELETE FROM user WHERE nama=? AND dom=? AND hobi=?', (usertemp[1],usertemp[2],usertemp[3]))
    c.connection.close()

def test_add_friend():
    nama = "test"
    dom = "dimana aja boleh"
    hobi = "fangirling"
    u = user(nama,dom,hobi)
    add_user(u)

    # get id dari user yang baru ditambahkan
    id1 = get_last_row_id()
    
    # tambahkan user lagi
    nama = "test"
    dom = "dimana aja boleh"
    hobi = "fangirling"
    u1 = user(nama,dom,hobi)
    add_user(u1)

    # get id dari user yang baru ditambahkan
    id2 = get_last_row_id()

    # add friend
    add_friend(id1,id2)

    # cek apakah id2 merupakan teman dari id1
    friends = get_friends(id1)

    found = False
    for f in friends:
        if(f==u1):
            found = True
            break
    assert found==True

    # hapus user yang baru ditambahkan
    c = cursor()
    with c.connection:
        c.execute('DELETE FROM user WHERE nama=? AND dom=? AND hobi=?', (nama,dom,hobi))
        c.execute('DELETE FROM teman WHERE user_id1=? AND user_id2=?',(id1,id2))
    c.connection.close()

def test_get_user_by_all():
    assert len(get_user_by_all(""))==get_last_row_id()
