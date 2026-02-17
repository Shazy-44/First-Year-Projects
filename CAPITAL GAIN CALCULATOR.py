print("\Student Name: SHAZRINA KITUTU, Student no: 403151162")

from collections import deque
def calculate_capital_gain(transactions):
    buy_queue = deque()
    total_gain = 0

    for day, transactions in enumerate(transactions, start=1):
        action, shares, price = transactions

        if action == "BUY":
            buy_queue.append({"shares": shares,
                              "price": price,
                              "day": day
                              })
        elif action == "SELL":
            shares_to_sell = shares

            while shares_to_sell > 0:
                if not buy_queue:
                    raise ValueError("Error: Attempted to sell more shares than available.")

                oldest_buy = buy_queue[0]
                available_shares = oldest_buy["shares"]

                sold_shares = min(shares_to_sell, available_shares)

                gain = sold_shares * (price - oldest_buy["price"])
                total_gain += gain

                if oldest_buy["shares"] == 0:
                    buy_queue.popleft()
            return total_gain

def main():
    print("\DAR CAPITAL GAIN CALCULATOR")

    transactions = []

    n = int(input("Enter the number of transactions: "))

    print('\Enter transaction in the format:')
    print("BUY shares price OR SELL shares price")
    print('\Example: BUY 100 20')

    for i in range(n):
        entry = input(f'Transaction {i + 1}: ').strip().split()

        action = entry[0].upper()
        shares = int(entry[1])
        price = int(entry[2])

        if action not in ["BUY", "SELL"]:
            print("\Invalid action.")
            return

        transactions.append((action, shares, price))

    try:
        total_gain = calculate_capital_gain(transactions)
        print("\Total Capital GAIN/LOSS is $", total_gain)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

