"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account
def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        cd_balance (float): The initial balance of the CD account.
        interest_rate (float): The interest rate for the CD account.
        months (int): The length of the CD in months.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account`   and pass in the balance and interest parameters.
    cd_account = Account(balance, 0)
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    

    # Calculate interest earned
    # ADD YOUR CODE HERE
    
    interest_earned = balance * (interest_rate / 100) * (months / 12)

    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE
    updated_balance = balance + interest_earned
    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    cd_account.set_balance(updated_balance)

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    cd_account.set_interest(interest_earned)
    # Return the updated balance and interest earned.
    # ADD YOUR CODE HERE
    return updated_balance, interest_earned
# if __name__ == "__main__":
#     cd_balance = float(input("Enter the CD balance: "))
#     interest_rate = float(input("Enter the interest rate for the CD: "))
#     months = int(input("Enter the length of the CD in months: "))
    
#     updated_balance, interest_earned = create_cd_account(balance, interest_rate, months)
    
#     print(f"Updated CD account balance: {updated_balance}")
#     print(f"Interest earned: {interest_earned}")