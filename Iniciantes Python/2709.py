import math


def is_prime(num):
    raiz = int(math.sqrt(num))
    if num != 2 and num % 2 == 0 or num == 1:
        return False
    for i in range(3, raiz + 1, 2):
        if num % i == 0:
            return False
    return True


while True:
    try:
        n = int(input())
    except EOFError:
        break

    vet = [int(input()) for i in range(n)]
    s = int(input())

    ans = sum(vet[i] for i in range(n - 1, -1, -s))
    print("You’re a coastal aircraft, Robbie, a large silver aircraft." if is_prime(ans) else "Bad boy! I’ll hit you.")
