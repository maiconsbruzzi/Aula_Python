#!/usr/bin/python

import whois

target = "google.com.br"


def func_whois(_domain):
    querywhois = whois.query(target)
    print("[+] - Nome do domínio:", querywhois.name)
    print("[+] - Data de criação:", querywhois.creation_date)
    print("[+] - Data de expiração:", querywhois.expiration_date)
    print("[+] - Data da ultima atualização:", querywhois.last_updated)
    print("[+] - Servidor Whois registrado:", querywhois.registrar)

    for _domain in querywhois.name_servers:
        print(_domain)

func_whois(target)
