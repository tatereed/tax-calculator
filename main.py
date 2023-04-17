import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from brackets import brackets
from taxes import taxes





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
    bracket = brackets("married", 2023, 45000)
    tax_bill = taxes(45000, bracket)
    print(tax_bill)




    #x = []
    #k = 30000
    #j = True
    #while j == True:
    #    x.append(k)
    #    if k == 1000000:
    #        j = False
    #    else:
    #        k += 5000

    #y1 = []
    #y2 = []
    #y3 = []
    #for i in range(0, len(x)):
    #    y1.append(taxes(x[i], brackets("single", 2023, x[i])))
    #for i in range(0, len(x)):
    #    y2.append(taxes(x[i], brackets("married", 2023, x[i])))
    #for i in range(0, len(x)):
    #    y3.append(taxes(x[i], brackets("hoh", 2023, x[i])))

    #plt.plot(x,y1, linewidth="1", marker="o")
    #plt.plot(x,y2, linewidth="1", marker="o")
    #plt.plot(x,y3, linewidth="1", marker="o")
    #plt.show()















if __name__ == "__main__":
    main()
