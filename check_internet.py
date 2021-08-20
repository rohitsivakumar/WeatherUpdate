import requests


def check_internet(url="https://8.8.8.8"):
    timeout = 5
    if "https:" not in url:
        url = "https://" + url
    try:
        request = requests.get(url, timeout=timeout)
        print("Connected to the Internet")
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("No internet connection.")


check_internet("www.google.com")
