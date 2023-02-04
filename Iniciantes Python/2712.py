WEEKDAYS = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]


def verifica_placa(placa):
    if len(placa) != 8:
        return False
    if placa[3] != '-':
        return False
    first_three_chars = placa[:3]
    if not all(c.isalpha() and c.isupper() for c in first_three_chars):
        return False
    if not all(c.isdigit() for c in placa[4:]):
        return False
    return True


def rodizio(placa):
    last_char = placa[-1]
    if last_char in '12':
        return 0
    elif last_char in '34':
        return 1
    elif last_char in '56':
        return 2
    elif last_char in '78':
        return 3
    elif last_char in '90':
        return 4


num_cases = int(input().strip())
for _ in range(num_cases):
    placa = input().strip()
    if verifica_placa(placa):
        print(WEEKDAYS[rodizio(placa)])
    else:
        print("FAILURE")
