from tkinter import * 
import tkinter as tk
from tkinter import ttk    #provides access to the Tk themed widget set
import psycopg2
from tkinter import messagebox



def run_query(query,parameters=()):
    #create a connection to the database
    conn = psycopg2.connect(
        dbname="studentdb",
        user="postgres",
        password="0330",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()
    query_result=None 

    try:
        cur.execute(query,parameters)
        if query.lower().startswith("select"):
            query_result = cur.fetchall()           #fetch all results for select query
        conn.commit()
    except psycopg2.Error as e:
        messagebox.showerror("Database Error",str(e))
    finally:
        cur.close()
        conn.close()
        return query_result


#define function to refresh treeview
def refresh_treeview():
    #clear the current data in the treeview
    for item in tree.get_children():
        tree.delete(item)
    records=run_query("SELECT * FROM students")
    for record in records:
        tree.insert("",END,values=record)


def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS students (
        student_id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        address VARCHAR(255) NOT NULL,
        age INT NOT NULL,
        number VARCHAR(15) NOT NULL
    );
    """
    run_query(query)
    messagebox.showinfo("Success","Table created successfully")


def insert_data():
    name = name_entry.get()
    address = address_entry.get()
    age = Age_entry.get()
    number = number_entry.get()

    if not name or not address or not age or not number:
        messagebox.showwarning("Input Error","All fields are required")
        return

    query = """
    INSERT INTO students (name,address,age,number)
    VALUES (%s,%s,%s,%s)
    """
    parameters=(name,address,age,number)
    run_query(query,parameters)
    messagebox.showinfo("Success","Data inserted successfully")
    refresh_treeview()


def delete_data():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showwarning("Selection Error","No item selected")
        return

    values = tree.item(selected_item,"values")
    student_id = values[0]

    query = "DELETE FROM students WHERE student_id=%s"
    parameters=(student_id,)
    run_query(query,parameters)
    messagebox.showinfo("Success","Data deleted successfully")
    refresh_treeview()


def update_data():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showwarning("Selection Error","No item selected")
        return

    values = tree.item(selected_item,"values")
    student_id = values[0]

    name = name_entry.get()
    address = address_entry.get()
    age = Age_entry.get()
    number = number_entry.get()

    if not name or not address or not age or not number:
        messagebox.showwarning("Input Error","All fields are required")
        return

    query = """
    UPDATE students
    SET name=%s, address=%s, age=%s, number=%s
    WHERE student_id=%s
    """
    parameters = (name,address,age,number,student_id)
    run_query(query,parameters)
    messagebox.showinfo("Success","Data updated successfully")
    refresh_treeview()



root = Tk()
root.title("Student Management System")
root.configure(bg="#f2f2f2")   # light grey background

label_font = ("Arial", 11)    # simple font
button_font = ("Arial", 10, "bold")

#input sections 

frame = LabelFrame(root, text="Student Details", font=("Arial", 12, "bold"),
bg="#f2f2f2", padx=10, pady=10)
frame.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

Label(frame, text="Name:", bg="#f2f2f2", font=label_font).grid(row=0, column=0, pady=5, sticky="w")
name_entry = Entry(frame, font=label_font)
name_entry.grid(row=0, column=1, pady=5)

Label(frame, text="Address:", bg="#f2f2f2", font=label_font).grid(row=1, column=0, pady=5, sticky="w")
address_entry = Entry(frame, font=label_font)
address_entry.grid(row=1, column=1, pady=5)

Label(frame, text="Age:", bg="#f2f2f2", font=label_font).grid(row=2, column=0, pady=5, sticky="w")
Age_entry = Entry(frame, font=label_font)
Age_entry.grid(row=2, column=1, pady=5)

Label(frame, text="Number:", bg="#f2f2f2", font=label_font).grid(row=3, column=0, pady=5, sticky="w")
number_entry = Entry(frame, font=label_font)
number_entry.grid(row=3, column=1, pady=5)

#button section

button_frame = Frame(root, bg="#f2f2f2")
button_frame.grid(row=1, column=0, padx=20, pady=10)

Button(button_frame, text="Create Table", width=15, font=button_font,bg="#4CAF50", fg="white", command=create_table).grid(row=0, column=0, padx=5)

Button(button_frame, text="Insert Data", width=15, font=button_font,bg="#2196F3", fg="white", command=insert_data).grid(row=0, column=1, padx=5)

Button(button_frame, text="Update Data", width=15, font=button_font,bg="#FFC107", command=update_data).grid(row=0, column=2, padx=5)

Button(button_frame, text="Delete Data", width=15, font=button_font,bg="#F44336", fg="white", command=delete_data).grid(row=0, column=3, padx=5)

Button(button_frame, text="Exit", width=15, font=button_font,bg="#9E9E9E", fg="white", command=root.quit).grid(row=0, column=4, padx=5)



#table frame

tree_frame = Frame(root)
tree_frame.grid(row=2, column=0, padx=20, pady=20)

# Simple Treeview styles
style = ttk.Style()
style.configure("Treeview.Heading", font=("Arial", 11, "bold"), foreground="black")
style.configure("Treeview", font=("Arial", 10), rowheight=25)

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="browse")
tree.pack()

tree_scroll.config(command=tree.yview)


#define columns in tables 

tree["columns"] = ("ID", "Name", "Address", "Age", "Number")

tree.column("#0", width=0, stretch=NO)
tree.column("ID", anchor=CENTER, width=80)
tree.column("Name", anchor=W, width=120)
tree.column("Address", anchor=W, width=200)
tree.column("Age", anchor=CENTER, width=80)
tree.column("Number", anchor=W, width=120)

tree.heading("ID", text="ID", anchor=CENTER)
tree.heading("Name", text="Name", anchor=W)
tree.heading("Address", text="Address", anchor=W)
tree.heading("Age", text="Age", anchor=CENTER)
tree.heading("Number", text="Number", anchor=W)

refresh_treeview()
root.mainloop()
