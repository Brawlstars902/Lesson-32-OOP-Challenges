class Roman_Numerals:
    def __init__(self,number):
        self.number=number
        
    def conversion(self):

        Conversion_Scale= [(1000, 'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]

        result = ""
        num=self.number
        for value, symbol in Conversion_Scale:
            while num >= value:
                result += symbol
                num -= value

        return(result)
    

try:
    user_input=int(input('Enter an Integer to convert into Roman Numerals: '))
    convertor=Roman_Numerals(user_input)
    print('The Roman Numeral for {} is: {}'.format(user_input,convertor.conversion()))

except(ValueError):
    print('\nError! Please enter a Valid Integer!')