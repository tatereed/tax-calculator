def taxes(income, bracket):
    new_income = income - bracket[0]

    if bracket[10] == 1:
        income_tax = new_income * 0.1
    elif bracket[10] == 2:
        income_tax = bracket[12] + ((new_income - bracket[1]) * 0.12)
    elif bracket[10] == 3:
        income_tax = bracket[13] + ((new_income - bracket[2]) * 0.22)
    elif bracket[10] == 4:
        income_tax = bracket[14] + ((new_income - bracket[3]) * 0.24)
    elif bracket[10] == 5:
        income_tax = bracket[15] + ((new_income - bracket[4]) * 0.32)
    elif bracket[10] == 6:
        income_tax = bracket[16] + ((new_income - bracket[5]) * 0.35)
    elif bracket[10] == 7:
        income_tax = bracket[17] + ((new_income - bracket[6]) * 0.37)
    else:
        return "error"

    if income > bracket[9]:
        fica_tax = bracket[9] * 0.0765
    else:
        fica_tax = income * 0.0765

    return income_tax + fica_tax
