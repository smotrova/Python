import sqlite3
con = sqlite3.connect("countries.db")
c = con.cursor()

# create table if it doesen't exist
try:
    c.execute("""CREATE TABLE location_with_key(ID INTEGER PRIMARY KEY, city TEXT, country TEXT)""")
except:
    pass

countries = dict({"Berlin":"Germany", "Bern":"Swiss", "Hamburg":"Germany", "Paris":"France",
"Kyiv":"Ukraine", "Lemberg":"Ukraine", "Munich":"Germany"})

i = 100
for k in countries.keys():
    c.execute("""INSERT INTO location_with_key(ID, city, country) VALUES (?, ?, ?);""", (i, k, countries[k]))
    i += 1

con.commit()

c.execute("""SELECT * FROM location_with_key;""")
for line in c:
    print(line)

c.close()
con.close()
