from GUI import GUI
from faker import Faker
from Database import Database
from Patient import Patient
import random

if __name__ == "__main__":
    fake = Faker('tr_TR')
    database = Database()

    departments = ["Internal Medicine", "Cardiology", "Orthopedics", "Neurology"]
    blood_types = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

    for _ in range(400):
        first_name = fake.first_name()
        last_name = fake.last_name()
        id_number = fake.unique.numerify(text="###########")
        address = fake.address().replace("\n", " ")
        age = random.randint(1, 100)
        height = round(random.uniform(1.4, 2.0), 2)
        weight = random.randint(40, 120)
        blood_type = random.choice(blood_types)
        complaint = fake.sentence()
        department = random.choice(departments)

        patient = Patient(first_name, last_name, id_number, address, age, height, weight, blood_type, complaint, department)
        database.add_patient(patient)
    app = GUI()
    app.run()
