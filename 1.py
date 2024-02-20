from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

# Example Usage:
full_time_employee = FullTimeEmployee(name="John Doe", hourly_rate=15, hours_worked=40)
salary = full_time_employee.calculate_salary()
print(f"{full_time_employee.name}'s salary is ${salary}")
