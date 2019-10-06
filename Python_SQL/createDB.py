import sqlite3
con = sqlite3.connect("countries.db")

# create cursor object
c = con.cursor()

# create table if it doesen't exist
try:
    c.execute("""CREATE TABLE location(city TEXT, country TEXT)""")
except:
    pass

countries = dict({"Berlin":"Germany", "Bern":"Swiss", "Hamburg":"Germany", "Paris":"France",
"Kyiv":"Ukraine", "Lemberg":"Ukraine", "Munich":"Germany"})

for i in countries.keys():
    c.execute("""INSERT INTO location(city, country) VALUES (?, ?);""", (i, countries[i]))

con.commit()

c.close()
con.close()
