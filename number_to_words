decimal_digit = ('', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
tens_digit = ('', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')
# Handle numbers between 11-19 in order to avoid pronounciation of "ten one", "ten two", "ten three", ...
irregular_numbers = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

with open('NumToWord copy\\number_names.txt', 'r', encoding='utf-8') as textfile:
    number_names = textfile.readlines()

# Pronounciation of single digit number
def decimal_pronounciation(number):
    return decimal_digit[number]

# Pronounciation of double digit number
def tens_digit_pronounciation(number):
    last_digit = number % 10
    first_digit = number // 10

    if number in irregular_numbers:
        return irregular_numbers[number]
    else:
        if last_digit == 0:
            return tens_digit[first_digit]
        else:
            return f"{tens_digit[first_digit]}{decimal_pronounciation(last_digit)}"

# Pronounciation of three digit number
def hundred_pronounciation(number):
    first_digit = number // 100
    last_digits = number % 100

    return f"{decimal_pronounciation(first_digit)}hundred{tens_digit_pronounciation(last_digits)}"
    
def pronounciation(number):
    if 1 <= number <= 9:
        return decimal_pronounciation(number)
    elif 10 <= number <= 99:
        return tens_digit_pronounciation(number)
    elif 100 <= number <= 999:
        return hundred_pronounciation(number)

user_input = int(input('Please type a number: '))
# Separates the input number with a thousands separator
user_input_seperator = f"{user_input:,}"
# Splits the number into each individual number
user_input_seperator_list = user_input_seperator.split(',')
# Reverses the lists, so each iteration of the loop corresponds its number name in order
user_input_seperator_list.reverse()

for number in reversed(range(len(user_input_seperator_list))):
    individual_number = pronounciation(int(user_input_seperator_list[number]))
    # Avoids pronounciation of individual number that contains only zeros
    if individual_number is None:
        continue
    print(f"{individual_number} {number_names[number][:-1].lower()}", end=' ')
