import re
import dns.resolver

def email_lookup():

    email = input("Digite o email: ")

    print("\nVerificação de Email")

    pattern = r"[^@]+@[^@]+\.[^@]+"

    if re.match(pattern, email):
        print("Formato válido")
    else:
        print("Email inválido")

    domain = email.split("@")[-1]

    print("Domínio:", domain)

    try:

        records = dns.resolver.resolve(domain, "MX")

        print("\nServidores MX")

        for r in records:
            print(r)

    except:

        print("Não foi possível consultar MX")
