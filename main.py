
import json
import os


class Employee:

    def __init__(self, emp_id, name, age, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def display(self):
        print("\nEmployee ID:", self.emp_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)
        print("Salary:", self.salary)

    def to_dict(self):
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "age": self.age,
            "department": self.department,
            "salary": self.salary
        }


class EmployeeManagement:

    FILE_NAME = "employees.json"

    def __init__(self):
        self.employees = []
        self.load_data()

    # Load employee data from file
    def load_data(self):

        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "r") as file:
                data = json.load(file)

                for emp in data:
                    employee = Employee(
                        emp["emp_id"],
                        emp["name"],
                        emp["age"],
                        emp["department"],
                        emp["salary"]
                    )

                    self.employees.append(employee)

    # Save employee data
    def save_data(self):

        data = []

        for emp in self.employees:
            data.append(emp.to_dict())

        with open(self.FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

    # Add employee
    def add_employee(self):

        emp_id = input("Enter Employee ID: ")

        for emp in self.employees:
            if emp.emp_id == emp_id:
                print("Employee ID already exists!")
                return

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        employee = Employee(emp_id, name, age, department, salary)

        self.employees.append(employee)

        self.save_data()

        print("Employee added successfully!")

    # Display all employees
    def view_employees(self):

        if len(self.employees) == 0:
            print("No employees found!")
            return

        for emp in self.employees:
            emp.display()

    # Search employee
    def search_employee(self):

        emp_id = input("Enter Employee ID to search: ")

        for emp in self.employees:

            if emp.emp_id == emp_id:
                emp.display()
                return

        print("Employee not found!")

    # Update employee salary
    def update_salary(self):

        emp_id = input("Enter Employee ID: ")

        for emp in self.employees:

            if emp.emp_id == emp_id:

                new_salary = float(input("Enter new salary: "))

                emp.salary = new_salary

                self.save_data()

                print("Salary updated successfully!")
                return

        print("Employee not found!")

    # Delete employee
    def delete_employee(self):

        emp_id = input("Enter Employee ID to delete: ")

        for emp in self.employees:

            if emp.emp_id == emp_id:

                self.employees.remove(emp)

                self.save_data()

                print("Employee deleted successfully!")
                return

        print("Employee not found!")


# Main program
def main():

    management = EmployeeManagement()

    while True:

        print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Salary")
        print("5. Delete Employee")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            management.add_employee()

        elif choice == "2":
            management.view_employees()

        elif choice == "3":
            management.search_employee()

        elif choice == "4":
            management.update_salary()

        elif choice == "5":
            management.delete_employee()

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
