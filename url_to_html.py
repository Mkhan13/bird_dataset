"""
This script accepts a website URL as a command-line argument, fetches the HTML content of the page, 
and saves it to an html file.
"""

import requests
import sys
from urllib.parse import urlparse

# Check that the URL is provided as a command line argument
if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1] #Get the URL from the command line input

#Parse the URL to get the domain name
parsed_url = urlparse(url)
domain_name = parsed_url.netloc

if not domain_name:
    print("Invalid URL. Please provide a valid website URL.")
    sys.exit(1)

#Remove 'www' if present and strip the TLD (.com, .org, etc.)
domain_parts = domain_name.split('.')
if domain_parts[0] == 'www':
    domain_parts.pop(0)  #Remove 'www'
domain = domain_parts[0]  #Get the domain name only

response = requests.get(url) #Send a GET request to the website

if response.status_code == 200: #Check if the request was successful

    html_content = response.text #Get the HTML content
    file_name = f"{domain}.html" #Create the filename using the domain name
    
    with open(file_name, 'w', encoding='utf-8') as file: #Write the HTML content to the file
        file.write(html_content)
    print(f"HTML content has been saved to '{file_name}'")
else:
    print(f"Failed to retrieve the website. Status code: {response.status_code}")