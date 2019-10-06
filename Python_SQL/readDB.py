import sqlite3
con = sqlite3.connect("countries.db")
c = con.cursor()

# select all data drom table
# c.execute("""SELECT * FROM location;""")
#
# for line in c:
#     print(line)
#
# print("\n")

selected_country = "Ukraine"
c.execute("""SELECT * FROM location WHERE country = ?;""", (selected_country,))
for line in c:
    print(line)

c.close()
con.close()
