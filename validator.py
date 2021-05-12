def accountNumberValidator(accountNumber):
    if accountNumber: # This checks if an account number was entered and not left blank during login(), goes to Else at bottom if blank
        try:
            int(accountNumber) #turns to integer and goes to except if non-integer detected

            if len(str(accountNumber)) == 10:
                
                return True
            else:
                print('Account number MUST be 10 digits long')
                return False
            
        except ValueError:
            print("Invalid data, please enter only numbers")
            return False
        except TypeError:
            print("Invalid data type, please try again")
            return False
    else:
        print('Account number not found, please try again')
        return False

        
