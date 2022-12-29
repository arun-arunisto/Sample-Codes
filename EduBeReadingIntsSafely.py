def read_int(prompt, min, max):
    while True:
        try:
            x = int(input(prompt))
            assert (x >= min and x <= max)
            return x
        except ValueError:
            print("wrong Input")
        except AssertionError:
            print(f"Error: the value is not within permitted range ({min}..{max})")

v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
