#!/usr/bin/env python3

import requests
LOOKUPS = 51

def main():
    for i in range(LOOKUPS):
        requests.get("http://0.0.0.0:2224/fast")

if __name__ == '__main__':
    main()
