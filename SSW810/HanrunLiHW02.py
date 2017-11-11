class Fraction:
    '''
     Implement a fraction calculator that asks the user for 
     two fractions and an operator and then prints the result.
    '''

    def __init__(self, numerator, denominator):
        try:
            a = int(numerator)
            b = int(denominator)
            if denominator == 0:
                raise ValueError("Denominator cannot be zero!")
        except ValueError as e:
            print("invalid input:", e)
            return

        # get the gcd as x
        (x, y) = (a, b)
        while y != 0:
            (x, y) = (y, x % y)

        self.numerator = int(a / x)
        self.denominator = int(b / x)

    def plus(self, other):
        newNumerator = self.numerator * other.denominator + \
            other.numerator * self.denominator
        newDenominator = self.denominator * other.denominator
        return Fraction(newNumerator, newDenominator)

    def minus(self, other):
        newNumerator = self.numerator * other.denominator - \
            other.numerator * self.denominator
        newDenominator = self.denominator * other.denominator
        return Fraction(newNumerator, newDenominator)

    def times(self, other):
        newNumerator = self.numerator * other.numerator
        newDenominator = self.denominator * other.denominator
        return Fraction(newNumerator, newDenominator)

    def divide(self, other):
        newNumerator = self.numerator * other.denominator
        newDenominator = self.denominator * other.numerator
        return Fraction(newNumerator, newDenominator)

    def equal(self, other):
        if self.numerator * other.denominator == self.denominator * other.numerator:
            return True
        else:
            return False

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)


def main():
    # f1 = Fraction(2, 4)
    # f2 = Fraction(7, 5)
    # f3 = Fraction(-1, -2)
    # print(f1)
    # print(f2)
    # print(f1.plus(f2))
    # print(f1.minus(f2))
    # print(f1.times(f2))
    # print(f1.divide(f2))
    # print(f1.equal(f2))
    # print(f1.equal(f3))

    print("Welcome to the fraction calculator!")

    f1n = input("Fraction 1 numerator: ")
    try:
        val = int(f1n)
    except ValueError as e:
        print("invalid input:", e)
        return
    f1d = input("Fraction 1 denominator: ")
    try:
        val = int(f1d)
        if val == 0:
            raise ValueError("Denominator cannot be zero!")
    except ValueError as e:
        print("invalid input:", e)
        return
    f1 = Fraction(f1n, f1d)

    # Operation (+, -, *, /):
    ope = input("Operation (+, -, *, /): ")
    try:
        if ope == "+" or ope == "-" or ope == "*" or ope == "/":
            pass
        else:
            raise ValueError("invalide operation")
    except ValueError as e:
        print("invalid input:", e)
        return

    f2n = input("Fraction 2 numerator: ")
    try:
        val = int(f2n)
    except ValueError as e:
        print("invalid input:", e)
        return
    f2d = input("Fraction 2 denominator: ")
    try:
        val = int(f2d)
        if val == 0:
            raise ValueError("Denominator cannot be zero!")
    except ValueError as e:
        print("invalid input:", e)
        return
    f2 = Fraction(f2n, f2d)

    # final result
    if ope == "+":
        print(f1, ope, f2, "=", end=" ")
        print(f1.plus(f2))
    elif ope == "-":
        print(f1, ope, f2, "=", end=" ")
        print(f1.minus(f2))
    elif ope == "*":
        print(f1, ope, f2, "=", end=" ")
        print(f1.times(f2))
    elif ope == "/":
        print("(" + str(f1) + ")", ope, "(" + str(f2) + ")", "=", end=" ")
        print(f1.divide(f2))
    return


if __name__ == "__main__":
    main()
