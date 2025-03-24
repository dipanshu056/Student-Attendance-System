import sqlite3

conn = sqlite3.connect('attendance.db')
cursor = conn.execute("SELECT * FROM attendance")
print("Attendance Records:")
for row in cursor:
    print(f"Name: {row[0]}, Date: {row[1]}")
conn.close()