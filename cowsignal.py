import os

def main():
    fin = open("cowsignal.in", "r")
    fout = open("cowsignal.out", "w")

    M, N, K = map(int, fin.readline().split())

    for i in range(M):
        row = fin.readline().rstrip("\n")
        expanded = ""

        for c in row:
            expanded += c * K

        for j in range(K):
            fout.write(expanded + "\n")

    fin.close()
    fout.close()

if __name__ == "__main__":
    main()
