#!/usr/bin/python3
import os
import requests
import argparse
import datetime

from dotenv import load_dotenv

load_dotenv()


## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def returncreds():
    """Returns query parameter key-value pair containing credentials"""
    nasa_api_key = os.getenv('NASA_API_KEY')
    return f"api_key={nasa_api_key}" 

def get_args():
    """Setup required args and verify they were passed in"""
    # Set up required args
    parser = argparse.ArgumentParser(description="Pass in start date")
    parser.add_argument('--start-date',
            metavar='STARTDATE',
            type=str,
            help='Pass in a date in YYYY-MM-DD format'
    )
    parser.add_argument('--end-date',
            metavar='ENDDATE',
            type=str,
            help='Pass in a date in YYYY-MM-DD format (OPTIONAL)'
    )

    # Verify the args were passed in
    args = parser.parse_args()
    if not args.start_date:
        parser.print_help()
        exit(1)
    return args


# this is our main function
def main():
    """runtime"""

    # Get script command-line arguments.
    args = get_args()
    startdate = "start_date=" + args.start_date.strip() # datetime.datetime.fromisoformat(args.start_date.strip())

    ## Obtain credential query string.
    nasacreds = returncreds()

    # Build request URL
    request_url = NEOURL + startdate + "&" + nasacreds
    if args.end_date:
        request_url += f"&end_date={args.end_date}"
    
    # make a request with the request library
    neowrequest = requests.get(request_url)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)

if __name__ == "__main__":
    main()

