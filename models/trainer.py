class Trainer():

    def __init__(self, name, lastName, age, phone, email):
        self.name = name
        self.lastName = lastName
        self.age = age
        self.phone = phone
        self.email = email

    def to_json(self):
        return {
            'name': self.name,
            'lastName': self.lastName,
            'age': self.age,
            'phone': self.phone,
            'email': self.email
        }

