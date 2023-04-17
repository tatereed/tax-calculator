def brackets(filing, year, income):
    _2023_template = [
        # single 2023
        # x0: standard deduction
        # x1-6: tax brackets - 10,12,22,24,32,35,37
        # x7-8: capital gains tax brackets - 15,20
        # x9: maximum taxable income for fica
        13850,
        11000,
        44725,
        95375,
        182100,
        231250,
        578125,
        44625,
        492300,
        160200,
        # married 2023
        27700,
        22000,
        89450,
        190750,
        364200,
        462500,
        693750,
        89250,
        553850,
        320400,
        # hoh 2023
        20800,
        15700,
        59850,
        95350,
        182100,
        231250,
        578100,
        59750,
        523050,
        160200
    ]
    bracket = []
    # j decides which part of the template is used to make the bracket
    match filing:
        case "single":
            j = 0
        case "married":
            j = 10
        case "hoh":
            j = 20
        case other:
            print("error in setting filing")
            return
    # k decides which template to use based off of year
    match year:
        case 2023:
            k = _2023_template
        case other:
            print("error in setting year template")
            return

    # this makes the bracket from the template
    for i in range(j, j + 10):
        bracket.append(k[i])

    # first 0 takes the place of where the next standard deduction would be
    # the second zero shows that the first bracket does not have to subtract anything
    bracket.append(0)
    bracket.append(0)
    for i in range(1, 7):
        if i == 1:
            bracket.append(bracket[i] * 0.1)
        else:
            match i:
                case 2:
                    l = 0.12
                case 3:
                    l = 0.22
                case 4:
                    l = 0.24
                case 5:
                    l = 0.32
                case 6:
                    l = 0.35
                case other:
                    print("error in giving tax percentage")
                    return

            bracket.append(
                bracket[len(bracket) - 1] + ((bracket[i] - bracket[i - 1]) * l)
            )

    income = income - bracket[0]
    if income <= bracket[1]:
        bracket[10] = 1
    elif bracket[1] < income <= bracket[2]:
        bracket[10] = 2
    elif bracket[2] < income <= bracket[3]:
        bracket[10] = 3
    elif bracket[3] < income <= bracket[4]:
        bracket[10] = 4
    elif bracket[4] < income <= bracket[5]:
        bracket[10] = 5
    elif bracket[5] < income <= bracket[6]:
        bracket[10] = 6
    elif bracket[6] < income:
        bracket[10] = 7

    return bracket
