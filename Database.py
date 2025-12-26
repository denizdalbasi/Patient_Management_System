import sqlite3

class Database:
    def __init__(self, file_name="PatientData.db"):
        self.file_name = file_name
        self.connection = sqlite3.connect(self.file_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT, last_name TEXT, id_number TEXT, address TEXT,
                age INTEGER, height REAL, weight REAL, bmi REAL,
                blood_type TEXT, complaint TEXT, department TEXT
            )
        """)
        self.connection.commit()

    def add_patient(self, patient):
        self.cursor.execute("""
            INSERT INTO patients (first_name, last_name, id_number, address, age, height, weight, bmi, blood_type, complaint, department)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            patient.first_name, patient.last_name, patient.id_number, patient.address, patient.age,
            patient.height, patient.weight, patient.bmi, patient.blood_type, patient.complaint, patient.department
        ))
        self.connection.commit()

    def update_patient(self, patient_id, patient):
        self.cursor.execute("""
            UPDATE patients SET
                first_name = ?, last_name = ?, id_number = ?, address = ?, age = ?,
                height = ?, weight = ?, bmi = ?, blood_type = ?, complaint = ?, department = ?
            WHERE id = ?
        """, (
            patient.first_name, patient.last_name, patient.id_number, patient.address, patient.age,
            patient.height, patient.weight, patient.bmi, patient.blood_type, patient.complaint, patient.department,
            patient_id
        ))
        self.connection.commit()

    def delete_patient(self, patient_id):
        self.cursor.execute("DELETE FROM patients WHERE id = ?", (patient_id,))
        self.connection.commit()

    def all_patients(self):
        self.cursor.execute("SELECT * FROM patients")
        return self.cursor.fetchall()

    def clear_database(self):
        self.cursor.execute("DELETE FROM patients")
        self.connection.commit()

    def close(self):
        self.connection.close()
