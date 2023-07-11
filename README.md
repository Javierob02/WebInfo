# Description
WebInfo is a script that by inputting a website link as a parameter, will give information based on the website.
The information that this tool obtains are:
- Title
- Domain
- Domain Registrar
- Domain Status
- IP Address
- Emails
- Meta Tags
- Links
- SSL Certificate

# Steps
The script performs the following steps:
1. Extracts the domain from the given URL.
2. Retrieves the IP address of the domain using the socket module.
3. Retrieves WHOIS information about the domain using the whois module.
4. Retrieves emails associated with the domain from the WHOIS data.
5. Makes an HTTP request to the website and retrieves the content.
6. Parses the HTML content using Beautiful Soup and extracts the title, meta tags, and links on the page.
7. Obtains and decodes the SSL certificate information using the ssl and cryptography modules.
8. Prints the collected information, including the title, domain, domain registrar, domain status, IP addresses, emails, meta tags, links, and SSL certificate details.

To use the script, you need to provide a website URL as input. It will then display the collected information about the website

# Libraries
This script makes use of several libraries and modules to perform its task.
The script used are:
* **socket**: Used to retrieve the IP address associated with the domain.
* **requests**: Used to make an HTTP request to the website and retrieve the website's content.
* **ssl**: Used to obtain the SSL certificate information for the website.
* **re**: Used to extract the domain from the given URL.
* **whois**: Used to retrieve WHOIS information about the domain.
* **bs4** (Beautiful Soup): Used to parse and extract data from the HTML content of the website.
* **cryptography**: Used to decode and extract information from the SSL certificate.

# Note
#### Please note that this script only provides basic functionality and may not capture all possible information about a website. It can be further expanded or customized based on specific requirements.
