
class IntegerToRoman:
    def __init__(self, number):
        self.number = number
        self.roman_numeral = ""

    def convert(self):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        num = self.number
        roman = ""

        for i in range(len(val)):
            count = num // val[i]
            roman += syms[i] * count
            num -= val[i] * count

        self.roman_numeral = roman
        return roman

    def __str__(self):
        return f"Integer: {self.number}, Roman Numeral: {self.roman_numeral or self.convert()}"
    
number = 1994
converter = IntegerToRoman(number)
roman = converter.convert()
print(roman)              
print(converter)          

