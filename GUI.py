from tkinter import *
from tkinter import ttk, messagebox
from Patient import Patient
from Database import Database

class GUI:
    def __init__(self):
        self.database = Database()
        self.index = 0
        self.patient_list = self.database.all_patients()

        self.root = Tk()
        self.root.title("🏥 Hospital Record System")
        self.root.geometry("1100x600")

        self._create_vars()
        self._build_gui()
        self._update_screen()

    def _create_vars(self):
        self.first_name = StringVar()
        self.last_name = StringVar()
        self.id_number = StringVar()
        self.address = StringVar()
        self.age = IntVar()
        self.height = DoubleVar()
        self.weight = DoubleVar()
        self.bmi = StringVar()
        self.blood_type = StringVar()
        self.department = StringVar()

    def _build_gui(self):
        Label(self.root, text="🏥 HOSPITAL RECORD SYSTEM", font=("Arial", 18, "bold")).pack(pady=10)

        frame1 = Frame(self.root, bg="#e8f0fe", bd=2, relief="groove")
        frame1.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=5)
        Label(frame1, text="👤 PERSONAL INFORMATION", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=5)

        entries = [("First Name:", self.first_name), ("Last Name:", self.last_name), ("ID:", self.id_number), ("Address:", self.address)]
        for i, (text, var) in enumerate(entries):
            Label(frame1, text=text).grid(row=i+1, column=0, sticky="e", padx=5, pady=5)
            Entry(frame1, textvariable=var, width=30).grid(row=i+1, column=1, padx=5, pady=5)

        frame2 = Frame(self.root, bg="#fffde7", bd=2, relief="groove")
        frame2.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=5)
        Label(frame2, text="🩺 PATIENT INFORMATION", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=5)

        Label(frame2, text="Age:").grid(row=1, column=0, sticky="e")
        Entry(frame2, textvariable=self.age).grid(row=1, column=1)

        Label(frame2, text="Height (m):").grid(row=2, column=0, sticky="e")
        Entry(frame2, textvariable=self.height).grid(row=2, column=1)

        Label(frame2, text="Weight (kg):").grid(row=3, column=0, sticky="e")
        Entry(frame2, textvariable=self.weight).grid(row=3, column=1)

        Label(frame2, text="BMI:").grid(row=4, column=0, sticky="e")
        Label(frame2, textvariable=self.bmi).grid(row=4, column=1, sticky="w")

        Button(frame2, text="Calculate BMI", command=self._calculate_bmi).grid(row=5, column=0, columnspan=2, pady=5)

        Label(frame2, text="Blood Type:").grid(row=6, column=0, sticky="e")
        ttk.Combobox(frame2, textvariable=self.blood_type, values=["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]).grid(row=6, column=1)

        Label(frame2, text="Complaint:").grid(row=7, column=0, sticky="ne")
        self.complaint_text = Text(frame2, width=25, height=3)
        self.complaint_text.grid(row=7, column=1)

        Label(frame2, text="Department:").grid(row=8, column=0, sticky="e")
        ttk.Combobox(frame2, textvariable=self.department, values=["Internal Medicine", "Cardiology", "Orthopedics", "Neurology"]).grid(row=8, column=1)

        nav_frame = Frame(self.root)
        nav_frame.pack()
        Button(nav_frame, text="⏮ Previous", command=self.previous).pack(side=LEFT, padx=10, pady=10)
        Button(nav_frame, text="Next ⏭", command=self.next).pack(side=LEFT)

        control_frame = Frame(self.root)
        control_frame.pack(pady=10)
        Button(control_frame, text="✅ ADD", command=self.add).pack(side=LEFT, padx=5)
        Button(control_frame, text="✏️ UPDATE", command=self.update).pack(side=LEFT, padx=5)
        Button(control_frame, text="🗑 DELETE", command=self.delete).pack(side=LEFT, padx=5)
        Button(control_frame, text="🚫 CLEAR FILE", command=self.clear_database_popup).pack(side=LEFT, padx=5)

        exit_frame = Frame(self.root)
        exit_frame.pack(pady=10)
        Button(exit_frame, text="EXIT", command=self.root.destroy, bg="red", fg="white").pack()

    def _calculate_bmi(self):
        try:
            bmi_calc = round(self.weight.get() / (self.height.get() ** 2), 2)
            self.bmi.set(str(bmi_calc))
        except:
            self.bmi.set("Invalid input")

    def add(self):
        patient = Patient(
            self.first_name.get(), self.last_name.get(), self.id_number.get(), self.address.get(),
            self.age.get(), self.height.get(), self.weight.get(),
            self.blood_type.get(), self.complaint_text.get("1.0", END).strip(), self.department.get()
        )
        self.database.add_patient(patient)
        messagebox.showinfo("Success", "Patient added")
        self.patient_list = self.database.all_patients()
        self.index = len(self.patient_list) - 1
        self._update_screen()

    def update(self):
        if not self.patient_list:
            return
        selected_id = self.patient_list[self.index][0]
        patient = Patient(
            self.first_name.get(), self.last_name.get(), self.id_number.get(), self.address.get(),
            self.age.get(), self.height.get(), self.weight.get(),
            self.blood_type.get(), self.complaint_text.get("1.0", END).strip(), self.department.get()
        )
        self.database.hasta_guncelle(selected_id, patient)
        messagebox.showinfo("Success", "Patient information updated.")
        self.patient_list = self.database.all_patients()
        self._update_screen()

    def delete(self):
        if not self.patient_list:
            return
        selected_id = self.patient_list[self.index][0]
        self.database.all_patients(selected_id)
        messagebox.showinfo("Deleted", "Patient record deleted.")
        self.patient_list = self.database.all_patients()
        self.index = max(0, self.index - 1)
        self._update_screen()

    def previous(self):
        if self.index > 0:
            self.index -= 1
            self._update_screen()

    def next(self):
        if self.index < len(self.patient_list) - 1:
            self.index += 1
            self._update_screen()

    def _update_screen(self):
        if not self.patient_list:
            self._clear_fields()
            return
        patient = self.patient_list[self.index]
        self.first_name.set(patient[1])
        self.last_name.set(patient[2])
        self.id_number.set(patient[3])
        self.address.set(patient[4])
        self.age.set(patient[5])
        self.height.set(patient[6])
        self.weight.set(patient[7])
        self.bmi.set(patient[8])
        self.blood_type.set(patient[9])
        self.complaint_text.delete("1.0", END)
        self.complaint_text.insert(END, patient[10])
        self.department.set(patient[11])

    def _clear_fields(self):
        self.first_name.set("")
        self.last_name.set("")
        self.id_number.set("")
        self.address.set("")
        self.age.set(0)
        self.height.set(0.0)
        self.weight.set(0.0)
        self.bmi.set("")
        self.blood_type.set("")
        self.complaint_text.delete("1.0", END)
        self.department.set("")

    def clear_database_popup(self):
        window = Toplevel(self.root)
        window.title("Delete Database")
        Label(window, text="Are you sure you want to delete all records?", fg="red").pack(pady=10)
        Button(window, text="Yes", command=lambda: [self.database.clear_database(), window.destroy(), messagebox.showinfo("Deleted", "All data deleted"), self._clear_fields()]).pack(pady=5)
        Button(window, text="Cancel", command=window.destroy).pack()

    def run(self):
        self.root.mainloop()
