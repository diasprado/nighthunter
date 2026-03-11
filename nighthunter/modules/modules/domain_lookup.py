import whois
import dns.resolver

def domain_lookup():

    domain = input("Digite o domínio: ")

    print("\nWHOIS")

    try:

        w = whois.whois(domain)

        print("Registrar:", w.registrar)
        print("Criação:", w.creation_date)
        print("Expiração:", w.expiration_date)

    except:

        print("Erro no WHOIS")

    print("\nDNS")

    try:

        result = dns.resolver.resolve(domain, "A")

        for ip in result:
            print("IP:", ip)

    except:

        print("Erro ao resolver DNS")
