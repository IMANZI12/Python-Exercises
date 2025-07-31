age = int(input('What is your age: '))
currentweeks = age * 52
remainingWeeks = (90 * 52) - currentweeks
print(f"You May Be remaining with {remainingWeeks} WEEKS to reach 90 YEARS OLD" if remainingWeeks > 0 else
      "You Have already reached 90 YEARS OLD")
