import requests
import os


ascii = r"""

  
 ________  _______   ________  ___       ________  ________  ________  _________  ________  ________     
|\   ____\|\  ___ \ |\   __  \|\  \     |\   __  \|\   ____\|\   __  \|\___   ___\\   __  \|\   __  \    
\ \  \___|\ \   __/|\ \  \|\  \ \  \    \ \  \|\  \ \  \___|\ \  \|\  \|___ \  \_\ \  \|\  \ \  \|\  \   
 \ \  \  __\ \  \_|/_\ \  \\\  \ \  \    \ \  \\\  \ \  \    \ \   __  \   \ \  \ \ \  \\\  \ \   _  _\  
  \ \  \|\  \ \  \_|\ \ \  \\\  \ \  \____\ \  \\\  \ \  \____\ \  \ \  \   \ \  \ \ \  \\\  \ \  \\  \| 
   \ \_______\ \_______\ \_______\ \_______\ \_______\ \_______\ \__\ \__\   \ \__\ \ \_______\ \__\\ _\ 
    \|_______|\|_______|\|_______|\|_______|\|_______|\|_______|\|__|\|__|    \|__|  \|_______|\|__|\|__|
                                                                                                         
                                                                                                         
                                                                                                         


"""
print(ascii)

def main():
    os.system("color a")
    os.system("title Geolocator")
    ip = input("Enter IP to geolocate: ")
    url = f"https://ipinfo.io/{ip}/json"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        print(f"\n[+] IP Address: {data.get('ip', 'N/A')}")
        print(f"[+] Hostname: {data.get('hostname', 'N/A')}")
        print(f"[+] City: {data.get('city', 'N/A')}")
        print(f"[+] Region: {data.get('region', 'N/A')}")
        print(f"[+] Country: {data.get('country', 'N/A')}")
        print(f"[+] Location: {data.get('loc', 'N/A')}")
        print(f"[+] Org: {data.get('org', 'N/A')}")
        print(f"[+] Timezone: {data.get('timezone', 'N/A')}\n")
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    while True:
        main()
