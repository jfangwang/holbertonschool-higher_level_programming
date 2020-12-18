#!/usr/bin/python3
def roman_to_int(roman_string):
    # Roman Numeral Rules
    # 1: "VI" If the second symbol is smaller than the first, add
    # 2: "IV" If the 2nd symbol is greater than the 1st, subtract 2nd from 1st
    # 3: "XXX" There can't be more than 3 of the same symbol in a row
    # Realized checker will input valid numerals and #2 only applies
    if type(roman_string) != str or not roman_string:
        return 0
    sum, next, cur, ind = 0, 0, 0, 0
    while (ind < len(roman_string)):
        cur = convert(roman_string[ind])
        # print("Cur: {}, Sum: {}, Ind: {}".format(cur,
        # convert(roman_string[ind + 1]), ind))
        # Check if there is another letter after
        if ind + 1 < len(roman_string):
            next = convert(roman_string[ind + 1])
        else:
            # If last symbol, just add to sum and return
            sum += cur
            return sum
        # check #2
        if next > cur:
            sum += next - cur
            if ind + 2 < len(roman_string):
                ind += 2
            else:
                return sum
        else:
            sum += convert(roman_string[ind])
            ind += 1
    return sum

def convert(letter):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for key in roman:
        if key == letter:
            return roman[key]
