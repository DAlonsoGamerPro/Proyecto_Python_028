from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random

root = Tk()
root.geometry("900x500")
root.title("Connecting Jobs")

#/\/\/\Imagen/\/\/\#

image = ImageTk.PhotoImage(Image.open("CJ.jpeg"))
place_image = Label(root)
place_image["image"] = image
place_image.place(relx=0.7,rely=0.5,anchor=CENTER)

#/\/\/\Título de la App/\/\/\#

label = Label(root,text="Asignar Trabajos", font=("times",20,"bold"))
label.place(relx=0.12,rely=0.06,anchor=CENTER)

#Doctor#

label_doctor = Label(root,text="Doctor(a): ")
label_doctor.place(relx=0.04,rely=0.15,anchor=CENTER)

entry_doctor = Entry(root)
entry_doctor.place(relx=0.25,rely=0.15,anchor=CENTER)

label_selected_doctor = Label(root)
label_selected_doctor.place(relx=0.1,rely=03.,anchor=CENTER)

#Teacher#

label_teacher = Label(root,text="Profesor(a): ")
label_teacher.place(relx=0.04,rely=0.45,anchor=CENTER)

entry_teacher = Entry(root)
entry_teacher.place(relx=0.25,rely=0.45,anchor=CENTER)

label_selected_teacher = Label(root)
label_selected_teacher.place(relx=0.1,rely=33.,anchor=CENTER)

#Engineer#

label_engineer = Label(root,text="Ingeniero(a): ")
label_engineer.place(relx=0.04,rely=0.75,anchor=CENTER)

entry_engineer = Entry(root)
entry_engineer.place(relx=0.25,rely=0.75,anchor=CENTER)

label_selected_engineer = Label(root)
label_selected_engineer.place(relx=0.1,rely=0.93,anchor=CENTER)

#Clases#

class parent():
    def __init__(self):
        print("Esta es la clase padre")
        
    def doctor(doctor_name):
        hospital_list = ["Apex","Apolo","City Care","Galaxy"]
        random_hospital = random.randint(0,3)
        label_selected_doctor["text"] = "A " + doctor_name + " se le asignó " + hospital_list[random_hospital]
        
    def teacher(teacher_name):
        school_list = ["BYJU'S","Harmon hall","Howard","Educazion.net"]
        random_school = random.randint(0,3)
        label_selected_teacher["text"] = "A " + teacher_name + " se le asignó " + school_list[random_school]
        
    def engineer(engineer_name):
        street_list = ["Textitlán","Zapote","Zapata","Fifis"]
        random_street = random.randint(0,3)
        label_selected_engineer["text"] = "A " + engineer_name + " se le asignó " + street_list[random_street]
        
class child1(parent):
    def __init__(self):
        print("Esta es la clase child1")
    def getDoctor(self):
        name = entry_doctor.get()
        parent.doctor(name)
        
class child2(parent):
    def __init__(self):
        print("Esta es la clase child2")
    def getTeacher(self):
        name = entry_teacher.get()
        parent.softwareEngineer(name)
        
class child3(parent):
    def __init__(self):
        print("Esta es la clase child3")
    def getEngineer(self):
        name = entry_engineer.get()
        parent.softwareEngineer(name)
        
obj1 = child1()
obj2 = child2()
obj3 = child3()

#Botón Doctor#

btn_doctor = Button(root,text="Mostrar el Hospital Asignado",fg="white",bg="blue")
btn_doctor.place(relx=0.1,rely=0.23,anchor=CENTER)

#Botón Teacher#

btn_teacher = Button(root,text="Mostrar el Salón Asignado",fg="white",bg="blue")
btn_teacher.place(relx=0.1,rely=0.53,anchor=CENTER)

#Botón Engineer#

btn_engineer = Button(root,text="Mostrar la Calle Asignada",fg="white",bg="blue")
btn_engineer.place(relx=0.1,rely=0.83,anchor=CENTER)

root.mainloop()