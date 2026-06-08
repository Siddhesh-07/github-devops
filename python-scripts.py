import json
import logging
from datetime import datetime
from statistics import mean

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def to_dict(self):
        return {
            "id": self.emp_id,
            "name": self.name,
            "department": self.department,
            "salary": self.salary
        }

    def __str__(self):
        return f"{self.name} ({self.department}) - ₹{self.salary}"


class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_average_salary(self):
        return mean(emp.salary for emp in self.employees)

    def highest_paid_employee(self):
        return max(self.employees, key=lambda e: e.salary)

    def save_to_json(self, filename):
        with open(filename, "w") as f:
            json.dump([e.to_dict() for e in self.employees], f, indent=4)

    def display_report(self):
        print("\nEMPLOYEE REPORT")
        print("-" * 50)

        for emp in self.employees:
            print(emp)

        print("-" * 50)
        print(f"Average Salary: ₹{self.get_average_salary():,.2f}")
        print(f"Highest Paid: {self.highest_paid_employee().name}")
        print("-" * 50)


def generate_sample_data():
    manager = EmployeeManager()

    employees = [
        Employee(101, "Rahul", "DevOps", 60000),
        Employee(102, "Priya", "Data Science", 75000),
        Employee(103, "Amit", "Cloud", 80000),
        Employee(104, "Neha", "Automation", 70000),
        Employee(105, "Vikas", "Security", 90000),
    ]

    for emp in employees:
        manager.add_employee(emp)

    return manager


def calculate_bonus(salary, percentage):
    return salary * (percentage / 100)


def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]


def write_log(message):
    logging.info(message)


def create_text_report(filename):
    with open(filename, "w") as file:
        file.write("System Report\n")
        file.write("=" * 40 + "\n")
        file.write(f"Generated: {datetime.now()}\n")
        file.write("Status: SUCCESS\n")


def main():
    print("Starting Application...\n")

    manager = generate_sample_data()

    manager.display_report()

    print("\nBONUS CALCULATIONS")
    print("-" * 30)

    for emp in manager.employees:
        bonus = calculate_bonus(emp.salary, 10)
        print(f"{emp.name}: ₹{bonus:,.2f}")

    print("\nFIBONACCI SERIES")
    print("-" * 30)
    print(fibonacci(20))

    manager.save_to_json("employees.json")
    create_text_report("report.txt")

    write_log("Employee data exported.")
    write_log("Report generated successfully.")

    print("\nFiles created:")
    print("- employees.json")
    print("- report.txt")

    print("\nApplication completed successfully.")


if __name__ == "__main__":
    main()
