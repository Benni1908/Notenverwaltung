import sqlite3
from student import Student

conn = sqlite3.connect('notenliste.db')

c = conn.cursor()

# c.execute("""CREATE TABLE notenliste (
#             vorname text,
#             nachname text,
#             matrnr text
#             )""")


def insert_stud(stud):
    with conn:
        c.execute("INSERT INTO notenliste VALUES (:vorname,:nachname,:matrnr)",
                  {'vorname': stud.vorname, 'nachname': stud.nachname, 'matrnr': stud.matrnr})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM notenliste WHERE nachname=:nachname", {'nachname': lastname})
    return c.fetchall()



def remove_stud(stud):
    with conn:
        c.execute("DELETE from notenliste WHERE vorname = :vorname AND nachname = :nachname",
                  {'vorname': stud.vorname, 'nachname': stud.nachname})


# stud = Student('Benni', 'Eli', '396904')
feld1 = 'Marco'
feld2 = 'Simon'
feld3 = '397377'
stud = Student(feld1, feld2, feld3)


insert_stud(stud)

print(stud)

studs = get_emps_by_name('Simon')
print(studs)

conn.close()
