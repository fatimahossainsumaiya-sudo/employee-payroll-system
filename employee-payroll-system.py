import matplotlib.pyplot as plt

# -------- Base Class --------
class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def calculate_gross_salary(self):
        raise NotImplementedError

    def calculate_tax(self, gross_salary):
        if gross_salary <= 50000:
            return gross_salary * 0.10
        elif gross_salary <= 100000:
            return gross_salary * 0.20
        else:
            return gross_salary * 0.30

    def calculate_net_salary(self):
        gross = self.calculate_gross_salary()
        tax = self.calculate_tax(gross)
        return gross - tax


# -------- Child Classes --------
class SalariedEmployee(Employee):
    def __init__(self, name, department, monthly_salary):
        super().__init__(name, department)
        self.monthly_salary = monthly_salary

    def calculate_gross_salary(self):
        return self.monthly_salary


class HourlyEmployee(Employee):
    def __init__(self, name, department, hourly_rate, hours_worked):
        super().__init__(name, department)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_gross_salary(self):
        return self.hourly_rate * self.hours_worked


# -------- Payroll Processing --------
employees = [
    SalariedEmployee("Alice", "IT", 90000),
    SalariedEmployee("Bob", "HR", 45000),
    HourlyEmployee("Charlie", "IT", 500, 160),
    HourlyEmployee("David", "Finance", 600, 170),
    SalariedEmployee("Eva", "Finance", 120000),
]

department_payout = {}


for emp in employees:
    net_salary = emp.calculate_net_salary()
    department_payout[emp.department] = department_payout.get(emp.department, 0) + net_salary


# -------- Visualization --------
departments = list(department_payout.keys())
payouts = list(department_payout.values())

plt.bar(departments, payouts, color="maroon")
plt.xlabel("Department")
plt.ylabel("Total Monthly Payout")
plt.title("Department-wise Payroll Distribution")
plt.tight_layout()
plt.show()

