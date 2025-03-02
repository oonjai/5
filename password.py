correct_username = "admin"
correct_password = "Ad13n@23t"

username = input("Username: ")
password = input("Password: ")

if username == correct_username and password == correct_password:
    print("Welcome, admin")
else:
    print("You are not admin")
