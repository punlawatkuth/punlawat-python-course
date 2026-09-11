def calculate_electricity_cost(units):
    unitprices = 0.00
    tempunit =  units
    totalservicefees = 25.00
    if units < 0:
        print("invalid! please enter the correct amount")
        return
    if units >= 0 and units <= 50:
        if units == 0:
             print(f"electricity bill info:\n 1-50 unit: {unitprices} baht \n services fee: 25.00 baht \n total fee: {totalservicefees}") 
        elif units < 50:
            tempunit - 50
            unitprices = 2.50 * tempunit
            totalservicefees =+ unitprices
            print(f"electricity bill info:\n 1-50 unit: {unitprices} baht \n services fee: 25.00 baht \n total fee: {totalservicefees}") 
        unitprices += 2.50 * 50
        print(f"electricity bill info:\n 1-50 unit: {unitprices} baht \n services fee: 25.00 baht \n total fee: {totalservicefees}") 
    elif units >= 51 and units <= 100:
        if units < 100:
                    tempunit - 100
                    unitprices = 3.00 * tempunit
                    totalservicefees =+ unitprices
                    print(f"electricity bill info:\n 1-50 unit: 125 baht \n 51-100 unit: {unitprices} baht \n services fee: 25.00 baht \n total fee: {totalservicefees}")
        unitprices += 3.00 * 50
        print(f"electricity bill info:\n 1-50 unit: 125 baht \n 51-100 unit: {unitprices} baht \n services fee: 25.00 baht \n total fee: {totalservicefees}") 
    elif units >= 101 and units <= 200:
        if units < 200:
             tempunit - 200
             unitprices = 3.50 * tempunit
             totalservicefees =+ unitprices
             print(f"electricity bill info:\n 1-50 unit: 125 baht \n 51-100 unit: 150 baht \n 101-200 unit: {unitprices} baht \n services fee: 25.00 baht \n total fee: {totalservicefees}")
        unitprices = 3.50 * 20
        print(f"electricity bill info:\n 1-50 unit: 125 baht \n 51-100 unit: 150 baht \n 101-200 unit: {unitprices} baht \n services fee: 25.00 baht \n total fee: {totalservicefees}")
    elif units > 200:
        units - 200
        unitprices = 4.00 * units
        totalservicefees =+ unitprices
        print(f"electricity bill info:\n 1-50 unit: 125 baht \n 51-100 unit: 150 baht \n 101-200 unit: 350 baht \n 200+ units: {unitprices} \n services fee: 25.00 baht \n total fee: {totalservicefees}")

while True:
    print("===== electricity calculate program =====")
    print("1. enter the program")
    print("2. exit the program")
    choices = input("choose the menu: ")
    if choices == "1":
         units = float(input("please enter your electricity unit: "))
         calculate_electricity_cost(units)
    elif choices == "2":
         break
    else:
         print("invalid!")