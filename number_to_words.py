digits = {0: "", 1: "eins", 2: "zwei", 3: "drei", 4: "vier", 5: "fünf", 6: "sechs", 7: "sieben", 8: "acht", 9: "neun"}
tens = {0: "", 1: "zehn", 2: "zwanzig", 3: "dreißig", 4: "vierzig", 5: "fünfzig", 6: "sechzig", 7: "siebzig", 8: "achtzig", 9: "neunzig"}
exceptionalNumbers = {11: "elf", 12: "zwölf", 17: "siebzehn"}

with open(r"C:\Users\anilo\Documents\Projekte\NumberToWords\numberNames.txt", 'r', encoding='utf-8') as textFile:
    numberNames = [line.strip() for line in textFile.readlines()]

def twoDigitPronounciation(number):
    firstDigit = number // 10
    lastDigit = number % 10

    if number in digits:
        return digits[number]
    elif number in exceptionalNumbers:
        return exceptionalNumbers[number]
    elif lastDigit == 0:
        return tens[firstDigit]
    return "{}und{}".format(digits[lastDigit], tens[firstDigit])

def hundredPronounciation(number):
    firstDigitOfHundred = number // 100
    lastDigitsOfHundred = number % 100
    lastDigitsOfHundredWrittenOut = twoDigitPronounciation(lastDigitsOfHundred)

    if firstDigitOfHundred == 1:
        return "einhundert{}".format(lastDigitsOfHundredWrittenOut)
    return "{}hundert{}".format(digits[firstDigitOfHundred], lastDigitsOfHundredWrittenOut)
    
def seperateNumbers(number):
    numberFormatted = "{:,}".format(number)
    numberSeperated = numberFormatted.split(",")
    numberSeperatedLength = len(numberSeperated)
    return numberSeperated, numberSeperatedLength

def outwriteNumber(userInput):
    if userInput == 0:
        print("null")
    elif userInput == 1:
        print("eins")
    else:
        individualNumbers = seperateNumbers(userInput)[0]
        index = seperateNumbers(userInput)[1]-1

        for individualNumber in individualNumbers:
            individualNumber = int(individualNumber)
            correspondingNumberName = numberNames[index]

            if individualNumber == 0:
                continue
            elif individualNumber == 1:
                if correspondingNumberName == "Tausend":
                    print("eintausend".format())
                else:
                    print("eine {}".format(correspondingNumberName), end=" ")
            elif 2 <= individualNumber <= 99:
                print("{} {}".format(twoDigitPronounciation(individualNumber), correspondingNumberName), end=" ")
            else:
                print("{} {}".format(hundredPronounciation(individualNumber), correspondingNumberName), end=" ")
            index -= 1

outwriteNumber(123456789)
