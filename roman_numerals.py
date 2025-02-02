def decimal_to_roman(decimal):
    roman = ''
    #pas = 0
    for value, letter in ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                          (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                          (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')):
        #pas += 1
        while decimal >= value:
            #print (pas, decimal, value, letter)
            decimal -= value
            roman += letter
    return roman

decimal_number = int(input('Enter a decimal number: '))
roman_number = decimal_to_roman(decimal_number)
print(f'Decimal number {decimal_number} is equal to roman number {roman_number}')

