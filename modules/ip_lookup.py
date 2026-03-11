import requests
import ipaddress

def lookup_ip(ip):
    print("\n IP Information\n")

    ip = ip.strip()

    try:
        ip_obj = ipaddress.ip_address(ip)
    except ValueError:
        print(" IP inválido\n")
        return

    if ip_obj.is_private:
        print(f"IP: {ip}")
        print("⚠ Este é um IP PRIVADO usado apenas na rede local.")
        print("Não é possível obter geolocalização.\n")
        return

    try:
        url = f"http://ip-api.com/json/{ip}"
        r = requests.get(url, timeout=10)
        data = r.json()

        if data["status"] != "success":
            print(" Não foi possível obter informações do IP\n")
            return

        print(f"IP: {ip}")
        print(f" País: {data.get('country')}")
        print(f" Cidade: {data.get('city')}")
        print(f" ISP: {data.get('isp')}")
        print(f" Organização: {data.get('org')}")
        print(f" Timezone: {data.get('timezone')}")
        print(f" Latitude: {data.get('lat')}")
        print(f" Longitude: {data.get('lon')}")

        if data.get("proxy"):
            print(" Proxy/VPN: Detectado")
        else:
            print(" Proxy/VPN: Não detectado")

        print()

    except Exception as e:
        print(" Erro ao consultar o IP\n")
        print(e)
