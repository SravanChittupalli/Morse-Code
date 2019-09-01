MORSE_CODE_DICT = { 'A':'.-',   'B':'-...', 
                    'C':'-.-.', 'D':'-..',  'E':'.', 
                    'F':'..-.', 'G':'--.',  'H':'....', 
                    'I':'..',   'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--',   'N':'-.', 
                    'O':'---',  'P':'.--.', 'Q':'--.-', 
                    'R':'.-.',  'S':'...',  'T':'-', 
                    'U':'..-',  'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----','2':'..---','3':'...--', 
                    '4':'....-','5':'.....','6':'-....', 
                    '7':'--...','8':'---..','9':'----.', 
                    '0':'-----',', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..','/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-' } 
decodedword = ''


def encode(string , encodedword):
    if (string == ' '):
        encodedword = encodedword + '  '
    else:
        encoded = MORSE_CODE_DICT[string]
        encodedword = encodedword + encoded + ' '
    return encodedword

def decode(encodedword):
    for key , value in MORSE_CODE_DICT.items():
        if(value == encodedword):
            return (str(decodedword) + str(key))
    
    
if __name__ == '__main__':
    message = input("Enter The Sentence To Be Converted To Morse Code : ")
    encodedword = ''
    for i in message :
        encodedword = encode(i , encodedword)
    print(encodedword)
    

    encodedmess = input("Enter The Encoded Message To Be Decoded : ")
    encodedwords = encodedmess.split('  ')
    
    for i in encodedwords:
        encodedletters = i.split(' ')
        for j in encodedletters:
            decodedword = decode(j)
        decodedword = str(decodedword) + ' '
    print(decodedword)
