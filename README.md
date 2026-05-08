# Cash Flow Minimizer System

## Project Description
This project is a Cash Flow Minimizer system for CSCI 377. The program reduces the number of transactions needed to settle debts among a group of people. It calculates each person's net balance and then creates a simpler payment plan.

## Team Member
Mahbubur Rahman

## Programming Language
Python

## Dependencies
This program uses Python built-in libraries only:
- heapq
- time
- random

No external installations are required.

## How to Run the Program
1. Download or clone this repository.
2. Open the file `cash_flow_minimizer.py`.
3. Run the file using Python:

```bash
python cash_flow_minimizer.py

Sample Input
transactions = [
    ("A", "B", 50),
    ("B", "C", 20),
    ("C", "A", 10),
    ("A", "D", 30),
    ("D", "B", 10)
]
Sample Output
Net Balances: {'A': -70, 'B': 40, 'C': 10, 'D': 20}

--- Slow Algorithm Output ---
A pays B $40
A pays D $20
A pays C $10

--- Fast Algorithm Output ---
A pays B $40
A pays D $20
A pays C $10

Algorithms Implemented
This project implements two algorithms:
Slow Greedy Algorithm
Repeatedly scans all balances to find the maximum debtor and maximum creditor.
Time complexity: O(n²)
Fast Heap-Based Algorithm
Uses heaps/priority queues to find the maximum debtor and creditor more efficiently.
Time complexity: O(n log n)
Report
The final project report is included in the repository.
AI Usage Disclosure
ChatGPT was used for brainstorming, understanding algorithms, organizing the report, and clarifying pseudocode. All code and explanations were reviewed, tested, and edited before submission.

