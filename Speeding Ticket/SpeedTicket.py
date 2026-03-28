def main():
    N, M = map(int, input().split())

    limit = [0] * 100
    speed = [0] * 100

    pos = 0
    for i in range(N):
        length, lim = map(int, input().split())
        for j in range(length):
            limit[pos] = lim
            pos += 1

    pos = 0
    for i in range(M):
        length, spd = map(int, input().split())
        for j in range(length):
            speed[pos] = spd
            pos += 1
    
    maxOver = 0
    for i in range(100):
        maxOver = max(maxOver, speed[i] - limit[i])

    print(maxOver)


if __name__ == "__main__":
    main()
