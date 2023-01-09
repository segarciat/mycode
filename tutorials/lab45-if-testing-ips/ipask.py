#!/usr/bin/env python3
"""Author: Sergio Garcia"""

def main():
    """Confirms if the IP provided by the user is valid"""
    ipchk = input("Provide an IP address: ").split(".")
    if len(ipchk) == 4 and all(s.isnumeric() and 0 <= int(s) <= 255 for s in ipchk):
        print("Valid IP address")
    else:
        print("Invalid IP address")

if __name__ == '__main__':
    main()
