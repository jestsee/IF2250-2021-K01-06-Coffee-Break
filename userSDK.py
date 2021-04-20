import sqlite3
from user import user

conn = sqlite3.connect('user.db')

c = conn.cursor()

##### CREATE TABLE #####
# Create table buat nampung data user
c.execute('''CREATE TABLE IF NOT EXISTS user
             (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
             nama TEXT, 
             dom TEXT, 
             hobi TEXT)''')

# Create table buat nampung data teman yg fk nya references ke table user
c.execute('''CREATE TABLE IF NOT EXISTS teman
             (user_id1 INTEGER, user_id2 INTEGER,
                PRIMARY KEY (user_id1, user_id2),
                FOREIGN KEY (user_id1) REFERENCES user (user_id),
                FOREIGN KEY (user_id2) REFERENCES user (user_id))''')

def cursor():
    return sqlite3.connect('user.db').cursor()

# menambahkan user ke database
def add_user(user):
    c = cursor()
    with c.connection:
        c.execute("INSERT INTO user (nama, dom, hobi) VALUES (?, ?, ?)", (user.nama, user.dom, user.hobi))
    c.connection.close()
    return c.lastrowid

# return list of user
def get_users():
    c = cursor()
    friends = []
    for row in c.execute('SELECT * FROM user'):
        friends.append(user(row[1],row[2],row[3]))
    c.connection.close()
    return friends

# buat testing
def get_raw_data():
    c = cursor()
    c.execute('SELECT * FROM user')
    return c.fetchall()

# mengembalikan id (pk) dari baris terakhir
def get_last_row_id():
    c = cursor()
    c.execute('''SELECT user_id FROM user WHERE user_id = 
    (SELECT MAX(user_id) FROM user)''')
    return c.fetchone()[0]
    #return c.lastrowid

# mengembalikan id berdasarkan identitas
def get_id(user):
    c = cursor()
    query = user.nama
    query2 = user.dom
    query3 = user.hobi
    c.execute('''
    SELECT user_id FROM user WHERE nama LIKE ? INTERSECT
    SELECT user_id FROM user WHERE dom LIKE ? INTERSECT
    SELECT user_id FROM user WHERE hobi LIKE ?''', (query,query2,query3,))
    return c.fetchone()[0]

# menambahkan userid1 dan userid2 ke tabel teman
def add_friend(myid, friendid):
    try:
        c = cursor()
        with c.connection:
            c.execute("INSERT INTO teman (user_id1,user_id2) VALUES (?, ?)", (myid, friendid))
        c.connection.close()
        return c.lastrowid
    except:
        return -99

# get user by id
def get_user_by_id(id):
    c = cursor()
    query = id
    c.execute('SELECT * FROM user WHERE user_id = ?', (query,))
    return c.fetchone()

# get friends
def get_friends(myid):
    c = cursor()
    query = myid
    friends = []
    temp = c.execute('SELECT * FROM teman WHERE user_id1 = ?', (query,))
    for row in temp:
        temp1 = get_user_by_id(row[1])
        temp2 = user(temp1[1],temp1[2], temp1[3])
        friends.append(temp2)
    c.connection.close()
    return friends

# del friend
def delete_friend(myid,friendid):
    c = cursor()
    with c.connection:
        c.execute('DELETE FROM teman WHERE user_id1=? AND user_id2=?', (myid, friendid))
    rows = c.rowcount
    c.connection.close()
    return rows

''' MODUL PENCARIAN '''
# filter pencarian : nama, dom, hobi
def get_user_by_name(nama):
    c = cursor()
    query = '%'+nama+'%'
    c.execute('SELECT * FROM user WHERE nama LIKE ?', (query,))
    return c.fetchall()

def get_user_by_dom(dom):
    c = cursor()
    query = '%'+dom+'%'
    c.execute('SELECT * FROM user WHERE dom LIKE ?', (query,))
    return c.fetchall()

def get_user_by_hobi(hobi):
    c = cursor()
    query = '%'+hobi+'%'
    c.execute('SELECT * FROM user WHERE hobi LIKE ?', (query,))
    return c.fetchall()

def get_user_by_all(query):
    c = cursor()
    query = '%'+query+'%'
    friends = []
    temp = c.execute('''
    SELECT * FROM user WHERE nama LIKE ? UNION
    SELECT * FROM user WHERE dom LIKE ? UNION
    SELECT * FROM user WHERE hobi LIKE ?''', (query,query,query,))

    for row in temp:
        friends.append(user(row[1],row[2],row[3]))
    c.connection.close()
    return friends

''' driver ( sementara kalo mau nambahin user, lewat sini dulu )'''
# print("buat nambahin user ke database")
# nama = input("Masukan nama : ")
# dom = input("Masukan domisili : ")
# hobi = input("Masukan hobi : ")
# u = user(nama,dom,hobi)
# print(add_user(u))

############################

# cek database sementara
# print(get_raw_data())
# print(get_last_row_id())
# print(get_users())
# print(get_user_by_all('a'))

# test = user("anto","jakarta","bobo")
# print(get_id(test))

# print(get_user_by_id(get_last_row_id()))
# print(get_friends(2))

############################

# user = get_user_by_id(get_last_row_id())
# print(user)