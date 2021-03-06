import sqlite3
from sqlite3 import Error
from pathlib import Path
# Import config file
import sys
import os
sys.path.append('../')
from configs.appconf import conf


# Get path of db
scheduler_db_path = conf["scheduler_db_path"]

# When connect to an SQLite database file that does not exist, SQLite creates a new database
conn = sqlite3.connect(scheduler_db_path)
# Create main table
sql_create_table = """CREATE TABLE IF NOT EXISTS JOBS
    (jobid INTEGER PRIMARY KEY, jobname TEXT NOT NULL, UNLOADED TEXT,
    LOAD_DAY TEXT, LOAD_TIME TEXT, UNLOAD_TIME TEXT, FREQ TEXT
    , ISADHOC TEXT, HOLD TEXT
    );"""
c = conn.cursor()
c.execute(sql_create_table)
