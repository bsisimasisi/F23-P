import sqlite3

conn = sqlite3.connect("crew.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

cursor.execute("DELETE FROM Roster")

data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]
cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", data)

cursor.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")

cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
bajoran_crew = cursor.fetchall()

print("Bajoran Crew:")
for name, age in bajoran_crew:
    print(f"{name} - {age} years old")

conn.commit()
conn.close()
