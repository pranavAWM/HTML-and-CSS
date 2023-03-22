import random

# Define a dictionary of honeywords
#honeywords = {'honey1', 'honey2', 'honey3'}

uname = input("Enter the name : ")
pass1 = input("Enter the password : ")

#pass1 = input("Enter the password ")

# opening the file in read mode
my_file = open(r"C:\Users\pk285\OneDrive\Desktop\testfol ", "r",encoding='cp437')

# reading the file
data = my_file.read()

honeywords = data.split("\n")
print(honeywords)

r = random.randint(0,len(honeywords))


honeywords.insert(r,pass1)
print(honeywords[r])

# Define a function to check if a password is a honeyword
def check_password(password):
    if password in honeywords:
        # Log the access attempt and trigger an alert
        print('Unauthorized access detected!')
        return False
    else:
        return True

# Example usage: authenticate user with username and password
def authenticate(username, password):
    # Check if the password is a honeyword
    if not check_password(password):
        return False
    else:
        # Authenticate the user with the real password
        # (replace this with your actual authentication logic)
        if password == 'correctpassword':
            return True
        else:
            return False


out = authenticate(uname,pass1)

print(out)




# opening the file in read mode





# replacing end splitting the text
# when newline ('\n') is seen.

print("\nThe number is ",r)

my_file.close()

