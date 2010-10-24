import sqlite3
import os
import sys

class DataConnect:
	
    def __init__(self,db_file=""):
	    if db_file == "":
            db_file = sys.path.append(os.getcwd()) + "/db"

    def connect(self):
        try:
            self.conn = sqlite3.connect(db_file):        
        except e:
            raise e
        else:
            self.conn.execute("CREATE TABLE IF NOT EXISTS 'sprite_map' (file_name,associate_classes,sprite_sheet)")

