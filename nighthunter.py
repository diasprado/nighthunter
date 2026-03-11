import requests
import json
import os
import re

from modules.ip_lookup import lookup_ip
from modules.email_lookup import lookup_email
from modules.domain_lookup import lookup_domain


def banner():
    print("""
███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ 
████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
██╔██╗ ██║██║██║  ███╗███████║   ██║   ███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
██║╚██╗██║██║██║   ██║██╔══██║   ██║   ██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
██║ ╚████║██║╚██████╔╝██║  ██║   ██║   ██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

NIGHTHUNTER v3 - OSINT Framework
""")


def scan_username(username):

    print(f"\n🔎 Procurando username: {username}\n")

    with open("sites.txt", "r") as f:
        sites = f.read().splitlines()

    resultados = []

    for site in sites:

        url = site.replace("{}", username)

        try:

            r = requests.get(url, timeout=5)

            if r.status_code == 200:
                print(f"✔ Encontrado: {url}")
                resultados.append(url)

        except:
            pass

    with open("resultado.json", "w") as file:
        json.dump(resultados, file, indent=4)

    print("\nScan finalizado.")
    print("Resultados salvos em resultado.json")


try:
    import dns.resolver
except ImportError:
    dns = None

def lookup_email(email):

    print(f"\n🔎 Iniciando scan para: {email}\n")

    if "@" not in email:
        print("[!] Email inválido")
        return

    username, domain = email.split("@")

    print(f"[✔] Username: {username}")
    print(f"[✔] Domain: {domain}\n")

    if dns:
        try:
            answers = dns.resolver.resolve(domain, 'MX')
            print(f"[✔] Servidor de email encontrado: {answers[0].exchange}")
        except Exception:
            print("[!] Não foi possível encontrar servidor de email (MX Record)")
    else:
        print("[!] dnspython não instalado, MX Record não verificado")

    print("\n[+] Possíveis perfis sociais:")

    socials = [
        f"https://twitter.com/{username}",
        f"https://instagram.com/{username}",
        f"https://github.com/{username}",
        f"https://linkedin.com/in/{username}",
        f"https://facebook.com/{username}"
    ]

    for s in socials:
        print(f"  {s}")

    print("\n[+] Checando vazamentos conhecidos (simulado)...")
    print("  Nenhum vazamento encontrado (simulação)\n")

    print("[+] Scan de email finalizado.\n")


def menu():

    banner()

    print("""
1 - Scan Username
2 - Lookup IP
3 - Lookup Email
4 - Lookup Domain
0 - Sair
""")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        username = input("Username: ")
        scan_username(username)

    elif escolha == "2":
        ip = input("IP: ")
        lookup_ip(ip)

    elif escolha == "3":
        email = input("Email: ")
        lookup_email(email)

    elif escolha == "4":
        domain = input("Domínio: ")
        lookup_domain(domain)

    elif escolha == "0":
        exit()

    else:
        print("Opção inválida")


menu()
