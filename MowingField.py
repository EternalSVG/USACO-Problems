n = int(input())

x, y = 0, 0

time = 0
visited = {(0, 0): 0}

answer = float('inf')

for _ in range(n):
    direction, steps = input().split()
    steps = int(steps)

    for _ in range(steps):
        if direction == 'N':
            y += 1
        elif direction == 'S':
            y -= 1
        elif direction == 'E':
            x += 1
        else:  
            x -= 1

        time += 1

        if (x, y) in visited:
            gap = time - visited[(x, y)]
            answer = min(answer, gap)

        visited[(x, y)] = time

if answer == float('inf'):
    print(-1)
else:
    print(answer)