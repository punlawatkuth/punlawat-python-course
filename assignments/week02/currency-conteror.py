def usdcalc(thb):
    usdrate = 35.5
    usd = thb / usdrate
    return usd


def thbcalc(usd):
    thbrate = 35.5
    thb = usd * thbrate
    return thb


print("Please choose the desired conversion")
print("1. THB to USD")
print("2. USD to THB")
choices = input("Enter your choice: ").strip().upper()

if choices == "1" or choices == "THB":
    thb = float(input("Please enter your THB: "))
    usd = usdcalc(thb)
    print(f"Your conversion will be: {usd:.2f} USD")

elif choices == "2" or choices == "USD":
    usd = float(input("Please enter your USD: "))
    thb = thbcalc(usd)
    print(f"Your conversion will be: {thb:.2f} THB")

else:
    print("Invalid choice")