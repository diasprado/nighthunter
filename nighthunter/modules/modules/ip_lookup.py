import requests

def ip_lookup():

    ip = input("Digite o IP: ")

    try:

        r = requests.get(f"https://ipinfo.io/{ip}/json", timeout=10)

        data = r.json()

        print("\nInformações do IP")

        print("IP:", data.get("ip"))
        print("Cidade:", data.get("city"))
        print("Região:", data.get("region"))
        print("País:", data.get("country"))
        print("Localização:", data.get("loc"))
        print("Organização:", data.get("org"))

    except:

        print("Erro ao consultar IP")

