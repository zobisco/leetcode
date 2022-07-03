from tkinter import N


def romanToInt(s: str) -> int:
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}
    num = 0
    for i in range(len(s) - 1):
        if i == len(s) - 1:
            num += roman_dict[s[i]]
        elif roman_dict[s[i]] >= roman_dict[s[i+1]]:
            num += roman_dict[s[i]]
        else:
            num -= roman_dict[s[i]]
    return num


print(romanToInt("III"))  # expected 3
print(romanToInt("IV"))  # expected 4
print(romanToInt("IX"))  # expected 9
print(romanToInt("LVIII"))  # expected 58
print(romanToInt("MCMXCIV"))  # expected 1994
print(romanToInt("MCMXCIX"))  # expected 1999


def roman_to_integer(s: str) -> int:
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    special_cases_arr = ['I', 'X', 'C']
    special_cases = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,
    }
    sum_of_numerals = 0
    s_list = list(s)
    if s[-2:] not in special_cases:
        sum_of_numerals += roman_numerals[s[-1]]
    for idx, numeral in enumerate(s_list):
        if idx < len(s_list) - 1:
            if numeral in special_cases_arr:
                special_case = f'{numeral}{s_list[idx+1]}'
                if special_case in special_cases:
                    sum_of_numerals += special_cases[special_case]
                    s_list.pop(idx+1)
                else:
                    sum_of_numerals += roman_numerals[numeral]
            else:
                sum_of_numerals += roman_numerals[numeral]
    return sum_of_numerals


print(roman_to_integer("III") == 3)  # expected 3
print(roman_to_integer("IV") == 4)  # expected 4
print(roman_to_integer("IX") == 9)  # expected 9
print(roman_to_integer("LVIII") == 58)  # expected 58
print(roman_to_integer("DCXXI") == 621)  # expected 621
print(roman_to_integer("MCMXCIV") == 1994)  # expected 1994
print(roman_to_integer("MCMXCIX") == 1999)  # expected 1999
print(roman_to_integer("MMCDXXV") == 2425)  # expected 2425
print(roman_to_integer("MMMCDLXXXVII") == 3487)  # expected 2425
