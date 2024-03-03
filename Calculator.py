import time

def AutoRestartCode():
    def compound_interest(pr, r, t):
        n = 1

        FV = pr * (1 + r / (n * 100)) ** (n * t)

        return FV

    # Get input from the user
    M = float(input("How much money is in your account?: "))
    APR = float(input("How much is your Annual Percentage Rate?: "))
    Y = int(input("How many years has this been compounding?: "))

    # Call the compound_interest function to calculate the future value
    FV = compound_interest(M, APR, Y)  # FV

    # Print the result
    print(f"The future value after {Y} years is: {FV:.2f}")

def main():
    while True:
        AutoRestartCode()
        time.sleep(1)  # Optional: Add a short delay between runs

if __name__ == "__main__":
    main()