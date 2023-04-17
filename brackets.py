import brackets_templates
def brackets(filing, year, income):

    bracket = []
    # j decides which part of the template is used to make the bracket

    if filing == "single":
        j = 0
    elif filing == "married":
        j = 10
    elif filing == "hoh":
        j = 20
    else:
        print("error in setting filing")
        return
    # k decides which template to use based off of year

    if year == 2023:
        k = brackets_templates._2023_template
    elif year == 2022:
        k = brackets_templates._2022_template
    else:
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

            if i == 2:
                l = 0.12
            elif  i == 3:
                l = 0.22
            elif  i == 4:
                l = 0.24
            elif  i == 5:
                l = 0.32
            elif  i == 6:
                l = 0.35
            else:
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
