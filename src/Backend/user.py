import sqlite3
import uuid
import os
from datetime import datetime

dir_path = os.path.dirname(os.path.realpath(__file__))
backendSrc = dir_path + "/storage.db"

# __getUsernameSQL = """
#     SELECT username FROM aktor
# """


def getUsername(userId) : 
    return userId