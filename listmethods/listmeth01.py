#!/usr/bin/env python3

def main():

    proto = ["ssh", "http", "https"]
    print(proto)
    print (proto[1]) # Display second element: "http"
    proto.extend("dns") # this line will add "d", "n", and "s"
    print(proto)

if __name__ == '__main__':
    main()
