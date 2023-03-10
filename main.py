MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please Enter a number")
            
    return amount

def get_number_of_lines():
    while True:
        lines = input("How many lines would you like to play (1-" + str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 1  <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number")
        else:
            print("Please Enter a number")
            
    return lines

def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)
    
    
main()