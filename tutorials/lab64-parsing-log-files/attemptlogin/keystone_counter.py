#!/usr/bin/python3

LOG_FILENAME = "/home/student/mycode/attemptlogin/keystone.common.wsgi"
FAIL_PATTERN = "- - - - -] Authorization failed" 
SUCCESS_PATTERN = "-] Authorization failed"

def main():
    # parse keystone.common.wsgi and return number of failed login attempts
    fail_login = 0 # counter for fails
    success_login = 0
    # open the file for reading
    with open(LOG_FILENAME, 'r') as keystone_file:
        # loop over the list of lines
        for line in keystone_file:
            # if this 'fail pattern' appears in the line...
            if FAIL_PATTERN in line:
                fail_login += 1 # this is the same as loginfail = loginfail + 1
                print(f"Fail login: {line.split(' ')[-1]}")
            elif SUCCESS_PATTERN in line:
                success_login += 1

        print("The number of failed log in attempts is", fail_login)
        print("The number of successful log in attempts is", success_login) 

if __name__ == '__main__':
    main()
