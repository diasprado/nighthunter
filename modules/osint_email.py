import re
import dns.resolver

def email_lookup(email):

    print("\n📧 Email Intelligence Report")
    print("-" * 40)

    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if not re.match(regex, email):
        print("❌ Email inválido")
        return

    domain = email.split("@")[1]

    print(f"Email: {email}")
    print(f"Domínio: {domain}")
    print(f"TLD: {domain.split('.')[-1]}")

    print("\n🌐 DNS Records")

    # MX
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        print("\n📨 MX Records (servidores de email):")
        for r in mx_records:
            print(" -", r.exchange)
    except:
        print("MX não encontrado")

    # NS
    try:
        ns_records = dns.resolver.resolve(domain, 'NS')
        print("\n🧭 Nameservers:")
        for r in ns_records:
            print(" -", r)
    except:
        print("NS não encontrado")

    # A
    try:
        a_records = dns.resolver.resolve(domain, 'A')
        print("\n🌍 IPs do domínio:")
        for r in a_records:
            print(" -", r)
    except:
        print("IP não encontrado")

    # TXT
    try:
        txt_records = dns.resolver.resolve(domain, 'TXT')
        print("\n📄 TXT Records:")
        for r in txt_records:
            print(" -", r)
    except:
        print("TXT não encontrado")
