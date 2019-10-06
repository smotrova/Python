import sqlite3

con = sqlite3.connect("first.db")

# create cursor object
c = con.cursor()

# v1
# create table if it doesen't exist
try:
    c.execute("""CREATE TABLE person(name TEXT, telefon TEXT)""")
except:
    pass
#=========================================================================
# v2
#
# create table if it doesen't exist
# c.execute("""CREATE TABLE IF NOT EXISTS person(name TEXT, telefon TEXT)""")
# c.execute("""INSERT INTO person (name, telefon) VALUES ('Janie', 2154635414143);""")
# con.commit()
# c.close()
# con.close()
#=============================================================================
name_in_python = "Claudia"
tel_i_python = "215465365464"

names = ["Kat", "Peter", "Hans"]
tels = ["46346161", "189813693", "34111184368"]

c = sqlite3.connect("first.db")
c = con.cursor()

c.execute(""" INSERT INTO person(name, telefon) VALUES (?, ?); """, (name_in_python, tel_i_python))
con.commit()

for i in range(3):
    c.execute(""" INSERT INTO person(name, telefon) VALUES (?, ?); """, (names[i], tels[i]))
    con.commit()

c.close()
con.close()
