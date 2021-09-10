import re


def check_mail(log: dict, text: str):
    pattern = r'(?P<name>[A-Za-z]{5,})(?:@)(?P<domain>[a-z]{3,}\.(?:com|org|bg))$'
    match = re.finditer(pattern, text)
    for element in match:
        el = element.groupdict()
        if el['domain'] not in log.keys():
            log[el['domain']] = []
        if el['name'] not in log[el['domain']]:
            log[el['domain']].append(el['name'])


emails = {}
for _ in range(int(input())):
    mail = input()
    check_mail(emails, mail)

for i, j in sorted(emails.items(), key=lambda x: -len(x[1])):
    print(f'{i}:')
    [print(f'### {user}') for user in j]
