"""
    Description: This program checks for presence/absence of internet connection based on
                 site address passed as cmdline arguments
    Author: Rohit Sivakumar
    Date: 22-AUG-2021
"""
import requests
import argparse


def check_internet(url="https://8.8.8.8"):
    timeout = 5
    if "https:" not in url:
        url = "https://" + url
    try:
        requests.get(url, timeout=timeout)
        print("Connected to the Internet")
    except (requests.ConnectionError, requests.Timeout) as err:
        print("Could not reach the site. Either no internet connection or check site exists.\n\n [%s]" % err)


arg_descriptor = "Pass the URL to check internet connection.\n"
arg_descriptor += "You can provide your custom site to ping as:\n python check_internet.py -s \"www.google.com\""

# Initialize the parser
parser = argparse.ArgumentParser(description=arg_descriptor)

# Add custom arguments
parser.add_argument("-s", "--site", dest="site_to_ping")

# Read arguments from command line
args = parser.parse_args()
site_to_ping = args.site_to_ping

if site_to_ping is None:
    print(arg_descriptor)
    print("\nDefaulting to use :  www.google.com")
    check_internet("www.google.com")
else:
    print("\nChecking using %s" % site_to_ping)
    check_internet(site_to_ping)
