#!/usr/bin/python3

import dns.resolver
myquery = dns.resolver.Resolver()
target = "google.com.br"

def func_ns(_target):
    question = myquery.query(_target, "NS")

    for _ns in question:
        print(_ns)

func_ns(target)