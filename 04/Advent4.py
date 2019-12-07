def main():
    input = readFile("input.txt")
    differentPassword = []
    print(input)

    for i in range(int(input[0]), int(input[1])):
        ok = digitAlwaysIncrease(str(i)) and atLeastTwoSameDigit(str(i))
        if ok:
            differentPassword.append(i)

    print(differentPassword)
    print(len(differentPassword))

def digitAlwaysIncrease(password):
    ok = 1
    for i in range(0, len(password) - 1):
        if int(password[i]) <= int(password[i+1]):
            ok = ok+1
    return ok == 6
    
def atLeastTwoSameDigit(password):
    ok = False
    for i in range(0, len(password)):
        if password.count(str(password[i])):
            ok = True
    return ok


def readFile(filename):
    return open(filename, "r").read().split("-")

if __name__== "__main__":
    main()