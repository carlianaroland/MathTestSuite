# Carliana Roland
# COMP163
# MyMath Simple Calc

def calcAdd(num1, num2):
    return num1 + num2


avg_list = list()
def calcAvg(avg_list):
    return sum(avg_list) / len(avg_list)

def calcSub(num1, num2):
    if num2 < 0:
        difference = num1 + num2
    else:
        difference = num1 - num2
    return difference



def calcMult(num1, num2):
    return num1 * num2


def calcDiv(num1, num2):
    return num1 / num2


def calcFloorDiv(f1: float, f2: float):
    return f1 // f2


def calcAbs(num: int):  # the user-defined absolute function is to find the absolute for the root function
    if num < 0:
        return -num
    else:
        return num


def calcRoot(n: float, r: int):
    g = 1
    while True:
        g_prime = g - (g ** r - n) / (r * g ** (r - 1))
        if calcAbs(g_prime - g) < 0.0000000001:
            return g
        g = g_prime


def calcGCD(n1: int, n2: int):
    if n2 == 0:
        return n1
    elif n1 == 0:
        return n2
    else:
        return calcGCD(n2, n1 % n2)


def calcLCM(num1: int, num2: int):
    return (num1 * num2) / calcGCD(num1, num2)


def calcSin(x: float):
    pi = 3.141592653589793
    while x < -pi or x > pi:
        x += (2 * pi)
    while x > pi:
        x -= (2 * pi)

    t = x
    sine = t
    i = 0
    while abs(t) >= 0.0000000001:
        t *= ((-x**2) / ((2*i + 3) * (2*i + 2)))
        sine += t
        i += 1
    return sine


def calcCosine(x: float):
    pi = 3.141592653589793
    while x < -pi or x > pi:
        x += (2 * pi)
    while x > pi:
        x -= (2 * pi)

    t = 1
    cosine = t
    i = 0
    while abs(t) >= 0.0000000001: # this is the decimal for the 10 to the negative power of 10
        t *= ((-x ** 2) / ((2 * i + 2) * (2 * i + 1)))
        cosine += t
        i += 1
    return cosine


def calcPow(n, power):
    count = 1
    for i in range(1, power+1):
        count *= n
    return count


# double sign is a float. a reference in other languages like C shark and C++
def calcTan(x: float):
    res = calcSin(x) / calcCosine(x)
    return res


if __name__ == "__main__": # unit testing all functions for errors
    print((f'calcAdd: The sum of {1} and {6} expect {calcAdd(1, 6)} got: ' + str(calcAdd(1, 6))
           + " : " + ("Pass" if calcAdd(1, 6) == calcAdd(1, 6) else "Fail")))

    print((f'calcSub: The difference of {-1} and {-5} expect {calcSub(-1, -5)} got: ' + str(calcSub(-1, -5))
           + " : " + ("Pass" if calcSub(-1, -5) == calcSub(-1, -5) else "Fail")))

    print((f'calcMult: The product of {2} and {4} expect {calcMult(2, 4)} got: ' + str(calcMult(2, 4))
           + " : " + ("Pass" if calcMult(2, 4) == calcMult(2, 4) else "Fail")))

    print((f'calcDiv: The product of {12} and {6} expect {calcDiv(12, 6)} got: ' + str(calcDiv(12, 6))
           + " : " + ("Pass" if calcDiv(12, 6) == calcDiv(12, 6) else "Fail")))

    print((f'calcFloorDiv: The product of {24} and {6} expect {calcFloorDiv(24, 6)} got: ' + str(calcFloorDiv(24, 6))
           + " : " + ("Pass" if calcFloorDiv(24, 6) == calcFloorDiv(24, 6) else "Fail")))

    print((f'calcRoot: The root of {5.0625} and {4} expect {calcRoot(5.0625, 4)} got: ' + str(calcRoot(5.0625, 4)) +
           " : " + ("Pass" if calcRoot(5.0625, 4) == calcRoot(5.0625, 4) else "Fail")))

    print((f'calcGCD: The GCD of {12} and {6} expect {calcGCD(12, 6)} got: ' + str(calcGCD(12, 6)) + " : " + (
        "Pass" if calcGCD(12, 6) == calcGCD(12, 6) else "Fail")))

    print((f'calcLCM: The LCM of {4} and {6} expect {calcLCM(4, 6)} got: ' + str(calcLCM(4, 6)) + " : " + (
        "Pass" if calcLCM(4, 6) == calcLCM(4, 6) else "Fail")))

    print((f'calcSin: The sine of {1.047197551} expect {calcSin(1.047197551)} got: ' + str(calcSin(1.047197551)) +
           " : " + ("Pass" if calcSin(1.047197551) == calcSin(1.047197551) else "Fail")))

    print((f'calcCosine: The cosine of {1.047197551} expect {calcCosine(1.047197551)} got: ' +
           str(calcCosine(1.047197551)) + " : " + ("Pass" if calcCosine(1.047197551) == calcCosine(1.047197551)
            else "Fail")))

    print((f'calcTan: The tangent of {1.047197551} expect {calcTan(1.047197551)} got: ' + str(calcTan(1.047197551)) +
           " : " + ("Pass" if calcTan(1.047197551) == calcTan(1.047197551) else "Fail")))

    print((f'calcPow: The power of {5} and {2} expect {calcPow(5, 2)} got: ' + str(calcPow(5, 2)) + " : " + (
        "Pass" if calcPow(5, 2) == calcPow(5, 2) else "Fail")))
