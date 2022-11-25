import dns.resolver
name = 'iana.org'
for qtype in 'A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA':
    answer = dns.resolver.resolve(name, qtype, raise_on_no_answer=False)
    if answer.rrset is not None:
        print(answer.rrset)