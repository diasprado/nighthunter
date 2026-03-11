from modules.ip_lookup import ip_lookup
from modules.email_lookup import email_lookup
from modules.domain_lookup import domain_lookup

def banner():
    print("""
███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗
████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝
██╔██╗ ██║██║██║  ███╗███████║   ██║
██║╚██╗██║██║██║   ██║██╔══██║   ██║
██║ ╚████║██║╚██████╔╝██║  ██║   ██║
╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝

NIGHTHUNTER
Advanced OSINT Recon Framework
""")

def menu():

    print("""
1 - Username Scan
2 - IP Lookup
3 - Email Lookup
4 - Domain Lookup
0 - Sair
""")

    escolha = input("Escolha uma opção: ")

    if escolha == "2":
        ip_lookup()

    elif escolha == "3":
        email_lookup()

    elif escolha == "4":
        domain_lookup()

    elif escolha == "0":
        print("Saindo...")

    else:
        print("Opção inválida")

banner()
menu()
