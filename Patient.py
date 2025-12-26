class Patient:
    def __init__(self, first_name, last_name, id_number, address, age, height, weight, blood_type, complaint, department):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.address = address
        self.age = age
        self.height = height
        self.weight = weight
        self.blood_type = blood_type
        self.complaint = complaint
        self.department = department
        self.bmi = self.calculate_bmi()

    def calculate_bmi(self):
        try:
            return round(self.weight / (self.height ** 2), 2)
        except:
            return 0
