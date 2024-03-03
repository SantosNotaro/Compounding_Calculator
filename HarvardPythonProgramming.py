def main():
    A = float(input(How much money is in your account?)) # money in account
    IN = float(input(how much is your Annual Percentage Rate?)) # interest rate
    Y = int(input(How many years has this been compounding?)) # years

income = (A * IN * Y) / 100

main()

def main():
    dollars = float(input("How much was the meal? ").replace('$', ''))

    percent = float(input("What percentage would you like to tip? ").replace('%', '')) / 100

    tip = dollars * percent

    print(f"Leave ${tip:.2f}")



main()

