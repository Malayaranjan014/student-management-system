# student-management-system
A Python Tkinter + PostgreSQL CRUD project


📘 Student Management System
1-A simple Python Tkinter + PostgreSQL desktop application that allows users to:
2-Add Student
3-View All Students
4-Update Student
5-Delete Student
6-Manage data using a PostgreSQL database
------------------------------------------------------------------------------------
Project Overview
1-Tkinter → For creating the GUI
2-ttk.Treeview → For displaying student data in table format
3-PostgreSQL → Backend database
4-psycopg2 → Python connector for PostgreSQL
-----------------------------------------------------------------------------------
🛠️ Features
✔ Insert Student Data
Add name, address, age, and number to the database.
✔ Read (View All Students)
Displays all data in a table using Treeview.
✔ Update Selected Student
Select any row from the table → Edit fields → Update.
✔ Delete Selected Student
Deletes a student record after selecting from table.
-----------------------------------------------------------------------------------
💾 Database Schema
students (
    student_id SERIAL PRIMARY KEY,
    name       VARCHAR(100),
    address    VARCHAR(255),
    age        INT,
    number     VARCHAR(15)
)
----------------------------------------------------------------------------------












✔ Create Table

Automatically creates the database table if it doesn't exist.
