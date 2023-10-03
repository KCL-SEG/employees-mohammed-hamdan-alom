"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
    def __init__(self, name, contract, commission=None):
        self.name = name
        self.contract = contract
        self.commission = commission

    def get_pay(self):
        total_pay = self.contract.get_salary()
        if self.commission:
            total_pay += self.commission.get_commission()
        return total_pay

    def __str__(self):
        if self.commission:
            return f'{self.name} works {self.contract.get_contract_string()} {self.commission.get_commission_string()} Their total pay is {self.get_pay()}.'
        else:
            return f'{self.name} works {self.contract.get_contract_string()}. Their total pay is {self.get_pay()}.'

class Contract:
    def get_salary(self):
        pass

    def get_contract_string(self):
        pass


class HourlyContract(Contract):
    def __init__(self, wage, hours):
        self.wage = wage
        self.hours = hours

    def get_salary(self):
        return self.wage * self.hours

    def get_contract_string(self):
        return f"on a contract of {self.hours} hours at {self.wage}/hour"


class MonthlyContract(Contract):
    def __init__(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary

    def get_contract_string(self):
        return f"on a monthly salary of {self.salary}"


class Commission:
    def get_commission(self):
        pass

    def get_commission_string(self):
        pass


class BonusCommission(Commission):
    def __init__(self, commission):
        self.commission = commission

    def get_commission(self):
        return self.commission

    def get_commission_string(self):
        return f"and receives a bonus commission of {self.commission}."


class ContractCommission(Commission):
    def __init__(self, number_of_contracts, commission_per_contract):
        self.number_of_contracts = number_of_contracts
        self.commission_per_contract = commission_per_contract

    def get_commission(self):
        return self.number_of_contracts * self.commission_per_contract

    def get_commission_string(self):
        return f"and receives a commission for {self.number_of_contracts} contract(s) at {self.commission_per_contract}/contract."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', MonthlyContract(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlyContract(25, 100))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', MonthlyContract(3000), ContractCommission(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlyContract(25, 150), ContractCommission(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', MonthlyContract(2000), BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlyContract(30, 120), BonusCommission(600))



