# coding=utf-8
import pymysql.cursors
import os
import configparser as cparser

# ======== Reading db_config.ini setting ===========
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/db_config.ini"

cf = cparser.ConfigParser()

cf.read(file_path)
host     = cf.get("mysqlconf", "host")
port     = cf.get("mysqlconf", "port")
db       = cf.get("mysqlconf", "db_name")
user     = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")

# ======== MySql base operating ===================

class DB:

    def __init__(self):
        try:
            # Connect to the database
            self.connection = pymysql.connect(host=host,
                                              )
