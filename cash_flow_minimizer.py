# -----------------------------
# INPUT
# -----------------------------
transactions = [
    ("A", "B", 50),
    ("B", "C", 20),
    ("C", "A", 10),
    ("A", "D", 30),
    ("D", "B", 10)
]

# -----------------------------
# BALANCE CALCULATION
# -----------------------------
def calculate_balances(transactions):
    balances = {}
    for payer, receiver, amount in transactions:
        balances[payer] = balances.get(payer, 0) - amount
        balances[receiver] = balances.get(receiver, 0) + amount
    return balances


# -----------------------------
# ALGORITHM 1 (Slow O(n^2))
# -----------------------------
def slow_minimize_cash_flow(balances):
    balances = balances.copy()
    result = []

    while True:
        max_creditor = max(balances, key=balances.get)
        max_debtor = min(balances, key=balances.get)

        if balances[max_creditor] == 0 and balances[max_debtor] == 0:
            break

        amount = min(balances[max_creditor], -balances[max_debtor])

        balances[max_creditor] -= amount
        balances[max_debtor] += amount

        result.append((max_debtor, max_creditor, amount))

    return result


# -----------------------------
# ALGORITHM 2 (Fast O(n log n))
# -----------------------------
import heapq

def fast_minimize_cash_flow(balances):
    balances = balances.copy()
    result = []

    creditors = []
    debtors = []

    # Build heaps
    for person, balance in balances.items():
        if balance > 0:
            heapq.heappush(creditors, (-balance, person))  # max heap
        elif balance < 0:
            heapq.heappush(debtors, (balance, person))     # min heap

    while creditors and debtors:
        credit, creditor = heapq.heappop(creditors)
        debt, debtor = heapq.heappop(debtors)

        credit = -credit

        amount = min(credit, -debt)

        result.append((debtor, creditor, amount))

        credit -= amount
        debt += amount

        if credit > 0:
            heapq.heappush(creditors, (-credit, creditor))
        if debt < 0:
            heapq.heappush(debtors, (debt, debtor))

    return result


# -----------------------------
# RUN BOTH
# -----------------------------
balances = calculate_balances(transactions)

print("Net Balances:", balances)

print("\n--- Slow Algorithm Output ---")
slow_result = slow_minimize_cash_flow(balances)
for t in slow_result:
    print(t[0], "pays", t[1], "$" + str(t[2]))

print("\n--- Fast Algorithm Output ---")
fast_result = fast_minimize_cash_flow(balances)
for t in fast_result:
    print(t[0], "pays", t[1], "$" + str(t[2]))


import random
import time

def generate_transactions(num_people, num_transactions):
    people = ["P" + str(i) for i in range(num_people)]
    transactions = []

    for _ in range(num_transactions):
        payer = random.choice(people)
        receiver = random.choice(people)

        while receiver == payer:
            receiver = random.choice(people)

        amount = random.randint(1, 100)
        transactions.append((payer, receiver, amount))

    return transactions


def measure_runtime(algorithm_function, balances, runs=3):
    total_time = 0

    for _ in range(runs):
        start = time.perf_counter()
        algorithm_function(balances)
        end = time.perf_counter()

        total_time += (end - start)

    average_time = total_time / runs
    return average_time * 1000   # milliseconds


input_sizes = [100, 500, 1000, 5000, 10000]

print("Input Size | Slow Algorithm (ms) | Fast Algorithm (ms)")
print("----------------------------------------------------")

for size in input_sizes:
    test_transactions = generate_transactions(num_people=size, num_transactions=size * 2)
    test_balances = calculate_balances(test_transactions)

    slow_time = measure_runtime(slow_minimize_cash_flow, test_balances)
    fast_time = measure_runtime(fast_minimize_cash_flow, test_balances)

    print(size, "|", round(slow_time, 4), "|", round(fast_time, 4))
