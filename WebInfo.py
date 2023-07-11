import socket
import requests
import ssl
import re
import whois
from bs4 import BeautifulSoup
from cryptography import x509
from cryptography.hazmat.backends import default_backend

def get_domain_info(url):
    domain = re.search(r"(?<=://)([^/]+)", url).group(0)    # Extract domain from URL
    ip_address = socket.gethostbyname(domain)   # Retrieve IP address of the domain
    domain_info = whois.whois(domain)   # Get WHOIS information from the domain

    # Retrieve emails associated with the domain from WHOIS data
    emails = set()
    if 'emails' in domain_info and domain_info['emails'] is not None:
        emails.update(domain_info['emails'])
    
    try:
        # Make an HTTP request to the website
        response = requests.get(url)
        response.raise_for_status()     # Raises exception if request was not successful
    except requests.exceptions.HTTPError as e:
        print(f"\nHTTPError: {e}")    # Handle the error condition
    
    # Extract page title
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string.strip() if soup.title else 'N/A'
    
    # Extract meta tags
    meta_tags = []
    for tag in soup.find_all('meta'):
        if 'name' in tag.attrs and 'content' in tag.attrs:
            meta_tags.append({'name': tag.attrs['name'], 'content': tag.attrs['content']})
    
    # Extract links on the page
    links = []
    for link in soup.find_all('a'):
        if 'href' in link.attrs:
            links.append(link.attrs['href'])

    # Obtain SSL certificate information
    cert = ssl.get_server_certificate((domain, 443))
    # Decode the certificate
    cert_decoded = x509.load_pem_x509_certificate(cert.encode(), default_backend())

    
    
    # Print the collected information
    print("\n-----------------------------------------------------------")
    print('\033[1m' + "Title: " + '\033[0m' + title)
    print('\033[1m' + "Domain: " + '\033[0m' + domain)
    if domain_info.registrar is not None:
        print('\033[1m' + "Domain Registrar: " + '\033[0m' + domain_info.registrar)
    else:
        print('\033[1m' + "Domain Registrar: " + '\033[0m' + 'No Info')

    if domain_info.status is not None:
        if len(domain_info.status[0]) == 1:
            print('\033[1m' + "Domain Status: " + '\033[0m' + domain_info.status)
        else:
            print('\033[1m' + "Domain Status: " + '\033[0m' + domain_info.status[0])
    else:
        print('\033[1m' + "Domain Status: " + '\033[0m' + 'No Info')
    print('\033[1m' + "IP Addresses: " + '\033[0m' + ip_address)
    if len(emails) == 0:
        print('\033[1m' + "Emails: " + '\033[0m' + 'No Info')
    else:
        print('\033[1m' + "Emails: " + '\033[0m' + ', '.join(emails))
    print('\033[1m' + "Meta Tags: " + '\033[0m')
    for tag in meta_tags:
        print(f"\tName: {tag['name']}")
        print(f"\tContent: {tag['content']}")
    print('\033[1m' + "Links: " + '\033[0m')
    for link in links:
        print(f'\t{link}')
    
    print('\033[1m' + "SSL Certificate: " + '\033[0m')
    print(f"\tIssuer: {cert_decoded.issuer}")
    print(f"\tSubject: {cert_decoded.subject}")
    print(f"\tValid From: {cert_decoded.not_valid_before}")
    print(f"\tValid Until: {cert_decoded.not_valid_after}")
    print("-----------------------------------------------------------\n")


# --------------------------------------- MAIN ---------------------------------------
def main():
    url = input("Enter the website URL: ")
    get_domain_info(str(url))

if __name__ == '__main__':
    main()
