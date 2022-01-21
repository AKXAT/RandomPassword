from scipy import rand
import takingInput
import listofchar
import random



def chooserandomcharacters(mylist):
    MYPASSWORD = ''
    for x in range(mylist[1]):
        MYPASSWORD = MYPASSWORD + random.choice(listofchar.mylistof_strings)
    for y in range(mylist[2]):
        MYPASSWORD = MYPASSWORD + random.choice(listofchar.mylistof_numbers)
    for z in range(mylist[3]):
        MYPASSWORD = MYPASSWORD + random.choice(listofchar.mylistof_symbols)
    if len(MYPASSWORD) == mylist[0]:
        return MYPASSWORD
    else:
        leftchars = mylist[0] - len(MYPASSWORD)
        for a in range(leftchars):
            MYPASSWORD = MYPASSWORD + random.choice(listofchar.mylistof_allchars)
        return MYPASSWORD

        
if __name__ == '__main__':

    try:
        mylist = list(takingInput.main())
        print(chooserandomcharacters(mylist))
    except:
        print("============================BYE BYE========================")