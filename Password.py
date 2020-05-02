import re

password = input("Enter Your Password :")
flag = 0
while True:
    if (len(password) < 8):
        print("Password must be more than 8 Characters")
        flag = -1
        break

    elif not re.search("[A-Z]", password):
        print("Password must contain 1 upper Characters")
        flag = -1
        break
    elif not re.search("[0-9]", password):
        print("Password must contain 1 numeric digit")
        flag = -1
        break
    elif not re.search("[_@$#]", password):
        print("Password must contain a special character")
        flag = -1
        break
    elif re.search("\s", password):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        break

if flag == -1:
    print("Not a Valid Password")