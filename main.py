

from brackets import brackets
from taxes import taxes
from budgeting import budgeting




def main():
    # these are your starting parameters to find out what you need
    # income = 15000
    # year = 2023
    # filing = "single"

    # fetches the bracket that will be used for your taxes
    # bracket = [
    # 0: standard deduction
    # 1-6: tax brackets income
    # 7-8: tax brackets capital
    # 9: max taxable income fica
    # 10: bracket number
    # 11: placeholder
    # 12-17: maximum taxes for each previous bracket
    # ]
    bracket = brackets("single", 2023, 45000)
    tax_bill = taxes(45000, bracket)
    budgeting(45000, tax_bill)




















if __name__ == "__main__":
    main()
