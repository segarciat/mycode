#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - strings test true"""

def is_valid_ip(ip):
    ip_list = ip.split(".")
    return len(ip_list) == 4 and all(s.isnumeric() and 0 <= int(s) <= 255 for s in ip_list)

def main():
    ipchk = input("Provide an IP address: ").strip()
    if not is_valid_ip(ipchk):
        print("You did not provide a valid IP address")
    elif ipchk == "192.168.70.1":
        print("Looks like the IP address of the Gateway was " + ipchk + 
                ". This is not recomended")
    else:
        print("Looks like the IP address was set to: " + ipchk)

if __name__ == '__main__':
    main()
