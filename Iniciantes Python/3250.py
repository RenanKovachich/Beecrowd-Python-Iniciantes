from collections import deque

def find_button_presses(f, s, g, u, d):
    visited = [False] * (f + 1)
    queue = deque([(s, 0)])

    while queue:
        current_floor, presses = queue.popleft()

        if current_floor == g:
            return presses

        up_floor = current_floor + u
        down_floor = current_floor - d

        if up_floor <= f and not visited[up_floor]:
            visited[up_floor] = True
            queue.append((up_floor, presses + 1))

        if down_floor >= 1 and not visited[down_floor]:
            visited[down_floor] = True
            queue.append((down_floor, presses + 1))

    return "use the stairs"

f, s, g, u, d = map(int, input().split())

result = find_button_presses(f, s, g, u, d)
print(result)
