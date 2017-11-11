def fahrenheit2celsius(f):
    if not (isinstance(f, float) or isinstance(f, int)):
        return "Please input a number"
    if f < (-459.67):
        return "Less than absolute zero"
    return float(f - 32) * 5 / 9


def f2c_6train(f):
    if not (isinstance(f, float) or isinstance(f, int)):
        return -9999
    if (f == 86):
        return 30
    if (f == 77):
        return 25
    if (f == 68):
        return 20
    if (f == 59):
        return 15
    if (f == 50):
        return 10
    if (f == 41):
        return 5
    if (f == 32):
        return 0
    if (f == 23):
        return -5
    if (f == 14):
        return -10
    return -9999


def f2c(f):
    if f2c_6train(f) == (-9999):
        return fahrenheit2celsius(f)
    else:
        return f2c_6train(f)


def main():
    print("Test cases:");
    print(f2c(52))
    print(f2c(51))
    print(f2c(50))
    print(f2c(-100.15))
    print(f2c(77))
    print(f2c(9))
    print(f2c(0))
    print(f2c(-10000))
    print(f2c("123"))
    print(f2c("abc"))
    print("\n")
    f = input("Please input a valid fahrenheit degree to convert to celsius:");
    try:
        val = int(f)
    except ValueError:
        try:
            val = float(f)
        except ValueError:
            print("invalid input")
            return
    print(f2c(val))
    return


if __name__ == "__main__":
    main()
