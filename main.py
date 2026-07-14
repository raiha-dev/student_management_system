import mysql.connector

# Database connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",  # IMPORTANT: yahan apna MySQL password likhna
        database="student_db"
    )

# 1. Add Student
def add_student():
    conn = connect_db()
    cursor = conn.cursor()
    name = input("Enter Name: ")
    roll_no = input("Enter Roll No: ")
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))
    
    sql = "INSERT INTO students (name, roll_no, course, marks) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (name, roll_no, course, marks))
    conn.commit()
    print("Student Added Successfully!")
    conn.close()

# 2. View All Students
def view_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    for row in results:
        print(row)
    conn.close()

# 3. Update Student
def update_student():
    conn = connect_db()
    cursor = conn.cursor()
    roll_no = input("Enter Roll No to update: ")
    new_marks = float(input("Enter New Marks: "))
    sql = "UPDATE students SET marks=%s WHERE roll_no=%s"
    cursor.execute(sql, (new_marks, roll_no))
    conn.commit()
    print("Student Updated!")
    conn.close()

# 4. Delete Student
def delete_student():
    conn = connect_db()
    cursor = conn.cursor()
    roll_no = input("Enter Roll No to delete: ")
    sql = "DELETE FROM students WHERE roll_no=%s"
    cursor.execute(sql, (roll_no,))
    conn.commit()
    print("Student Deleted!")
    conn.close()

# Main Menu
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == '1': add_student()
    elif choice == '2': view_students()
    elif choice == '3': update_student()
    elif choice == '4': delete_student()
    elif choice == '5': break
    else: print("Invalid Choice!")
