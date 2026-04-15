import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    marks INTEGER
)
''')

conn.commit()

def add_student():
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    
    cursor.execute("INSERT INTO students (name, marks) VALUES (?, ?)", (name, marks))
    conn.commit()
    print("Student added!")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)

def update_student():
    id = int(input("Enter student ID: "))
    marks = int(input("Enter new marks: "))
    
    cursor.execute("UPDATE students SET marks = ? WHERE id = ?", (marks, id))
    conn.commit()
    print("Updated successfully!")

def delete_student():
    id = int(input("Enter student ID: "))
    
    cursor.execute("DELETE FROM students WHERE id = ?", (id,))
    conn.commit()
    print("Deleted successfully!")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        break
    else:
        print("Invalid choice!")

conn.close()
