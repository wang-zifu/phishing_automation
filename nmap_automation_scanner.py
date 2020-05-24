import os
#from tld import get_tld
from requests import get

def get_nmap(options, url):
    command = "nmap " + options + " " + url
    process = os.popen(command)
    results = str(process.read())
    return results 

# def get_domain_name(url):
#     domain_name = get_tld(url)
#     return domain_name

# print(get_domain_name('https://www.website.com'))


def get_ip_address(url):
    command = "tracert " + url
    process = os.popen(command)
    results = str(process.read())
    # marker = results.find("has address") + 12
    # return results[marker:].splitlines()[0]
    return results



def main():
    
    print("\nScanning website now....... please wait this may take a few minutes\n")
    print(get_nmap("-T4 -A -v", "ip address goes here"))
    print(get_ip_address("website.com"))
    
if __name__ == "__main__":
    main()

# ip = get('https://api.ipify.org').text
# print(f'My public IP address is: {ip}')


