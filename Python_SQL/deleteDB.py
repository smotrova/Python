import sqlite3
con = sqlite3.connect("countries.db")
c = con.cursor()

del_country = "Ukraine"

c.execute("""DELETE FROM location WHERE country = ?;""", (del_country, ))

c.execute("""SELECT * FROM location;""")
for line in c:
    print(line)

# update DB after you have a look at a table
# con.commit()

c.close()
con.close()
