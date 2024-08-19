import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {"A": 3, "B": 4, "C": 6, "D": 8}
symbol_value = {"A": 6, "B": 5, "C": 4, "D": 3}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for (
        symbol,
        symbol_count,
    ) in symbols.items():  # Dictonary, .items() give key + values associated with key
        for _ in range(
            symbol_count
        ):  # _ gives anonymus variable, when we dont care about the iteration value
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # Making copy using [:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(
            columns
        ):  # enumerate returns i and the value for that i in the variable
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount needs to be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? "
        )
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Lines needs to be between 1-" + str(MAX_LINES) + ".")
        else:
            print("Please enter a number.")
    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount. Your current balance is {balance}"
            )
        else:
            break
    print(
        f"Your are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}"
    )

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balane is ${balance}")
        if balance == 0:
            print(f"You Lost, Thank you for playing")
            break
        answer = input("Press enter to play (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You are left with ${balance}")


main()
