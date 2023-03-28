# Determines whether a provided card number is valid according to Luhn's algorithm

# Modules
from cs50 import get_string

def main():
	cardNumber = getUserInput()

	if isValid(cardNumber):
		print(getCardType(cardNumber))
	else:
		print("INVALID")

# Ask for user input and store it as string
def getUserInput():
	while True:
		userInput = get_string("Number: ")
		if userInput.isnumeric():
			break

	return userInput

# Checks if card number is valid according to Luhn's algorithm
def isValid(cardNumber):
	n = len(cardNumber)
	plainSum = productSum = 0

	i = n - 1
	while i > 0:
		firstDigit = int(cardNumber[i])
		secondDigit = int(cardNumber[i - 1])

		p = secondDigit * 2
		plainSum += firstDigit
		productSum += int(p % 10) + int(p / 10 % 10)

		i -= 2

	if (n % 2):
		plainSum += int(cardNumber[0])

	if (productSum + plainSum) % 10 == 0:
		return 1

	return 0

# Determines the type of card based on its number
def getCardType(cardNumber):
	n = len(cardNumber)

	# check if it's American Expresss
	# 15-digit numbers, starts with 34 or 37
	if (n == 15 and (cardNumber[0] == "3" and (cardNumber[1] == "4" or cardNumber[1] == "7"))):
		return "AMEX"

	# check if it's Visa
	# 13 or 16 digit number, starts with 4
	if (cardNumber[0] == "4" and (n == 13 or n == 16)):
		return "VISA"

	# check if it's Mastercard
	# 16 digit number, starts with 51, 52, 53, 54 or 55
	if (n == 16 and cardNumber[0] == "5" and (cardNumber[1] >= "1" and cardNumber[1] <= "5")):
		return "MASTERCARD"

	# if none above
	return "UNKNOWN CARD TYPE"


# Run the program
main()
