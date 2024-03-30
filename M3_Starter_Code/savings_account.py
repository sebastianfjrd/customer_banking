"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    interest_rate = 0
    #Account = Account(balance,interest_rate)
    # Calculate interest earned
     # ADD YOUR CODE HERE
    interest_earned = balance * (interest_rate/100 * months/12)
    interest_earned = balance * interest_rate
    balance += interest_earned
    print(f"The new balance is: {balance}")
    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE

    # Return the updated balance and interest earned.
    return balance, interest_earned
# ADD YOUR CODE HERE

if __name__ == "__main__":
    create_savings_account