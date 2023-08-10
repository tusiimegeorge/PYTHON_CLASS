import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        return math.pi * self.radius**2

    def get_circumference(self):
        return 2 * math.pi * self.radius


circle1 = Circle(5)
print("Circle 1")
print("Radius:", circle1.get_radius())
print("Area:", circle1.get_area())
print("Circumference:", circle1.get_circumference())

circle2 = Circle(7)
print("\nCircle 2")
print("Radius:", circle2.get_radius())
print("Area:", circle2.get_area())
print("Circumference:", circle2.get_circumference())

circle2.set_radius(10)
print("\nUpdated Circle 2")
print("Radius:", circle2.get_radius())
print("Area:", circle2.get_area())
print("Circumference:", circle2.get_circumference())













class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def get_name(self):
        return self.name

    def get_employee_id(self):
        return self.employee_id

    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        self.salary = new_salary

    def give_raise(self, percentage):
        increase_amount = self.salary * percentage / 100
        self.salary += increase_amount

    def __str__(self):
        return f"Employee ID: {self.employee_id}\nName: {self.name}\nSalary: {self.salary}"


employee1 = Employee("Katende Brian", 12345, 60000)
print(employee1)

employee1.give_raise(10)  # Increase salary by 10%
print("\nAfter giving a raise:")
print(employee1)
