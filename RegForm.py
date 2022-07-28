UpperCase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LowerCase="abcdefghijklmnopqrstuvwxyz"
specialchar="$@_#*-/+^%&!<:;>{\}[.,?]"
digits="0123456789"

def register():
    db = open("database.txt", "r")
    Username = input("Enter Username(Email) : ")
    Password = input("Create Password : ")
    CPassword = input("Confirm Password : ")
    d = []
    f = []
    for i in db:
        a, b = i.split(",")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d,f))
        
    if not len(Username or Password)<1:
            
        if Username in d:
            print("Username Exists, restart!!!")
            register()
        else: 
            if any(un in Username[0] for un in specialchar) or any(un in Username[0] for un in digits):
                print("Username cannot start with Special Characters or Digits, restart!!!!")
                register()
            elif not any(un in '@' for un in Username) or not any(un in '.' for un in Username):
                print("Username must contain '@' & '.', restart!!!!")
                register()
         
            elif Password != CPassword:
                print("Passwords don't match, restart!!!")
                register()

            elif len(Password)<=5 or len(Password)>=16 : 
                print("Password should be between 5 to 16 character, restart!!!!")
                register()

            elif not any(uc in UpperCase for uc in Password) or not any(lc in LowerCase for lc in Password) or not any(di in digits for di in Password) or not any(sp in specialchar for sp in Password):
                print("Password must have minimum one UpperCase Character, one LowerCase Character, one Digit, one Special Character, restart!!!!")
                register()
            else:
                db = open("database.txt","a")
                db.write(Username+","+Password+"\n")
                print("Success!!!")
                exit()
    else:
        print("Username and Password cannot be empty, restart!!!!")
        register()    

def logIn():
    db = open("database.txt","r")
    Username = input("Enter your username : ")
    Password = input("Enter your password : ")

    if not len(Username or Password)<1:
        d = []
        f = []
        for i in db:
            a, b = i.split(",")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d,f))
        
        if (Username in data):
            if Password == data[Username]:
                print("Login success")
                print("Hi,",Username)
            else:
                print("Password incorrect")
                choice = input("Forget Password | Try Again | New Password : ")
                if choice == "Forget Password" or choice == "forget password":
                    Username = input("Enter your username : ")
                    print("Here is your Password : "+data[Username])
                elif choice == "Try Again" or choice == "try again":
                    logIn()
                elif choice == "new password" or choice == "New Password":
                    newPassWord()
        else:
            print("Username dosen't exist")
            logIn()
    else:
        print("Please enter a value")
        logIn()

def newPassWord():
    
    db = open("database.txt","r")
    Username = input("Enter your username : ")
    if not len(Username)<1:
        d = []
        f = []
        for i in db:
            a, b = i.split(",")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d,f))
    OPassword = data[Username]
    NPassword = input("Enter New Password : ")
    CPassword = input("Confrim Password : ")

    if NPassword != CPassword:
        print("Passwords don't match, restart!!!")
        newPassWord()

    elif len(NPassword)<=5 or len(NPassword)>=16 :
        print("Password should be between 5 to 16 character, restart!!!!")
        newPassWord()

    elif not any(uc in UpperCase for uc in NPassword) or not any(lc in LowerCase for lc in NPassword) or not any(di in digits for di in NPassword) or not any(sp in specialchar for sp in NPassword):
        print("Password must have minimum one UpperCase Character, one LowerCase Character, one Digit, one Special Character, restart!!!!")
        newPassWord()
    with open("database.txt","r") as file:
        data = file.read()
        data = data.replace(OPassword,NPassword)
    with open("database.txt","w") as file:
        file.write(data)
        print("Password changed successfully")
    file.close()
    logIn()

def form(option=None):
    option = input("Login | Signup : ")
    if option == "Login" or option == "login" :
        logIn()
    elif option == "Signup" or option == "signup" :
        register()
    else:
        print("Please enter an option")
        form()
form()


