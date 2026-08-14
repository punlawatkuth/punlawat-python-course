#func changin currencies
#THB TO USD
def Currencies(thb,usdz):
    if usdz == "USD":
        result = thb / 32.0
        print(f"{result:.2f} usd")
    elif usdz == "THB":
        result = thb * 32.0
        print(f"{result:.2f} thb")


print("using the func")
Currencies(100, "USD")
Currencies(100, "THB")
        