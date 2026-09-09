correct_username = "admin"
correct_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

username_correct = username == correct_username
password_correct = password == correct_password

if username_correct and password_correct:
    print("Login Successful!")
else:
    print("Login Failed!")