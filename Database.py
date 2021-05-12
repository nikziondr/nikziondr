import os
import validator
import datetime
time = datetime.datetime.now()

data_path = 'C:/Users/Niki/Documents/Programming Projects/Data/user_record/'
auth_path = 'C:/Users/Niki/Documents/Programming Projects/Data/auth_session/'

def create(accountNumber, first_name, last_name, email, password):

    user_data = str(accountNumber) + ',' + first_name + "," + last_name + "," + email + "," + password + "," + str(0)
    if does_account_number_exist(accountNumber): #returns false if acct # already exists
        return False

    if does_email_exist(email): #returns false if email already exists in existing acct
        print('User already exists')
        return False

    completion_state = False

    try:
        f = open(data_path + str(accountNumber) + ".txt", "x")

    except FileExistsError:
        does_file_contain_data = read(data_path + str(accountNumber) + ".txt")
        if not does_file_contain_data:
            delete(accountNumber)
    else:
        f.write(str(user_data))
        completion_state = True
    finally:
        f.close()
        return completion_state

def delete(accountNumber):
    is_delete_successful = False
    if os.path.exists(data_path + str(accountNumber) + ".txt"):
        try:
            os.remove(data_path + str(accountNumber) + ".txt")
            is_delete_successful = True
        except FileNotFoundError:
            print('User not found')
        finally:
            return is_delete_successful

def read(accountNumber):
    is_valid_account_number = validator.accountNumberValidator(accountNumber) #if validator returns true it gets saved here
    try:
        if is_valid_account_number: #if previous line returned true, then it opens the file that matches the acct #, else does the same without the .txt
            f = open(data_path + str(accountNumber) + ".txt", "r")
        else:
            f = open(data_path + str(accountNumber), "r") 
    except FileNotFoundError:
        print('User not found')
    except FileExistsError:
        print("User doesn't exist")
    else:
        return f.readline()
    return False

def does_email_exist(email):
    all_users = os.listdir(data_path)
    for user in all_users: 
        user_list = str.split(read(user), ',')
        if email in user_list:
            return True
        else:
            return False

def does_account_number_exist(accountNumber):
    all_users = os.listdir(data_path) # lists all files in folder 'user_record' and assigns to list
    for user in all_users: # checks to see if inside the all_users list there is a file name that matches the accnt number entered by the user
        if user == str(accountNumber) + ".txt":
            return True
        else:
            return False

def auth_user(accountNumber, password):
    if does_account_number_exist(accountNumber): # goes does_account_number_exist function to see if acct # is already in use
        user = str.split(read(accountNumber), ',') # creates list from auth files and then searches for password inside list
        if password == user[4]:
            return user
    else:
        return False

def account_balance(user):
    f = open(data_path + (user[0]) + ".txt", "w")
    user_str = str(user[0]) + ',' + user[1] + "," + user[2] + "," + user[3] + "," + user[4] + "," + str(user[5])
    try:
        f.write(str(user_str))

    finally:
        f.close()

def login_session_stamp(user):
    try:
        f = open(auth_path + (user[1]) + ".txt", "x")
        f.write('User logged in at ' + str(time))
    except FileExistsError:
        os.remove(auth_path + (user[1]) + ".txt",)
        f = open(auth_path + (user[1]) + ".txt", "x")
        f.write('User logged in at ' + str(time))

def logout_stamp_delete(user):
    os.remove(auth_path + (user[1]) + ".txt",)