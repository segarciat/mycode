#!/usr/bin/env python3

def main():
    proto = ["ssh", "http", "https"]
    protoa = ["ssh", "http", "https"]
    print(proto)
    proto.append("dns") # this line will add "dns" at the end of our list
    protoa.append("dns") # this line will add "dns" at the end of our list
    print(proto)
    proto2 = [22, 80, 443, 53] # a list of common ports
    proto.extend(proto2) # pass proto2 as an argument to the extend
    print(proto)
    protoa.append(proto2) # pass proto2 as an argument to the append method
    

    # Current contents of list
    print(protoa)
    # Remove and print last element until list is empty.
    while len(protoa):
        print(protoa.pop())
    print(protoa)

    # One line approach
    print(proto)
    proto.clear()
    print(proto)
    

if __name__ == '__main__':
    main()
