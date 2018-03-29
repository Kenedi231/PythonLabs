import random
import itertools

def createCode():
    result = ""
    ch = str(round(random.uniform(0, 9)))
    work = True
    while(work):
        if ch in result:
            ch = str(round(random.uniform(0, 9)))
        else:
            result += ch
        if len(result) >= 4:
            work = False
    return result

def Check(data):
    for i in range(len(data)):
        j = i + 1
        while (j < len(data)):
            if (data[i] == data[j]) :
                return False
            j += 1
    return True

def CheckBulls(secret, data):
    result = 0
    for i in range(len(secret)):
        if secret[i] == data[i]:
            result += 1
    return result

def CheckCows(secret, data):
    result = 0
    for i in range(len(secret)):
        j = 0
        while(j < len(secret)):
            if (data[i] == secret[j] and i != j):
                result += 1
            j += 1
    return result

def userPlay(secret):
    countTry = 0
    countBulls = 0
    countCows = 0
    work = True
    while work:
        while (True):
            inData = input("Enter the 4 character code: ")
            res = len(inData)
            if (res == 4) and Check(inData):
                countTry += 1
                break
            else:
                print("Incorrect!")
        print(inData)
        countBulls = CheckBulls(secret, inData)
        countCows = CheckCows(secret, inData)
        print(str(countBulls) + " bulls and " + str(countCows) + " cows!")
        if (countBulls == 4):
            print("You guessed the number with " + str(countTry) + " attempt!")
            work = False

def computerPlay(secret):
    print(secret)
    prevValue = {}
    code = "0123"
    work = True
    result = ""
    last = " "
    count = 4
    Attempt = 0
    number = False
    while work:
        countBulls = CheckBulls(secret, code)
        countCows = CheckCows(secret, code)
        prevValue[Attempt] = [code, countBulls, countCows]
        if Attempt != 0:
            if countBulls > prevValue[Attempt-1][1]:
                last = code[-1]
                count -= 1
            elif countBulls < prevValue[Attempt-1][1]:
                last = prevValue[Attempt-1][0][-1]
            if (countCows > prevValue[Attempt-1][2] or (countCows >= prevValue[Attempt-1][2] and code[-1] in secret)) and code[-1] != last:
                if prevValue[Attempt-1][0][-1] in secret:
                    if prevValue[Attempt-1][0][-1] not in result:
                        result += prevValue[Attempt-1][0][-1]
                if code[-1] not in result:
                    result += code[-1]
            elif countCows <= prevValue[Attempt-1][2] and prevValue[Attempt-1][0][-1] != last and prevValue[Attempt-1][0][-1] in secret:
                if countCows <= prevValue[Attempt-1][2] and not number:
                    number = True
                    count -= 1
                if prevValue[Attempt-1][0][-1] not in result:
                    result += prevValue[Attempt-1][0][-1]
        Attempt += 1
        value = int(code[-1]) + 1
        if value < 10:
            code = code[:3] + str(value)
        print("Computer entered " + str(code))
        print(str(countBulls) + " bulls and " + str(countCows) + " cows!")
        if len(result) == count or value >= 10:
            work = False
    if last == " ":
        for i in range(len(code) - 1):
            code = code[-1] + code[:3]
            countBulls = CheckBulls(secret, code)
            countCows = CheckCows(secret, code)
            prevValue[Attempt] = [code, countBulls, countCows]
            print("Computer entered " + str(code))
            print(str(countBulls) + " bulls and " + str(countCows) + " cows!")
            if Attempt != 0:
                if countBulls > prevValue[Attempt - 1][1]:
                    last = code[-1]
                    count -= 1
                    break
                elif countBulls < prevValue[Attempt - 1][1]:
                    last = prevValue[Attempt - 1][0][-1]
            Attempt += 1
    if len(result) != 3:
        while len(result) != 3:
            result = ' ' + result
        for i in range(len(code) - 1):
            sum = countCows + countBulls
            if result[1] != ' ':
                result = code[i] + result[1] + result[2] + last
            else:
                result = result[0] + code[i] + result[2] + last
            countBulls = CheckBulls(secret, result)
            countCows = CheckCows(secret, result)
            print("Computer entered " + str(result))
            Attempt += 1
            print(str(countBulls) + " bulls and " + str(countCows) + " cows!")
            if countCows + countBulls > sum and code[i] in secret:
                result = code[i] + result[1] + result[2] + last
            elif result[0] == ' ':
                result = result[0] + result[0] + result[2] + last
            if countBulls + countCows == 4:
                break
    else:
        result = result + last
    temp = list(itertools.permutations(result[:-1], 3))
    for i in range(len(temp)):
        if (countBulls == 4):
            print("The computer won with " + str(Attempt) + " attempt!")
            break
        result = ''.join(temp[i]) + result[-1]
        countBulls = CheckBulls(secret, result)
        countCows = CheckCows(secret, result)
        print("Computer entered " + str(result))
        Attempt += 1
        print(str(countBulls) + " bulls and " + str(countCows) + " cows!")


def main():
    secret = createCode()
    print("The number is enumerated ????")
    print("1 - Solve by yourself")
    print("2 - Get the computer to guess the number")
    choice = input('Enter your choice: ')
    if choice == '1':
        userPlay(secret)
    elif choice == '2':
        computerPlay(secret)
    else:
        print("If you do not want that yet!")
main()