#!/usr/bin/env python3

import requests
import json
import pprint
from datetime import datetime

IP_URL = "http://ip.jsontest.com/"
VALIDATE_JSON_URL = "http://validate.jsontest.com/"
SERVERS_FILE = "myservers.txt"

def main():
    """Create a JSON string and validate it thorugh a POST request."""
    my_json = {}
    
    # Part A: Current timestamp.
    my_json["time"] = datetime.now().timestamp()

    # Part B: IP of our system.    
    response = requests.get(IP_URL)
    data = response.json()
    my_json.update(data)
    
    # Part C: List of servers from a file
    with open(SERVERS_FILE, "r", encoding="utf8") as f:
        my_json["mysvrs"] = [line.strip() for line in f]

    # Part E: Validate JSON
    response = requests.post(VALIDATE_JSON_URL, {"json": json.dumps(my_json)})
    data = response.json()
    pprint.pprint(data)

if __name__ == '__main__':
    main()
