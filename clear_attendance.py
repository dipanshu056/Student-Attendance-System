import sqlite3

# Connect to database
conn = sqlite3.connect('attendance.db')
cursor = conn.cursor()

# Delete all records of attendance
cursor.execute("DELETE FROM attendance")
conn.commit()

print("All attendance records deleted successfully!")

conn.close()