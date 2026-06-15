year=int(input("Enter your year of birth:"))
birthday=int(input("press 1 if your birthday has passed else press 0:"))
age=2026-year
if birthday==1:
    print(f"You are {age} year old.")
else:
    print(f"You are {age-1} year old.")
