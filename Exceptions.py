try:
    age = int(input ("Age:"))
    income = 20000
    total = income / age
    print(age)
except ZeroDivisionError:
    print("it cannot be divided with 0")

except ValueError:
    print("invalid value")