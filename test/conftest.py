import os
os.environ['RUN_ENV'] = 'test'

from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
engine = create_engine("mysql+pymysql://admin:Software9525*@database-bpet.csro2nol6a13.us-east-1.rds.amazonaws.com:3306/bpet_db",  poolclass=NullPool)

def postgresql_connection():
    con = engine
    return con

def delete_database():

    sql_drop_db = f"DROP DATABASE IF EXISTS test_bpet_db"
    con = postgresql_connection()
    con.execute(sql_drop_db)
    con.dispose()

def create_database():
    sql_create_db = f"CREATE DATABASE test_bpet_db;"

    con = postgresql_connection()
    con.execute(sql_create_db)
    con.dispose()
    
def create_table():
    sql_create_db = f"CREATE TABLE test_users (id int NOT NULL AUTO_INCREMENT,name varchar(255) DEFAULT NULL,email varchar(255) DEFAULT NULL,password varchar(255) DEFAULT NULL,PRIMARY KEY (id))"
    con = postgresql_connection()
    con.execute(sql_create_db)
    con.dispose()
    
def pytest_sessionstart(session):

    delete_database()
    create_database()
    create_table()

def pytest_sessionfinish(session, exitstatus):
    delete_database()