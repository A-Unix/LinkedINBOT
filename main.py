#!/usr/bin/python3

import os
import subprocess
import time
import requests
from bs4 import BeautifulSoup

try:
    from colorama import init, Fore
except ImportError:
    print(Fore.Red + "Colorama is not installed. Installing it...")
    subprocess.run(["pip", "install", "colorama"], check=True)
    from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# Replace with the target LinkedIn profile URL
linkedin_profile_url = input(Fore.LIGHTMAGENTA_EX + 'Enter the LinkedIn profile url here, e.g., https://www.linkedin.com/in/example-profile: ')

# Send a request to the LinkedIn profile
response = requests.get(linkedin_profile_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the profile page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the email from the profile
    email_element = soup.find('span', {'class': 'email'})
    
    if email_element:
        email = email_element.text.strip()
        print(Fore.LIGHTGREEN_EX + f'Email found: {email}')
    else:
        print(Fore.LIGHTYELLOW_EX + 'Email not found on the profile.')

else:
    print(Fore.LIGHTRED_EX + f'Error: {response.status_code} - {response.text}')
