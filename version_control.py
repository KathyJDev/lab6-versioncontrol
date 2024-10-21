# Kathryn Jerez
def encode(password):
    result = ""
    for i in range(len(password)):
        result += str(int(password[i]) + 3)
    return result

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
                encoded_password = encode(password)
            except:
                print(f"Your password failed to encode.")
            else:
                print("Your password has been encoded and stored!")
        elif option == 2:
            print()
        elif option == 3:
            break