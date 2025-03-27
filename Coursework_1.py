import tkinter as tk
import sqlite3
from tkinter import messagebox
from PIL import Image, ImageTk

All_Data = sqlite3.connect('all_data.db')
c = All_Data.cursor()



c.execute("""
    CREATE TABLE IF NOT EXISTS All_Data (
        SERIAL_NUMBER INTEGER PRIMARY KEY AUTOINCREMENT,
        DATE_OF_CASE TEXT,
        STUDENT_NAME TEXT,
        MODULE_CODE TEXT,
        MODULE_LEADER TEXT,
        ALLEGATION TEXT,
        OUTCOME_OF_CASE TEXT
    )
""")



#Deffining function to Take the data from the user
def insert_data():
    date = input('Enter the date of the case: ')
    student = input('Enter the name of the student: ')
    code = input('Enter the module code: ')
    leader = input('Enter the module leader: ')
    allegation = input('Enter the allegation: ')
    outcome = input('Enter the outcome of the case: ')
    c.execute("""
        INSERT INTO All_Data (DATE_OF_CASE, STUDENT_NAME, MODULE_CODE, MODULE_LEADER, ALLEGATION, OUTCOME_OF_CASE)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (date, student, code, leader, allegation, outcome))

#save button function for Tkinter GUI
def Save_button_function():
    #to take input from the entry fields.
    date_value = date.get()
    student_value = student.get()
    code_value = code.get()
    leader_value = leader.get()
    allegation_value = allegation.get()
    outcome_value = outcome.get()
#to insert the data into the database
    c.execute("""
    INSERT INTO All_Data (DATE_OF_CASE, STUDENT_NAME, MODULE_CODE, MODULE_LEADER, ALLEGATION, OUTCOME_OF_CASE)
    VALUES (?, ?, ?, ?, ?, ?) """,
              (date_value, student_value, code_value, leader_value, allegation_value, outcome_value))

    All_Data.commit()
    message = messagebox.showinfo('Data Entry', 'Data has been saved!')
    #to clear the entry fields after saving the data
    date.delete(0, tk.END)
    student.delete(0, tk.END)
    code.delete(0, tk.END)
    leader.delete(0, tk.END)
    allegation.delete(0, tk.END)
    outcome.delete(0, tk.END)


#Data taking function ends here


way = input('Which way are you going to run the function: TUI or GUI? ')
        #Asking the user to choose the way to function: TUI or GUI

#If the user choose TUI then the following code will run
if way == 'TUI':
    What_to_do = input('What do you want to do?'
                    ' display/insert/change/delete: ')
    if What_to_do == 'display':#Displaying the data
        c.execute("SELECT * FROM All_Data")
        items = c.fetchall()
        for item in items:
            print(item)
    elif What_to_do == 'insert':#Inserting the data
        while True:  # Infinite loop for taking input
            insert_data()
            All_Data.commit()
            add_more_data = input('Do you want to add more data? (yes/no): ').lower()  # Normalize input
            if add_more_data != 'yes':  # Break the loop unless the user explicitly says 'yes'
                break

    elif What_to_do == 'change':#Changing the data
        c.execute("SELECT * FROM All_Data")
        items = c.fetchall()
        for item in items:
            print(item)
        #inputing the data to change
        serial_number = input('Enter the serial number of the case you want to change: ')
        date = input('Enter the new date of the case: ')
        student = input('Enter the new name of the student: ')
        code = input('Enter the new module code: ')
        leader = input('Enter the new module leader: ')
        allegation = input('Enter the new allegation: ')
        outcome = input('Enter the new outcome of the case: ')
        c.execute("""
            UPDATE All_Data
            SET DATE_OF_CASE = ?, STUDENT_NAME = ?, MODULE_CODE = ?, MODULE_LEADER = ?, ALLEGATION = ?, OUTCOME_OF_CASE = ?
            WHERE SERIAL_NUMBER = ?
        """, (date, student, code, leader, allegation, outcome, serial_number))
        All_Data.commit()
    elif What_to_do == 'delete':
        c.execute("SELECT * FROM All_Data")
        items = c.fetchall() #Dispalay the data to delete by number of case
        for item in items:
            print(item)
        serial_number = input('Enter the serial number of the case you want to delete: ')
        c.execute("DELETE FROM All_Data WHERE SERIAL_NUMBER = ?", (serial_number,))
        All_Data.commit()
elif way == 'GUI':
    root = tk.Tk()
    root.title('Data Entry GUI')
    root.geometry('820x700')

    image_path = ImageTk.PhotoImage(
        Image.open("images/blue_abstract_background.png")
    )
    background_image = tk.Label(root, image=image_path)
    background_image.place(x=0, y=0, relwidth=1, relheight=1)
    root.image_path = image_path




    label = tk.Label(root, text='Enter the date of the case:', font=('Arial', 10))
    label.place(x=20, y=10)
    date = tk.Entry(root, width=50)
    date.place(x=20, y=40)

    label = tk.Label(root, text='Enter the name of the student:', font=('Arial', 10))
    label.place(x=20, y=70)
    student = tk.Entry(root, width=50)
    student.place(x=20, y=100)

    label = tk.Label(root, text='Enter the module code:', font=('Arial', 10))
    label.place(x=20, y=130)
    code = tk.Entry(root, width=50)
    code.place(x=20, y=160)

    label = tk.Label(root, text='Enter the module leader:', font=('Arial', 10))
    label.place(x=20, y=190)
    leader = tk.Entry(root, width=50)
    leader.place(x=20, y=220)

    label = tk.Label(root, text='Enter the allegation:', font=('Arial', 10))
    label.place(x=20, y=250)
    allegation = tk.Entry(root, width=50)
    allegation.place(x=20, y=280)

    label = tk.Label(root, text='Enter the outcome of the case:', font=('Arial', 10))
    label.place(x=20, y=310)
    outcome = tk.Entry(root, width=50)
    outcome.place(x=20, y=340)

    label = tk.Label(root, text='Enter the date of the case:', font=('Arial', 10))
    label.place(x=20, y=10)
    date = tk.Entry(root, width=50)
    date.place(x=20, y=40)

    label = tk.Label(root, text='Enter the name of the student:', font=('Arial', 10))
    label.place(x=20, y=70)
    student = tk.Entry(root, width=50)
    student.place(x=20, y=100)

    label = tk.Label(root, text='Enter the module code:', font=('Arial', 10))
    label.place(x=20, y=130)
    code = tk.Entry(root, width=50)
    code.place(x=20, y=160)

    label = tk.Label(root, text='Enter the module leader:', font=('Arial', 10))
    label.place(x=20, y=190)
    leader = tk.Entry(root, width=50)
    leader.place(x=20, y=220)

    label = tk.Label(root, text='Enter the allegation:', font=('Arial', 10))
    label.place(x=20, y=250)
    allegation = tk.Entry(root, width=50)
    allegation.place(x=20, y=280)

    label = tk.Label(root, text='Enter the outcome of the case:', font=('Arial', 10))
    label.place(x=20, y=310)
    outcome = tk.Entry(root, width=50)
    outcome.place(x=20, y=340)

    button = tk.Button(root, text='Save', command=Save_button_function, bg='green', font=('Arial', 20))
    button.place(x=20, y=365)

    # Delete function
    label=tk.Label(root, text='Enter the serial number of case you want to delete:', font=('Arial', 10))
    label.place(x=500, y=130)
    serial_number=tk.Entry(root, width=40)
    serial_number.place(x=500, y=160)
    # Delete function setup
    label_delete = tk.Label(root, text='Enter the serial number of case you want to delete:', font=('Arial', 10))
    label_delete.place(x=500, y=130)

    serial_number_delete = tk.Entry(root, width=40)  # Separate entry field for delete functionality
    serial_number_delete.place(x=500, y=160)


    def delete_data():
        serial_number_value = serial_number_delete.get()  # Use the specific entry field
        if serial_number_value.strip():  # Check if input is not empty
            c.execute("DELETE FROM All_Data WHERE SERIAL_NUMBER = ?", (serial_number_value,))
            All_Data.commit()


    # Delete button
    button_delete = tk.Button(root, text='Delete', command=delete_data, bg='Red', font=('Arial', 20))
    button_delete.place(x=500, y=200)

    label=tk.Label(root, text='Enter the serial number of case you want to change:', font=('Arial', 10))
    label.place(x=500, y=290)
    serial_number=tk.Entry(root, width=40)
    serial_number.place(x=500, y=320)
    def change_data():
        serial_number_value=serial_number.get()
        date_value = date.get()
        student_value = student.get()
        code_value = code.get()
        leader_value = leader.get()
        allegation_value = allegation.get()
        outcome_value = outcome.get()
        c.execute("""
            UPDATE All_Data
            SET DATE_OF_CASE = ?, STUDENT_NAME = ?, MODULE_CODE = ?, MODULE_LEADER = ?, ALLEGATION = ?, OUTCOME_OF_CASE = ?
            WHERE SERIAL_NUMBER = ?
        """, (date_value, student_value, code_value, leader_value, allegation_value, outcome_value, serial_number_value))
        All_Data.commit()
        message=messagebox.showinfo('Data Entry', 'Data has been changed!')
        date.delete(0, tk.END)
        student.delete(0, tk.END)
        code.delete(0, tk.END)
        leader.delete(0, tk.END)
        allegation.delete(0, tk.END)
        outcome.delete(0, tk.END)
        serial_number_delete.delete(0, tk.END)
    button = tk.Button(root, text='Update', command=change_data, bg='lightgreen', font=('Arial', 20))
    button.place(x=500, y=350)
    frame=tk.Frame(root, bg='lightblue')
    frame.place(x=20, y=450, width=780, height=230)


    def display():
        # Clear existing items from the canvas
        canvas.delete("all")

        # Fetch all items from the database
        c.execute("SELECT * FROM All_Data")
        items = c.fetchall()

        # Create a new frame inside the canvas for displaying items
        inner_frame = tk.Frame(canvas, bg='white')
        inner_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Use the window function of Canvas to embed the inner frame
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")

        # Display data as Labels inside the inner_frame
        for item in items:
            display_text = f"Serial: {item[0]} | Date: {item[1]} | Student: {item[2]} | Module: {item[3]} | " \
                           f"Leader: {item[4]} | Allegation: {item[5]} | Outcome: {item[6]}"
            tk.Label(inner_frame, text=display_text, font=('Arial', 10), anchor='w').pack(pady=5)


    # Create a canvas for scrollable content
    canvas = tk.Canvas(root, bg='white', width=780, height=230)
    canvas.place(x=20, y=450)

    # Add vertical scrollbar
    scrollbar_y = tk.Scrollbar(root, command=canvas.yview)
    scrollbar_y.place(x=800, y=450, height=230)
    canvas.configure(yscrollcommand=scrollbar_y.set)

    # Add horizontal scrollbar
    scrollbar_x = tk.Scrollbar(root, command=canvas.xview, orient="horizontal")
    scrollbar_x.place(x=20, y=680, width=780)
    canvas.configure(xscrollcommand=scrollbar_x.set)


    # Button to trigger the display function
    button = tk.Button(root, text='Display', command=display, bg='Yellow', font=('Arial', 20))
    button.place(x=200, y=365)
    #display by case
    label=tk.Label(root, text='Enter the serial number of case you want to display:', font=('Arial', 10))
    label.place(x=500, y=10)
    serial_number=tk.Entry(root, width=40)
    serial_number.place(x=500, y=40)
    def display_by_case():
        canvas.delete("all")


        # Create a new frame inside the canvas for displaying items
        inner_frame = tk.Frame(canvas, bg='white')
        inner_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Use the window function of Canvas to embed the inner frame
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")


        # Fetch all items from the database
        serial_number_value = serial_number.get()
        c.execute("SELECT * FROM All_Data WHERE SERIAL_NUMBER = ?", (serial_number_value,))
        items = c.fetchall()

        # Display data as Labels inside the inner_frame
        for item in items:
            display_text = f"Serial: {item[0]} | Date: {item[1]} | Student: {item[2]} | Module: {item[3]} | " \
                           f"Leader: {item[4]} | Allegation: {item[5]} | Outcome: {item[6]}"
            tk.Label(inner_frame, text=display_text, font=('Arial', 10), anchor='w').pack(pady=5)
        serial_number_value=serial_number.get()

    button = tk.Button(root, text='Display by case', command=display_by_case, bg='lightyellow', font=('Arial', 20))
    button.place(x=500, y=70)



    root.mainloop()
else:
    print("Invalid input. Please choose 'TUI' or 'GUI'.")
All_Data.commit()
All_Data.close()