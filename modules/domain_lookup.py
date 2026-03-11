import whois

def lookup_domain(domain):

    print("\n🌐 Domain Information")

    try:
        w = whois.whois(domain)

        print("Domain:", domain)
        print("Registrar:", w.registrar)
        print("Creation date:", w.creation_date)
        print("Expiration date:", w.expiration_date)

    except:
        print("Erro ao consultar domínio")
