from tkinter import *
from tkinter import messagebox
import mysql.connector as ms

mycon = ms.connect(host='localhost', user='root', passwd='1024', database='mydb')
cur = mycon.cursor()


def verifier():
    a = b = c = d = e = f = 0
    if not student_name.get():
        t1.insert(END, "<>Student name is required<>\n")
        a = 1
    if not roll_no.get():
        t1.insert(END, "<>Roll no is required<>\n")
        b = 1
    if not stream.get():
        t1.insert(END, "<>Stream is required<>\n")
        c = 1
    if not phone.get():
        t1.insert(END, "<>Phone number is requrired<>\n")
        d = 1
    if not father.get():
        t1.insert(END, "<>Father name is required<>\n")
        e = 1
    if not admission_num.get():
        t1.insert(END, "<>admission_num is Required<>\n")
        f = 1
    if a == 1 or b == 1 or c == 1 or d == 1 or e == 1 or f == 1:
        return 1
    else:
        return 0


def add_student():
    t1.config(state=NORMAL)
    ret = verifier()
    global mycon, cur
    if ret == 0:
        cur.execute(
            "CREATE TABLE IF NOT EXISTS STUDENTS(NAME VARCHAR(20),ROLL_NO INT,STREAM VARCHAR(20),PHONE_NO VARCHAR(10),FATHER VARCHAR(30),admission_num VARCHAR(10))")
        cur.execute("insert into STUDENTS values('{}',{},'{}','{}','{}','{}')".format(student_name.get(), roll_no.get(),
                                                                                      stream.get(), phone.get(),
                                                                                      father.get(),
                                                                                      admission_num.get()))
        mycon.commit()
        # mycon.close()
        t1.delete('1.0', END)
        t1.insert(END, "ADDED SUCCESSFULLY\n")
    t1.config(state=DISABLED)


def view_student():
    global mycon, cur
    allForm = Toplevel(root)
    allForm.title("...:::Students Database")
    allForm.geometry("900x465+250+150")
    allForm.resizable(False, False)
    query = "select * from students"
    cur.execute(query)
    ta = Text(allForm, height=40, width=400, bg="black", fg="white")
    ta.grid(row=0, column=0)
    records = cur.fetchall()
    heading = "%10s" % "NAME" + "%20s" % "ROLL NUMBER" + "%20s" % "STREAM" + "%20s" % "PHONE NUMBER" + "%20s" % "FATHER'S NAME" + "%20s" % "ADMISSION NUMBER" + '\n'

    ta.insert(END, heading)

    ta.insert(END, "=" * 150)
    ta.insert(END, '\n')
    for row in records:
        rec = "%10s" % str(row[0]) + "%20s" % row[1] + "%20s" % row[2] + "%20s" % str(row[3]) + "%20s" % row[
            4] + "%20s" % str(row[5]) + '\n'
        ta.insert(END, rec)
    ta.config(state=DISABLED)


def resetFields():
    student_name.set('')
    roll_no.set('')
    stream.set('')
    phone.set('')
    father.set('')
    admission_num.set('')


def findRecord():
    global mycon, cur
    e = roll_no.get()
    query = "select * from STUDENTS where roll_no={0}".format(e)
    cur.execute(query)
    mydata = cur.fetchone()
    if cur.rowcount > 0:
        roll_no.set(mydata[1])
        student_name.set(mydata[0])
        stream.set(mydata[2])
        phone.set(mydata[3])
        father.set(mydata[4])
        admission_num.set(mydata[5])

    else:
        messagebox.showinfo('Not Found', "NOT MATCHING STUDENT'S ROLL NUMBER ")


def search():
    global mycon, cur
    if roll_no.get():
        cur.execute("select * from STUDENTS where roll_no={}".format(roll_no.get()))
        data = cur.fetchall()
        # mycon.close()
        for i in data:
            t1.insert(END, str(i) + "\n")
    else:
        messagebox.showinfo(END, "ROLL NUMBER IS REQUIRED\n")


def delete_student():
    global mycon, cur
    t1.config(state=NORMAL)
    ret = verifier()
    response = messagebox.askquestion('Delete?', 'Are You Sure to Delete ?')
    if response == 'yes' and ret == 0:
        cur.execute("DELETE FROM STUDENTS WHERE ROLL_NO={}".format(roll_no.get()))
        mycon.commit()
        # mycon.close()
        t1.delete('1.0', END)
        t1.insert(END, "SUCCESSFULLY DELETED THE USER\n")

    t1.config(state=DISABLED)


def update_student():
    global mycon, cur
    t1.config(state=NORMAL)
    cur.execute(
        "UPDATE STUDENTS SET NAME='{}',ROLL_NO={},STREAM='{}',PHONE_NO='{}',FATHER='{}',admission_num='{}' where ROLL_NO={}".format(
            student_name.get(), roll_no.get(), stream.get(), phone.get(), father.get(), admission_num.get(),
            roll_no.get()))
    mycon.commit()
    # mycon.close()
    t1.delete('1.0', END)
    t1.insert(END, "UPDATED SUCCESSFULLY\n")
    t1.config(state=DISABLED)


def close():
    root.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("CLASS 11TH Student Management System")
    root.geometry("850x465+250+150")
    root.configure(background="cyan")
    root.resizable(False, False)

    student_name = StringVar()
    roll_no = StringVar()
    stream = StringVar()
    phone = StringVar()
    father = StringVar()
    admission_num = StringVar()

    label1 = Label(root, text="Student name:", bg='cyan', fg='black', font=('arial', 10, 'bold'))
    label1.place(x=0, y=30)

    label2 = Label(root, text="Roll no:", bg='cyan', fg='black', font=('arial', 10, 'bold'))
    label2.place(x=0, y=0)

    label3 = Label(root, text="stream:", bg='cyan', fg='black', font=('arial', 10, 'bold'))
    label3.place(x=0, y=60)

    label4 = Label(root, text="Phone Number:", bg='cyan', fg='black', font=('arial', 10, 'bold'))
    label4.place(x=0, y=90)

    label5 = Label(root, text="Father Name:", bg='cyan', fg='black', font=('arial', 10, 'bold'))
    label5.place(x=0, y=120)

    label6 = Label(root, text="admission_num:", bg='cyan', fg='black', font=('arial', 10, 'bold'))
    label6.place(x=0, y=150)

    e1 = Entry(root, textvariable=student_name)
    e1.place(x=100, y=30)

    e2 = Entry(root, textvariable=roll_no)
    e2.place(x=100, y=0)
    e2.focus_set()

    e3 = Entry(root, textvariable=stream)
    e3.place(x=100, y=60)

    e4 = Entry(root, textvariable=phone)
    e4.place(x=100, y=90)

    e5 = Entry(root, textvariable=father)
    e5.place(x=100, y=120)

    e6 = Entry(root, textvariable=admission_num)
    e6.place(x=100, y=150)

    t1 = Text(root, width=80, height=20, bg='white', fg='black', font=('arial', 10, 'bold'))
    t1.grid(row=10, column=1)
    t1.config(state=DISABLED)
    b = Button(root, text="CLEAR", command=resetFields, width=10)
    b.place(x=100, y=180)

    b1 = Button(root, text="ADD STUDENT", command=add_student, width=40, bg='dark orange', fg='black',
                font=('arial', 10, 'bold'))
    b1.grid(row=11, column=0)

    b2 = Button(root, text="VIEW ALL STUDENTS", command=view_student, width=40, bg='dark orange', fg='black',
                font=('arial', 10, 'bold'))
    b2.grid(row=12, column=0)

    b3 = Button(root, text="DELETE STUDENT", command=delete_student, width=40, bg='white', fg='black',
                font=('arial', 10, 'bold'))
    b3.grid(row=13, column=0)

    b4 = Button(root, text="UPDATE INFO", command=update_student, width=40, bg='green', fg='black',
                font=('arial', 10, 'bold'))
    b4.grid(row=14, column=0)

    b5 = Button(root, text="CLOSE", command=close, width=40, bg='green', fg='black', font=('arial', 10, 'bold'))
    b5.grid(row=15, column=0)

    b6 = Button(root, text="SEARCH", command=findRecord, width=6)
    b6.place(x=226, y=0)

    root.mainloop()
