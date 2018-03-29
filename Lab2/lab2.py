alphabeth = "abcdefghijklmnopqrstuvwxyz"
lenA = len(alphabeth)

def biasis(sym, bias) :
    i = alphabeth.find(sym)
    if (i != -1) :
        return alphabeth[(i + bias) % lenA]
    else :
        return sym

def Encode() :
    str = input("Enter string: ")
    bias = int(input("Enter bias: "))
    str = str.lower()
    length = len(str)
    result = ""

    for i in range(length) :
        result += biasis(str[i], bias)

    print(result)

def Dencode():
    str = input("Enter string: ")
    str = str.lower()
    length = len(str)
    for i in range(lenA):
        result = ""
        for j in range(length):
            result += biasis(str[j], i)
        print(i, result)

work = True

while work:
    print("Main menu: ")
    print("1: Encode")
    print("2: Dencode")
    print("3: Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        Encode()
    elif choice == 2:
        Dencode()
    else :
        work = False