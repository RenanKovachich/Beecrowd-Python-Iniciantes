def main():
    lines = []
    while True:
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break

    a = int(lines[0])
    count = -1
    aux = None

    for i in range(a + 1):
        if lines[i] != aux:
            aux = lines[i]
            count += 1

    print(count)

if __name__ == "__main__":
    main()
