#!/usr/bin/python

import time
import shodan
shodan_mykey='OygcaGSSq46Lg5fZiADAuFxl4OBbn7zm'
shodan_api = shodan.Shodan(shodan_mykey)
shodan_target='179.191.78.194'
shodan_host = shodan_api.host(shodan_target)

def shodan_info():
    print('[*] - Informacoes genericas do ALVO')
    print('IP alvo:', shodan_host['ip_str'])
    print('Orgionizacao:', shodan_host.get('org', 'n/a'))
    print('Sistema Operacional:', shodan_host.get('os', 'n/a'))
    print("-" * 60)

def shodan_portscan():
    print('[*] - Identificacao de portas abertas')

    for _line in shodan_host['data']:
        print("[+] - Porta Aberta", _line['port'])
        print("[+] - Banner:", _line['data'])
        print("-" * 60)


def shodan_vuln():
    print ('[*] - Lista de possiveis Vulnerabilidades:')

    for item in shodan_host['vulns']:
        time.sleep(0.5)
        CVE = item.replace('!','')
        print('Vulnerability', item)
        
        exploits = shodan_api.exploits.search(CVE)
        
        for item in exploits['matches']:
            try:
                if item.get('cve')[0] == CVE:
                    print('[++] - Vulnerabilidade / CVE', item.get('description'))
                    print(item.get('description'))
                    print()
            except:
                print('[!] - Descricao nao disponivel')





print("-" * 60)
print("-" * 60)
shodan_info()
print("-" * 60)
shodan_portscan()
print("-" * 60)
shodan_vuln()
print("-" * 60)