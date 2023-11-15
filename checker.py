import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import concurrent.futures

def check_security(ip):
    try:
        requests.get(f'https://{ip}', timeout=3)
        return 'https'
    except:
        return 'http'

def process_ip(ip):
    ip = ip.strip()
    result = ''
    if ip:
        protocol = check_security(ip)
        url = f'{protocol}://{ip}/.svn'
        try:
            session = requests.Session()
            retries = Retry(total=3, backoff_factor=0.1, status_forcelist=[ 500, 502, 503, 504 ])
            session.mount('http://', HTTPAdapter(max_retries=retries))
            session.mount('https://', HTTPAdapter(max_retries=retries))
            response = session.get(url, timeout=3)
            if "Index of /.svn" in response.text:
                result = url
                print(f"URL ajoutée: {url}")
                
        except:
            pass
    return result

def main():
    with open('ip.txt', 'r') as ip_file:
        ip_list = ip_file.readlines()

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        results = list(executor.map(process_ip, ip_list))

    with open('svn.txt', 'w') as svn_file:
        for url in results:
            if url:
                svn_file.write(url + '\n')

if __name__ == "__main__":
    main()
