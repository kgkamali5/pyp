from tkinter import *
import sqlite3


from tkinter import ttk
from tkinter import messagebox
from db import Database

root = Tk()
root.title("STUDENTS INFORMATION RECORD")

width = 1000
height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)


def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
    cursor.execute("SELECT * FROM `member` WHERE `username` = 'giritharan' AND `password` = 'giri@123'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `member` (username, password) VALUES('giritharan', 'giri@123')")
        conn.commit()


def Login(event=None):
    Database()

    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="blue")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?",
                       (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            HomeWindow()
            USERNAME.set("")
            PASSWORD.set("")
            lbl_text.config(text="")
        else:
            lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close()


def HomeWindow():
    global Home
    root.withdraw()
    Home = Toplevel()
    Home.title("STUDENTS INFORMATION RECORD")
    width = 800
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    lbl_home = Label(Home, text="Successfully Logined!", font=("Calibri", 16, "bold"),
                       fg="white", bg="#c0392b").pack()
    btn_back = Button(Home, text='Continue', command=Continue, font=("Calibri", 16, "bold"),
                     fg="white", bg="#2980b9").pack(pady=40, fill=X)

def Continue():

    from tkinter import ttk
    from tkinter import messagebox
    from db import Database

    db = Database("Employee.db")
    root = Tk()
    root.title("STUDENTS INFORMATION RECORD")
    root.geometry("1920x1080+0+0")
    root.config(bg="#2c3e50")
    root.state("zoomed")

    name = StringVar()
    age = StringVar()
    doj = StringVar()
    gender = StringVar()
    email = StringVar()
    contact = StringVar()
    collegename = StringVar()
    certificate = StringVar()
    resumelink = StringVar()
    collegenumber = StringVar()
    # Entries Frame
    entries_frame = Frame(root, bg="#16a085")
    entries_frame.pack(side=TOP, fill=X)
    title = Label(entries_frame, text="STUDENTS INFORMATION RECORD", font=("Calibri", 18, "bold"), bg="#535c68",
                  fg="white")
    title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

    lblName = Label(entries_frame, text="Name", font=("Calibri", 10), bg="#535c68", fg="white")
    lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    txtName = Entry(entries_frame, textvariable=name, font=("Calibri", 10), width=30)
    txtName.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    lblAge = Label(entries_frame, text="Age", font=("Calibri", 10), bg="#535c68", fg="white")
    lblAge.grid(row=1, column=2, padx=10, pady=10, sticky="w")
    txtAge = Entry(entries_frame, textvariable=age, font=("Calibri", 10), width=30)
    txtAge.grid(row=1, column=3, padx=10, pady=10, sticky="w")

    lbldoj = Label(entries_frame, text="D.O.J", font=("Calibri", 10), bg="#535c68", fg="white")
    lbldoj.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    txtDoj = Entry(entries_frame, textvariable=doj, font=("Calibri", 10), width=30)
    txtDoj.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    lblEmail = Label(entries_frame, text="Email", font=("Calibri", 10), bg="#535c68", fg="white")
    lblEmail.grid(row=2, column=2, padx=10, pady=10, sticky="w")
    txtEmail = Entry(entries_frame, textvariable=email, font=("Calibri", 10), width=30)
    txtEmail.grid(row=2, column=3, padx=10, pady=10, sticky="w")

    lblGender = Label(entries_frame, text="Gender", font=("Calibri", 10), bg="#535c68", fg="white")
    lblGender.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    comboGender = ttk.Combobox(entries_frame, font=("Calibri", 10), width=30, textvariable=gender, state="readonly")
    comboGender['values'] = ("Male", "Female")
    comboGender.grid(row=3, column=1, padx=10, sticky="w")

    lblContact = Label(entries_frame, text="Contact No", font=("Calibri", 10), bg="#535c68", fg="white")
    lblContact.grid(row=3, column=2, padx=10, pady=10, sticky="w")
    txtContact = Entry(entries_frame, textvariable=contact, font=("Calibri", 10), width=30)
    txtContact.grid(row=3, column=3, padx=10, sticky="w")

    lblAddress = Label(entries_frame, text="Address", font=("Calibri", 10), bg="#535c68", fg="white")
    lblAddress.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    txtAddress = Text(entries_frame, width=50, height=5, font=("Calibri", 10))
    txtAddress.grid(row=5, column=0, columnspan=4, padx=10, sticky="w")

    lblcollegename = Label(entries_frame, text="College Name", font=("Calibri", 10), bg="#535c68", fg="white")
    lblcollegename.grid(row=1, column=4, padx=10, pady=10, sticky="w")
    txtcollegename = Entry(entries_frame, textvariable=contact, font=("Calibri", 10), width=30)
    txtcollegename.grid(row=1, column=5, padx=10, sticky="w")

    lblcertificate = Label(entries_frame, text="Certificate no", font=("Calibri", 10), bg="#535c68", fg="white")
    lblcertificate.grid(row=2, column=4, padx=10, pady=10, sticky="w")
    txtcertificate = Entry(entries_frame, textvariable=contact, font=("Calibri", 10), width=30)
    txtcertificate.grid(row=2, column=5, padx=10, sticky="w")

    lblcertificatelink = Label(entries_frame, text="Certificate Link", font=("Calibri", 10), bg="#535c68", fg="white")
    lblcertificatelink.grid(row=3, column=4, padx=10, pady=10, sticky="w")
    txtcertificatelink = Entry(entries_frame, textvariable=contact, font=("Calibri", 10), width=30)
    txtcertificatelink.grid(row=3, column=5, padx=10, sticky="w")

    lblresumelink = Label(entries_frame, text="Resume link", font=("Calibri", 10), bg="#535c68", fg="white")
    lblresumelink.grid(row=3, column=4, padx=10, pady=10, sticky="w")
    txtresumelink = Entry(entries_frame, textvariable=contact, font=("Calibri", 10), width=30)
    txtresumelink.grid(row=3, column=5, padx=10, sticky="w")

    lblcollegenumber = Label(entries_frame, text="College Number", font=("Calibri", 10), bg="#535c68", fg="white")
    lblcollegenumber.grid(row=4, column=4, padx=10, pady=10, sticky="w")
    txtcollegenumber = Entry(entries_frame, textvariable=contact, font=("Calibri", 10), width=30)
    txtcollegenumber.grid(row=4, column=5, padx=10, sticky="w")

    def getData(event):
        selected_row = tv.focus()
        data = tv.item(selected_row)
        global row
        row = data["values"]
        # print(row)
        name.set(row[1])
        age.set(row[2])
        doj.set(row[3])
        email.set(row[4])
        gender.set(row[5])
        contact.set(row[6])

        txtAddress.delete(1.0, END)
        txtAddress.insert(END, row[7])

    def dispalyAll():
        tv.delete(*tv.get_children())
        for row in db.fetch():
            tv.insert("", END, values=row)

    def add_employee():
        if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(
                1.0, END) == "":
            messagebox.showerror("Erorr in Input", "Please Fill All the Details")
            return
        db.insert(txtName.get(), txtAge.get(), txtDoj.get(), txtEmail.get(), comboGender.get(), txtContact.get(),
                  txtAddress.get(
                      1.0, END))
        messagebox.showinfo("Success", "Record Inserted")
        clearAll()
        dispalyAll()

    def update_employee():
        if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(
                1.0, END) == "":
            messagebox.showerror("Erorr in Input", "Please Fill All the Details")
            return
        db.update(row[0], txtName.get(), txtAge.get(), txtDoj.get(), txtEmail.get(), comboGender.get(),
                  txtContact.get(),
                  txtAddress.get(
                      1.0, END))
        messagebox.showinfo("Success", "Record Update")
        clearAll()
        dispalyAll()

    def delete_employee():
        db.remove(row[0])
        clearAll()
        dispalyAll()

    def clearAll():
        name.set("")
        age.set("")
        doj.set("")
        gender.set("")
        email.set("")
        contact.set("")
        txtAddress.delete(1.0, END)

    btn_frame = Frame(entries_frame, bg="#535c68")
    btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
    btnAdd = Button(btn_frame, command=add_employee, text="Add Details", width=15, font=("Calibri", 16, "bold"),
                    fg="white",
                    bg="#16a085", bd=0).grid(row=0, column=0)
    btnEdit = Button(btn_frame, command=update_employee, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                     fg="white", bg="#2980b9",
                     bd=0).grid(row=0, column=1, padx=10)
    btnDelete = Button(btn_frame, command=delete_employee, text="Delete Details", width=15,
                       font=("Calibri", 16, "bold"),
                       fg="white", bg="#c0392b",
                       bd=0).grid(row=0, column=2, padx=10)
    btnClear = Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"),
                      fg="white",
                      bg="#f39c12",
                      bd=0).grid(row=0, column=3, padx=10)

    # Table Frame
    tree_frame = Frame(root, bg="#ecf0f1")
    tree_frame.place(x=0, y=480, width=1980, height=720)
    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('Calibri', 18),
                    rowheight=50)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
    tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
    tv.heading("1", text="ID")
    tv.column("1", width=5)
    tv.heading("2", text="Name")
    tv.heading("3", text="Age")
    tv.column("3", width=5)
    tv.heading("4", text="D.O.B")
    tv.column("4", width=5)
    tv.heading("5", text="Email")
    tv.heading("6", text="Gender")
    tv.column("6", width=5)
    tv.heading("7", text="Contact")
    tv.heading("8", text="Address")
    tv['show'] = 'headings'
    tv.bind("<ButtonRelease-1>", getData)
    tv.pack(fill=X)

    dispalyAll()
    root.mainloop()



USERNAME = StringVar()
PASSWORD = StringVar()


Top = Frame(root, bd=2, relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=500)
Form.pack(side=TOP, pady=50)


lbl_title = Label(Top, text="STUDENTS INFORMATION RECORDS", font=('arial', 15))
lbl_title.pack(fill=X)
lbl_username = Label(Form, text="Username:", font=('arial', 14),bd=15)
lbl_username.grid(row=0, sticky="e")
lbl_password = Label(Form, text="Password:", font=('arial', 14), bd=15)
lbl_password.grid(row=1, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)


username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)

btn_login = Button(Form, text="Login", width=40, command=Login, font=("Calibri", 16, "bold"),
                fg="white",
                bg="#16a085")
btn_login.grid(pady=25, row=3, columnspan=2)
btn_login.bind('<Return>', Login)

if __name__ == '__main__':
        root.mainloop()





