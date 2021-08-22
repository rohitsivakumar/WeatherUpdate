import requests
import argparse


def check_internet(url="https://8.8.8.8"):
    internet_status = False
    timeout = 5
    if "https:" not in url:
        url = "https://" + url
    try:
        request = requests.get(url, timeout=timeout)
        print("Connected to the Internet")
        internet_status = True
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("No internet connection.")
        internet_status = False

    return internet_status


arg_descriptor = "Pass the URL to check internet connection.\n"
arg_descriptor += "You can provide your custom site to ping as:\n ./check_internet.py -o \"www.google.com\""

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
    print("\nPinging %s" % site_to_ping)
    check_internet(site_to_ping)
