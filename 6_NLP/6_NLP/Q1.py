import re 

first_pattern = re.compile(r'a[a-z]*$')
test_string = "apple pen Apple pEn"
expressions = test_string.split()
for expr in expressions:
    if first_pattern.match(expr):
        print(f'Match: {expr}')
    else:
        print(f'No match: {expr}')



second_pattern = re.compile(r'([a-z]|[A-Z])*[0-9]$')
test_string = "anDrewng01 Andrewng02 Hello01"
expressions = test_string.split()
for expr in expressions:
    if second_pattern.match(expr):
        print(f'Match: {expr}')
    else:
        print(f'No match: {expr}')