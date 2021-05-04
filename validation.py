def account_number_validation(account_number):
  if account_number:
    
    if len(str(account_number)) == 10:

        try:
            int(account_number)
            return True
        except ValueError:
            print("invalid account number, account number should be integer")
            return False

        else:
            print("account number cannot be more or less than 10 digits")
            return False
    else:
            print("account number is a required field")
            return False