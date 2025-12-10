def hello():
    print("Hello and welcome to the client! Please select what you want to do:\n"
    "1. Search for flower\n"
    "2. Add new flower\n"
    "3. Remove flower")

hello()

def main():
    choose = input("What do you want to do?...")

    if choose == "1":
        flower = input("What flower do you want to search for?...")

        if flower == "Ros":
            print("En ros finns inte i databanken")

main()