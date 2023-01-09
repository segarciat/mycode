#!/usr/bin/env python3

def main():
    # create the string hostname
    hostname = input("What value should we set for hostname? ")

    # Code to execute if user-provided input is mtg
    if hostname.lower() == "mtg":
        print("The hostname was found to be mtg")
        print("hostname matches expected config")

    # Display message regardless of user-provided hostname
    print("Exiting the script.")

if __name__ == '__main__':
    main()
