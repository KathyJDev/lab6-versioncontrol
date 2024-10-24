# Kathryn Jerez
def encode(password):
    result = ""
    for i in range(len(password)):
        result += str((int(password[i]) + 3) % 10)
    return result

def decode(password):
    for i in range(9):
        password = encode(password)
    return password

if __name__ == "__main__":
    password = ""
    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = int(input("\nPlease enter an option: "))

        if option == 1:
            password = input("Please enter a password to encode: ")
            try:
                password = encode(password)
            except:
                print(f"Your password failed to encode.")
            else:
                print("Your password has been encoded and stored!")
        elif option == 2:
            print("The encoded password is " +password + ", and the original password is " + decode(password) + ".")
        elif option == 3:
            break
