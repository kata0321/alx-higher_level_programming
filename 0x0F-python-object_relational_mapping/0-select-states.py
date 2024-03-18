#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """
import MysQLdb
import sys
db=_mysql.connect(host="localhost",user="sys.agrv[1]",
                  password="sys.agrv[2]",database="sys.agrv.[3]",port="3306")
c = db.cursor()
c.execute("SELECT * FROM states")
c.close()
db.close()
