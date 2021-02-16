# Composition
class MonSal:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def ann_sal(self):
        return (self.pay * 12) + self.bonus


class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.new = MonSal(pay, bonus)

    def tot_salary(self):
        return self.new.ann_sal()


emp = Employee('lone', 25, 1500, 150)
print(emp.tot_salary())
