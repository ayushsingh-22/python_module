
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).


# age = int(input("Enter your age = "))

# if age < 13:
#     print("You are child.")
# elif age < 20:
#     print("You are teenager.")
# elif age < 60:
#     print("You are adult.")
# else:
#     print("You are senior citizen.")

# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

# age = int(input("Enter your age = "))
# day = input("Enter day = ")

# price = 12 if age >= 18 else 8

# if day == "wednesday":
#     price = price - 2

# print("Price of ticket is ₹",price)

# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

year = int(input("Enter year = "))

# if year%4 == 0:
#     if year%100 != 0:
#         print(year,"is leap year.")
#     else:
#         print(year,"is not leap year.")

# elif year%400 == 0:
#     print(year,"is leap year.")

# else:
#     print(year,"is not leap year.")


    # other approch

if (year%4 == 0 and year%100 != 0) or (year%400==0):
    print(year,"is leap year.")
else:
    print(year,"is not leap year.")
    



