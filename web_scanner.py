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
    icann = webbrowser.open('https://lookup.icann.org/')
    return f'Opening Icaan Domain Name Registration Data Lookup analysis tool {icann}\n'

def url_malware():
    paloalto = webbrowser.open('https://urlfiltering.paloaltonetworks.com/')
    return f'Opening Palo Alto Malware analysis tool {paloalto}\n'


def malware_analysis():
    mxtoolbox = webbrowser.open('https://mxtoolbox.com/blacklists.aspx')
    return f'Opening MXtool Malware analysis blacklist tool {mxtoolbox}\n'


def malware_analysis_1():
    zscaler = webbrowser.open('https://zulu.zscaler.com/')
    return f'Opening ZScaler URL Risk Analyzer tool {zscaler}\n'

def zvelo_analysis():
    zvelo = webbrowser.open('https://tools.zvelo.com/')
    return f'Opening Zvelo analysis tool {zvelo}\n'

def sucuri_site_analysis():
    sucuri = webbrowser.open('https://sitecheck.sucuri.net/?cjevent=9da4528d9de911ea80f603500a240611&cj_aid=13948096&cj_pid=8092889&cj_cid=4761150')
    return f'Opening Sucuri site analysis tool {sucuri}\n'

def upguard_analysis():
    upguard = webbrowser.open('https://webscan.upguard.com/')
    return f'Opening Upguard analysis tool {upguard}\n'

def siteguarding_analysis():
    siteguarding = webbrowser.open('https://www.siteguarding.com/en')
    return f'Opening Siteguarding analysis tool {siteguarding}\n'

print(malware_analysis())

print(malware_analysis_1())
    
print(url_malware())

print(open_webbrowser())

print(zvelo_analysis())

print(sucuri_site_analysis())

print(upguard_analysis())

print(siteguarding_analysis())

# ip_address = get("https://api.ipify.org/?format=json").json()['ip']
# print(ip_address)

# def my_public_ip():
#     ip = get('https://api.ipify.org').text
#     return f'Resolving my public ip address: {ip}\n'

# print(my_public_ip())`