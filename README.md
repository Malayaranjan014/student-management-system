Student Management System

A simple Python Tkinter + PostgreSQL desktop application that allows users to:

Add Student

View All Students

Update Student

Delete Student

Manage data using a PostgreSQL database

Project Overview

This project uses:

Tkinter – for creating the GUI

ttk.Treeview – for displaying student data in a table

PostgreSQL – backend database

psycopg2 – Python connector for PostgreSQL

Features

Insert Student Data

View All Students

Update Selected Student

Delete Selected Student

Create Table (if it does not already exist)

Database Schema
students (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    address VARCHAR(255),
    age INT,
    number VARCHAR(15)
)








✔ Create Table

Automatically creates the database table if it doesn't exist.
