def menu():
    print("Menu")
    print("-" * 13)
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    

def encode():
    pass


def main():

    while True:
        menu()

        option = int(input('Please enter an option: '))

        if option == 1:
            password = int(input('Please enter your password to encode:'))
            print("Your password has been encoded and stored!")

        elif option == 2:
            print(f"The encoded password is {password}, and the original password is {password}.")

        elif option == 3:
            break


if __name__ == "__main__":
    main()



