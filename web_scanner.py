import os
from requests import get
import webbrowser
import socket


# def get_nmap(options, url):
#     command = "nmap " + options + " " + url
#     process = os.popen(command)
#     results = str(process.read())
#     return results

print("\nScanning website now........... please wait this may take a few minutes\n")
#print(f'Getting nmap results.......\n {get_nmap("-T4 -A -v", "207.241.224.2")}')

# my_socket = socket.gethostbyname_ex('google.com')
# print(my_socket)

def open_webbrowser():
    browser = webbrowser.open('https://lookup.icann.org/')
    return browser

def url_malware():
    browser = webbrowser.open('https://urlfiltering.paloaltonetworks.com/')
    return browser

print(f'Opening Malware analysis database {url_malware()}\n')

def malware_analysis():
    malware_database = webbrowser.open('https://mxtoolbox.com/blacklists.aspx')
    return malware_database
    
print(f'Opening Malware analysis database {malware_analysis()}\n')

def malware_analysis_1():
    malware_domain = webbrowser.open('https://zulu.zscaler.com/')
    return malware_domain
    
print(f'Opening Malware analysis web brwoser {malware_analysis_1()}\n')

print(f'Opening web brwoser {open_webbrowser()}\n')

# ip_address = get("https://api.ipify.org/?format=json").json()['ip']
# print(ip_address)

def my_public_ip():
    ip = get('https://api.ipify.org').text
    return f'Resolving my public ip address: {ip}\n'

print(my_public_ip())

    
    
    
    
    
