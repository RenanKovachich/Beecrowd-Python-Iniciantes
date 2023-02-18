import re

body = False

while True:
    try:
        texto = input()

        if re.search("<body>", texto):
            body = True
            continue

        if body and re.search("</body>", texto):
            body = False

        if body:
            print(texto)
    except EOFError:
        break
        