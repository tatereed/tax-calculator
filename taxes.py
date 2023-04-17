def taxes(income, bracket):
    new_income = income - bracket[0]
    match bracket[10]:
        case 1:
            income_tax = new_income * 0.1
        case 2:
            income_tax = bracket[12] + ((new_income - bracket[1]) * 0.12)
        case 3:
            income_tax = bracket[13] + ((new_income - bracket[2]) * 0.22)
        case 4:
            income_tax = bracket[14] + ((new_income - bracket[3]) * 0.24)
        case 5:
            income_tax = bracket[15] + ((new_income - bracket[4]) * 0.32)
        case 6:
            income_tax = bracket[16] + ((new_income - bracket[5]) * 0.35)
        case 7:
            income_tax = bracket[17] + ((new_income - bracket[6]) * 0.37)
        case other:
            return "error"

    if income > bracket[9]:
        fica_tax = bracket[9] * 0.0765
    else:
        fica_tax = income * 0.0765

    return income_tax + fica_tax
