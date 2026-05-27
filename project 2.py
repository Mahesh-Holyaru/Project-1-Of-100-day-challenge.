print("----------     Welcome to the tip calculator!     ---------- \n")
bill = float(input("What was the total bill? $ "))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

Tip_calculation=bill*tip/100               #We have calculated the tip fot total bill
Bill_calculation=bill+Tip_calculation      #here bill is calculated
Bill_distribution=Bill_calculation/people  # divide the bill into people.


print(f"\n Bill For Each {Bill_distribution}")
