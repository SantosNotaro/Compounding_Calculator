import time
# Calculator restarts after total is calculated
def AutoRestartCode():
    def compound_interest(pr, r, t): #Compound Interest Formula
        n = 1

        FV = pr * (1 + r / (n * 100)) ** (n * t)

        return FV

    # Get input from the user
    M = float(input("How much money is in your account?: ").replace('$', '').replace(',', ''))
    APR = float(input("What is your Annual Percentage Rate?: ").replace('%', ''))
    Y = int(input("How many years has this been compounding?: "))

    # Call the compound_interest function to calculate the future value
    FV = compound_interest(M, APR, Y)

    # Print the result
    print(f"The future value after {Y} years is: ${FV:.2f}")

def main():
    while True:
        AutoRestartCode()
        time.sleep(1)  # Time(seconds) delay between code restarts

if __name__ == "__main__":
    main()