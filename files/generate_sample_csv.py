import csv
import random
from faker import Faker

fake = Faker()

header = ["first_name", "last_name", "age", "gender", "email", "city", "state", "country"]
genders = ["Male", "Female", "Other"]

with open("/workspaces/python-practice/lists/sample_customers.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    for _ in range(1000):
        first_name = fake.first_name()
        last_name = fake.last_name()
        age = random.randint(18, 80)
        gender = random.choice(genders)
        email = fake.email()
        city = fake.city()
        state = fake.state()
        country = fake.country()
        writer.writerow([first_name, last_name, age, gender, email, city, state, country])
print("sample_customers.csv generated with 1000 rows.")
