import requests

def lookup_ip(ip):

    try:
        url = f"http://ip-api.com/json/{ip}"
        r = requests.get(url).json()

        print("\n🌍 IP Information")
        print("IP:", ip)
        print("Country:", r.get("country"))
        print("Region:", r.get("regionName"))
        print("City:", r.get("city"))
        print("ISP:", r.get("isp"))
        print("Org:", r.get("org"))

    except:
        print("Erro ao buscar IP")
