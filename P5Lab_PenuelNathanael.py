# Nathanael Penuel
# 2024-11-17
# P5LAB
# This program simulates a self-checkout machine.

import random

# 1. Import the random module to generate a random total amount owed.
# 2. Define a function named disperse_change to calculate the breakdown of change.
# 3. Define a main function.
# 4. Call the main function to run the program.

# Calculate and display change breakdown
def disperse_change(change):
    # Calculate the number of dollars
    dollars = int(change // 1)
    change = round(change - dollars * 1, 2)

    # Calculate the number of quarters
    quarters = int(change // 0.25)
    change = round(change - quarters * 0.25, 2)

    # Calculate the number of dimes
    dimes = int(change // 0.10)
    change = round(change - dimes * 0.10, 2)

    # Calculate the number of nickels
    nickels = int(change // 0.05)
    change = round(change - nickels * 0.05, 2)

    # Calculate the number of pennies
    pennies = int(change // 0.01)

    # Display the results
    print(f"\n{dollars} Dollars")
    print(f"{quarters} Quarters")
    print(f"{dimes} Dimes")
    print(f"{nickels} Nickels")
    print(f"{pennies} Pennies")

# Main function
def main():
    # Generate a random float value for the total owed
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${total_owed}")

    # Prompt the user for the amount of cash entered
    payment = 0.0
    while payment < total_owed:
        try:
            payment = float(input("How much cash will you put in the self-checkout? "))
            if payment < total_owed:
                print("Insufficient payment. Please enter an amount greater than or equal to the total owed.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Calculate the change owed
    change = round(payment - total_owed, 2)
    print(f"Change is: ${change}")

    # Call the disperse_change function to break down the change
    disperse_change(change)

# Call the main function
if __name__ == "__main__":
    main()
