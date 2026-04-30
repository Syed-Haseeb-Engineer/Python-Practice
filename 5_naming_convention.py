MAX_LOGIN_ATTEMPTS = 3 # CONSTANT

#Class name in PascalCase Style
class UserProfile:
    pass #do nothing now

#Funtion: name in snake_case
def authenticate_user(username, password):

    #Variables: snake_case
    login_successful = False
    attempts_made = 1

    if attempts_made <=MAX_LOGIN_ATTEMPTS:
        print(f"Attempting to log in {username}...")
        login_successful = True

    return login_successful

is_logge_in = authenticate_user("ubuntu_admin", "super_secret_password")
print(f"Login success: {is_logge_in}")