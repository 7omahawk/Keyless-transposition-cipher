
import sys

def encryption(userInput):

    userInput = userInput.replace(" ", "")
    sizeOfInput = len(userInput)
    firstRow = ""
    secondRow = ""

    for i in range(sizeOfInput):

        if i % 2 == 0:
            firstRow = firstRow + userInput[i]
        else: 
            secondRow = secondRow + userInput[i]

    cipher = firstRow + secondRow

    print(f"The encrypted text is: {cipher}")

def decryption(userInput):
    hello = "will be update here"




while(True):
    print("Enter your choice(Number): ")
    print("1. Encryption: ")
    print("2. Decryption: ")
    print("3. Exit: ")

    number = int(input("Enter the number: "))

    def choice(number):
        if number == 1:
            userInput = input("Enter your text to encrypt: ")
            userInput = userInput.lower()
            encryption(userInput)
        elif number == 2:
            userInput = input("Enter your text to decrypt: ")
            userInput = userInput.lower()
            decryption(userInput)
        elif number == 3:
            sys.exit()
        else:
            print("Input should be a number from 1 to 3")

    choice(number) 