import math
def translate_to_roman(number: int) -> str:
    if number == 4:
        return "IV"
    if number == 9:
        return "IX"
    
    roman = ""

    number_of_l = number // 50
    roman += number_of_l * "L"
    remainder = number - (number_of_l * 50)

    if remainder == 40:
        roman += "XL"
        return roman

    number_of_x = number // 10
    roman += number_of_x * "X"
    remainder = number - (number_of_x * 10)

    if remainder == 9:
        roman += "IX"
        return roman

    number_of_v = (remainder) // 5
    roman += number_of_v * "V"
    remainder = remainder - (number_of_v * 5)

    if remainder == 4:
        roman += "IV"
        return roman

    number_of_i = remainder
    roman += number_of_i * "I"

    return roman

    # if remainder == 4:
    #     number_of_i = 0
    #     left = "IV"
    # else:
    #     number_of_i = remainder
    #     left = ""

    # return "X" * number_of_x + left + "V" * number_of_v + "I" * number_of_i