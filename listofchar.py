mylistof_upperstring = [chr(x) for x in range(65,91)]
mylistof_lowerstring = [x.lower() for x in mylistof_upperstring]
mylistof_strings = mylistof_lowerstring+mylistof_upperstring
mylistof_numbers = [chr(x) for x in range(48,58)]
mylistof_symbols = [chr(x) for x in range(33,48)]
mylistof_allchars = mylistof_symbols + mylistof_strings + mylistof_numbers