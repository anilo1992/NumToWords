# NumToWords

Welcome to NumToWords. This Python script converts numeric input into its corresponding English word representation. 

## Explanation

In general, I have written the code according to logic, unfortunately I lack the language to explain the logic. Therefore, I apologise if I cannot explain it properly.

First of all, The first values in the the tuples `decimal_digit` and `tens_digit` are empty in order to avoid pronounciation of zeros since Python is a zero-indexed language.

Since the numbers between 11 and 19 don't match the pattern between 20-99, I created the tuple `irregular_numbers = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}` to compensate this.

Furthermore, the textfile contains a list of the names for individual numbers. Since Python is a zero-indexed language and due to the logic of my code, the last individual number doesn't have a name. For example the number `1,234` is pronounced "one-thousand", followed by the pronounciation of just "twohundredthirtyfour".
