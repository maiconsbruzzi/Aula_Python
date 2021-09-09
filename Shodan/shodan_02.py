#!/usr/bin/python

import shodan
shodan_mykey='OygcaGSSq46Lg5fZiADAuFxl4OBbn7zm'
shodan_api = shodan.Shodan(shodan_mykey)
shodan_target='179.191.78.194'
shodan_host = shodan_api.host(shodan_target)


def shodan_info():
    print('IP alvo:', shodan_host['ip_str'])
    print('Orgenizacao:', shodan_host.get('org', 'n/a'))
    print('Sistema Operacional:', shodan_host.get('os', 'n/a'))

shodan_info()