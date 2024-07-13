import parser as parser


def read_file_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        return ["File not found."]


def input_from_terminal():
    while True:
        try:
            s = input('LISP > ')
        except KeyboardInterrupt:
            break
        if not s: continue
        result = parser.parse(s)

        print(f"Postfix: {result}")


def menu():
    while True:
        print("\nMenu:")
        print("1. Read from file")
        print("2. Read from terminal")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            file_path = 'DATA/lisp.txt'
            lines = read_file_lines(file_path)
            for line in lines:
                result = parser.parse(line)
                print(f"Postfix: {result}")
            break
        elif choice == '2':
            input_from_terminal()
        elif choice == '3':
            print("Exiting")
            break
        else:
            print("Invalid option. Try again.")


menu()
