# Aggregation
class MonSal:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def ann_sal(self):
        return (self.pay * 12) + self.bonus


class Employee:
    def __init__(self, name, age, pb):
        self.name = name
        self.age = age
        self.pb = pb

    def tot_salary(self):
        return self.pb.ann_sal()


pb = MonSal(1500, 150)
emp = Employee('lone', 25, pb)
print(emp.tot_salary())
