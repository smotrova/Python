import sqlite3
con = sqlite3.connect("countries.db")
c = con.cursor()

selected_country = "Ukraine"
new_city = "Charkiw"

c.execute("""UPDATE location SET city = ? WHERE country = ?;""", (new_city, selected_country))

c.execute("""SELECT * FROM location;""")
for line in c:
    print(line)

# update DB after look at a table
# con.commit()

c.close()
con.close()
