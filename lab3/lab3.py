import os
user = {0: ["root", "root", "admin"]}
countUsers = len(user)
standardPassword = "qwerty1"
fileBd = "bde.txt"

def rewriteBd():
    f = open(fileBd, 'w')
    for i in range(countUsers):
        f.write(str(i) + " " + user[i][0] + " " + user[i][1] + " " + user[i][2] + "\n")
    f.close()

def initBd():
    global countUsers
    OpenFile = True
    try:
        f = open(fileBd, 'r')
    except FileNotFoundError:
        OpenFile = False
    if OpenFile:
        for line in f:
            length = len(line)
            data = []
            j = 0
            temp = ""
            for i in range(length):
                if (line[i] != ' ') and (line[i] != '\n'):
                    temp += line[i]
                else:
                    data.insert(j, temp)
                    temp = ""
                    j += 1
            user[int(data[0])] = [data[1], data[2], data[3]]
        countUsers = len(user)
        f.close()
    else:
        rewriteBd()
    return

def cls():
    os.system('CLS')

def register(role = False):
    cls()
    print("Sign Up")
    check = True
    default = "user"
    global countUsers

    while check:
        login = input("Create a username: ")
        check = False
        for i in range(countUsers):
            if login == user[i][0]:
                print("Login already in use!")
                check = True
                break

    password = input("Create a password: ")
    if role:
        print("Roles")
        print("1. Admin")
        print("2. User")
        Choice = int(input("Select role: "))
        if Choice == 1:
            default = "admin"
        else:
            default = "user"

    user[countUsers] = [login, password, default]
    countUsers = len(user)
    rewriteBd()
    print("User registered successfully!")
    os.system('pause')
    return

def displayUsers():
    cls()
    print("ID\t\tLogin\t\tPassword\t\tRole")
    for i in range(countUsers):
        print(str(i)+"\t\t"+user[i][0]+"\t\t"+user[i][1]+"\t\t\t"+user[i][2])
    os.system('pause')
    return

def changeLogin(id):
    cls()
    print("Change Login")
    check = True
    while check:
        login = input("Create a username: ")
        check = False
        for i in range(countUsers):
            if login == user[i][0]:
                print("Login already in use!")
                check = True
                break
    user[id][0] = login
    print("Username successfully changed!")
    rewriteBd()
    os.system('pause')
    return

def changePassword(id):
    cls()
    print("Change Password")
    user[id][1] = input("Create a password: ")
    print("Password successfully changed!")
    rewriteBd()
    os.system('pause')
    return

def resetPassword():
    cls()
    print("Reset Password")
    id = int(input("Enter id users: "))
    if (id >= countUsers) and (id < 0):
        print("There is no such id in the database!")
    else:
        user[id][1] = standardPassword
        print("User password reset!")
        rewriteBd()
    os.system('pause')
    return

def changeRole():
    cls()
    print("Change role users")
    id = int(input("Enter id users: "))
    if (id >= countUsers) and (id < 0):
        print("There is no such id in the database!")
    else:
        print("Roles")
        print("1. Admin")
        print("2. User")
        Choice = int(input("Select role: "))
        default = "user"
        if Choice == 1:
            default = "admin"
        user[id][2] = default
        print(user[id][0] + " now became an " + user[id][2])
        rewriteBd()
        os.system('pause')
    return

def Apanel(id):
    work = True
    MyId = id
    while work:
        cls()
        if user[MyId][2] == "user":
            print("You were demoted!")
            os.system('pause')
            return
        print("You are logged in as Admin!("+user[MyId][0]+")")
        print("1. Create user")
        print("2. Change login")
        print("3. Change password")
        print("4. Reset password user")
        print("5. List users")
        print("6. Change role user")
        print("7. Log out")
        print("8. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            register(True)
        elif choice == 2:
            changeLogin(MyId)
        elif choice == 3:
            changePassword(MyId)
        elif choice == 4:
            resetPassword()
        elif choice == 5:
            displayUsers()
        elif choice == 6:
            changeRole()
        elif choice == 7:
            work = False
        elif choice == 8:
            exit(0)

def Upanel(id):
    work = True
    MyId = id
    while work:
        cls()
        print("You are logged in as User!(" + user[MyId][0] + ")")
        print("1. Change login")
        print("2. Change password")
        print("3. Log out")
        print("4. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            changeLogin(MyId)
        elif choice == 2:
            changePassword(MyId)
        elif choice == 3:
            work = False
        elif choice == 4:
            exit(0)

def signIn():
    cls()
    print("Sign In")
    login = input("Enter username: ")
    password = input("Enter password: ")
    for i in range(countUsers):
        if (login == user[i][0]) and (password == user[i][1]):
            print("You have successfully logged in!")
            if user[i][2] == "admin":
                Apanel(i)
            else:
                Upanel(i)
            return
    print("Login or password is incorrect!")
    os.system('pause')
    return

def main():
    initBd()
    work = True

    while work:
        cls()
        print("Main menu: ")
        print("1. Sign In")
        print("2. Sign Up")
        print("3. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            signIn()
        elif choice == 2:
            register()
        elif choice == 3:
            work = False
        else:
            print("Not Found!")
            os.system('pause')
    return

main()