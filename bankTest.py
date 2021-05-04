import random
import validation
Database = {}

def init():
  print("welcome to BANKPHB")
  
  have_account = int(input("Do you have account with us: 1 (yes) 2 (no)ln"))
  
  if(have_account==1):
        login()
  
  elif(have_account==2):
          register()
          
  else:
      print("you have selected invalid option")
      init()
      login()
        
  
def login():
  print("xxxxxx login xxxxxx")
  
  account_number_from_user = input("what is your account number?ln")
  
  is_valid_account_number = validation.account_number_validation(account_number_from_user)
  
  if is_valid_account_number:
    
    password = (input("what is your password?ln"))
    
    for account_number, user_details in databse.items():
      if account_number == int(account_number_from_user):
        if user_details[3] == password:
          bank_operation(user_details)
          print("invalid option or password")
          log()
    else:
        print("you have selected invalid option")
        init()
              
def register():
  print("xxxxxx register xxxxx")
  
  email = input("what is your email address?ln")
  
  first_name = input("what is your first nameln")
  
  last_name = input("what is your last nameln")
  
  password = input("create a passwordln")
  
  account_number = generation_account_number()
  database[account_number]=[first_name, last_name, email, password]
  
  print("your account has been created")
  print("=============================")
  print("your account number is: %d" % account_number)
  print("make sure you keep it safe")
  print("==============================")
  
  login()
    
#else:
  print("something went wrong, please try again")
  register()
        
        
def bank_operation(user):
    print("welcome%s %s" % (user[0], user[1]))

    selected_option = int(input("what would you like to do?(1) deposit (2) withdrawal (3) logout (4) exit ln"))
    
    if selected_option == 1:
        deposit_opertaion()
        
    elif selected_option == 2:
        withdrawal()
        
    elif selected_option == 3:
        logout()
        
    elif selected_option == 4:
        exit()
    
    else:
     print("invalid option selected")
     bank_operation(user)

def withdrawal_operation():
  
  withdrawal_amount = float(input("enter amount to withdrawln"))
  print("take your cashln")

def deposit_operation():

                deposit_amount = float("enter amount to depositln")
                print("deposit successfulln")

def generation_account_number():

    return random.randrange(111111111, 999999999)

def get_current_balance(user_details):
    return user_details[4]    
    
def logout():
    login() 
    