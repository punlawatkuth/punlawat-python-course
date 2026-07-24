balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        if choice == "1":
            print(f"{balance:.2f}")
            break
        elif choice == "2":
            withdraw = float(input("please enter the desired amount to withdraw:  "))
            if withdraw > 1000 or withdraw < 0:
                print("insufficient balance or incorrect amount")
                break
            else:
                balance -= withdraw
                print(f"withdrew {withdraw:.2f}!")
                print(f"current balance: {balance:.2f}")
                break
        elif choice == "3":
            deposit = float(input("Please enter the desired amount to deposit:  "))
            deposit + balance
            deposit == balance
            print(f"deposited {deposit:.2f}!")
            break
        elif choice == "4":
            break
else:
    print("Invalid PIN")