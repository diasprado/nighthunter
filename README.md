![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.x-blue)
![OSINT](https://img.shields.io/badge/type-OSINT-red)

# NIGHTHUNTER v4
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.x-blue)
![OSINT](https://img.shields.io/badge/type-OSINT-red)
![Version](https://img.shields.io/badge/version-4.0-orange)
![Platform](https://img.shields.io/badge/platform-Linux-lightgrey)
![Status](https://img.shields.io/badge/status-active-success)



Advanced OSINT Recon Framework

NIGHTHUNTER é uma ferramenta OSINT desenvolvida em Python para coleta de informações públicas da internet.

O objetivo do projeto é auxiliar pesquisas OSINT, análise de presença digital e investigações educacionais de perfis públicos online.

---

# Funcionalidades

• Scan de usernames em múltiplos sites
• OSINT de email
• OSINT de domínio
• OSINT de IP
• Scanner rápido com múltiplas requisições
• Estatísticas de resultados
• Exportação de relatórios
• Relatórios em JSON e HTML
• Sistema de plugins
• Ferramenta OSINT open-source

---

# Estrutura do Projeto

nighthunter
│
├── core
│   ├── scanner.py
│   ├── osint_email.py
│   ├── osint_ip.py
│   ├── osint_domain.py
│
├── plugins
│   └── plugin_example.py
│
├── reports
│   ├── report.html
│   └── results.json
│
├── data
│   └── sites.txt
│
├── nighthunter.py
├── requirements.txt
└── README.md

---

# Instalação

Clone o repositório

git clone https://github.com/diasprado/nighthunter.git

Entre na pasta do projeto

cd nighthunter

Instale as dependências

pip install -r requirements.txt

---

# Uso

Execute a ferramenta

python3 nighthunter.py

Digite o username alvo

Digite o username alvo ➤ dias

Exemplo de saída

Scanning...

User encontrado em:
https://github.com/"nome"
https://twitter.com/"nome"
https://reddit.com/user/"nome"

---

# Relatórios

Após o scan o NIGHTHUNTER pode gerar relatórios:

reports/results.json
reports/report.html

Esses relatórios podem ser utilizados para documentação de investigações OSINT.

---

# Roadmap

Próximas melhorias planejadas

• Scan em 1000+ sites
• Multithreading para scans mais rápidos
• Integração com APIs OSINT
• Modo TOR para anonimização
• Dashboard web
• Sistema avançado de plugins
• Geolocalização de IP
• Integração com bases de dados públicas

---

# Contribuição

Contribuições são bem-vindas.

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas alterações
4. Faça um Pull Request

---

# Aviso

Esta ferramenta foi desenvolvida apenas para fins educacionais e pesquisa OSINT.

Não utilize para:

• invasão de privacidade
• perseguição online
• atividades ilegais

O autor não se responsabiliza pelo uso indevido da ferramenta.

---

# Licença

Este projeto está licenciado sob a MIT License.
