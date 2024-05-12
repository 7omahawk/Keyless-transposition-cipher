# making rail fence cipher aka keyless transposition cipher encryption and decryption using python

import sys
import math

# the encryption function of rail fence cipher
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
    print(f"The encrypted message is: {cipher}")


# the encryption function of rail fence cipher
def decryption(userInput):
    
    userInput = userInput.replace(" ", "")
    sizeOfInput = len(userInput)

    divid = math.ceil(sizeOfInput / 2)
    temp = divid   # the temp variable is use for the number of loop running
    plaintext = ""

    if sizeOfInput % 2 == 0:   # when the length of input size is even this condition will work
        for i in range(temp):
            plaintext = plaintext + userInput[i]
            if i < temp:
                plaintext = plaintext + userInput[divid]
            divid += 1
    else:
        for i in range(temp):  # when the length of input size is odd this condition will work
            plaintext = plaintext + userInput[i]
            if i < temp-1:
                plaintext = plaintext + userInput[divid]
            divid += 1
    
    print(f"The decrypted message is: {plaintext}")


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