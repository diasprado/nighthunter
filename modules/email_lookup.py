def lookup_email(email):

    print("\n📧 Email Information")

    if "@" in email:
        dominio = email.split("@")[1]
        print("Email:", email)
        print("Domínio:", dominio)

    else:
        print("Email inválido")
