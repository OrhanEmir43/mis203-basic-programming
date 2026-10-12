# Week 4 Lab: Savings Goal Planner

`lab04_savings_planner.py` asks for a starting balance, monthly deposit,
monthly interest rate (%) and a savings goal, then simulates the savings
month by month (interest first, then the deposit) for at most 60 months.

Run it with:

    python lab04_savings_planner.py

## Testing

**Test I ran:** starting balance `1000`, deposit `500`, rate `1`, goal `3000`.
The program reached the goal in 4 months with a final balance of `3070.80`
and total interest of `70.80`, which matches the expected result. I also ran
the boundary case (balance `0`, deposit `1000`, rate `0`, goal `3000`, which
reached the goal in exactly 3 months), the 60-month limit case, and negative
or zero inputs to check that the program asks again.

**What I changed after testing:** when the starting balance already met the
goal, the summary said "Goal reached in 0 months.", which read oddly. I
changed it to "Goal reached: no deposits were needed."
