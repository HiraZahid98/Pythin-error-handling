try:
    print(1/2)
    print(2/2)
    print(3/2)
    print(4/2)
    print(1/0)
except ZeroDivisionError:
    print("This is zero division except error")

except ZeroDivisionError as err:
    print()