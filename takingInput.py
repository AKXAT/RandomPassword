def main():
    try:
        character_length = int(input("Enter Character Length "))
        if character_length >= 3:
            pass
        else:
            print("**********OOPS , atleast Input over 3 Expected **********")
            return False
    except:
        print('**********Wrong Input , only Integers accepted**********')
        return False

    while True:
        try:
            mandatory_uppercase = int(input('Enter Mandatory upper case = '))
            mandatory_digits = int(input('Enter Mandatory Digits = '))
            mandatory_symbols = int(input('Enter Mandatory Digits = '))
            if mandatory_uppercase+mandatory_digits+mandatory_symbols <= character_length:
                return character_length,mandatory_uppercase,mandatory_digits,mandatory_symbols
            else:
                print('****OOPS Sum of Mandatory elements are larger than Character*****')
                continue
        except:
            print('**************Something went wrong , Please try again************')
            return False
        
    

if __name__ == '__main__':
    main()
