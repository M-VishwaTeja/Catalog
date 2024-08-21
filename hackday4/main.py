
import datetime
import json
import os

# Classes to represent various entities
class Child:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        self.vaccinations = []
        self.reminders = []

    def add_vaccination(self, vaccine_name, date):
        self.vaccinations.append({"vaccine": vaccine_name, "date": date})
        self.set_reminder(vaccine_name, date)

    def set_reminder(self, vaccine_name, date):
        reminder_date = date - datetime.timedelta(days=3)  # Reminder 3 days before vaccination
        self.reminders.append({"vaccine": vaccine_name, "reminder_date": reminder_date})

    def view_vaccinations(self):
        print(f"\nVaccination records for {self.name}:")
        for record in self.vaccinations:
            print(f"Vaccine: {record['vaccine']}, Date: {record['date']}")

    def view_reminders(self):
        print(f"\nReminders for {self.name}:")
        for reminder in self.reminders:
            print(f"Vaccine: {reminder['vaccine']}, Reminder Date: {reminder['reminder_date']}")

    def to_dict(self):
        return {
            "name": self.name,
            "dob": self.dob.strftime("%Y-%m-%d"),
            "vaccinations": self.vaccinations,
            "reminders": self.reminders
        }

    @classmethod
    def from_dict(cls, data):
        child = cls(data["name"], datetime.datetime.strptime(data["dob"], "%Y-%m-%d").date())
        child.vaccinations = data["vaccinations"]
        child.reminders = data["reminders"]
        return child


class VaccinationManagementSystem:
    def __init__(self):
        self.children = {}
        self.load_data()

    def add_child(self, name, dob):
        if name in self.children:
            print("Child already exists.")
        else:
            self.children[name] = Child(name, dob)
            self.save_data()
            print(f"Child {name} added successfully.")

    def book_appointment(self, name, vaccine_name, date):
        if name not in self.children:
            print("Child not found.")
        else:
            self.children[name].add_vaccination(vaccine_name, date)
            self.save_appointment(name, vaccine_name, date)
            print(f"Appointment for {vaccine_name} on {date} booked successfully.")

    def view_child_records(self, name):
        if name not in self.children:
            print("Child not found.")
        else:
            self.children[name].view_vaccinations()
            self.children[name].view_reminders()

    def save_data(self):
        with open("children_data.json", "w") as file:
            data = {name: child.to_dict() for name, child in self.children.items()}
            json.dump(data, file)

    def load_data(self):
        if os.path.exists("children_data.json"):
            with open("children_data.json", "r") as file:
                data = json.load(file)
                self.children = {name: Child.from_dict(child_data) for name, child_data in data.items()}

    def save_appointment(self, name, vaccine_name, date):
        with open("appointments.txt", "a") as file:
            file.write(f"{name} - Vaccine: {vaccine_name}, Date: {date}\n")

    def view_appointments(self):
        if os.path.exists("appointments.txt"):
            with open("appointments.txt", "r") as file:
                print("\nAppointments:\n")
                print(file.read())
        else:
            print("No appointments found.")

    def show_help(self):
        print("""
        Child Vaccination Management System Help:
        1. Add Child - Adds a new child to the system. Requires the child's name and date of birth.
        2. Book Vaccination Appointment - Schedules a vaccination for a child. Requires child's name, vaccine name, and date.
        3. View Child Records - Shows the vaccination history and reminders for a specific child.
        4. View Appointments - Displays all booked appointments.
        5. Help - Displays this help menu.
        6. Exit - Exits the system.
        """)


# Utility functions
def input_date(prompt):
    while True:
        try:
            return datetime.datetime.strptime(input(prompt), "%Y-%m-%d").date()
        except ValueError:
            print("Please enter a valid date in YYYY-MM-DD format.")

def main():
    system = VaccinationManagementSystem()

    while True:
        print("\nChild Vaccination Management System")
        print("1. Add Child")
        print("2. Book Vaccination Appointment")
        print("3. View Child Records")
        print("4. View Appointments")
        print("5. Help")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter child's name: ")
            dob = input_date("Enter child's date of birth (YYYY-MM-DD): ")
            system.add_child(name, dob)
        elif choice == "2":
            name = input("Enter child's name: ")
            vaccine_name = input("Enter vaccine name: ")
            date = input_date("Enter vaccination date (YYYY-MM-DD): ")
            system.book_appointment(name, vaccine_name, date)
        elif choice == "3":
            name = input("Enter child's name: ")
            system.view_child_records(name)
        elif choice == "4":
            system.view_appointments()
        elif choice == "5":
            system.show_help()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
