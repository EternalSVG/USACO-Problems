def main():
    
    # Variable to read the board count.
    N = int(input())

    total = [0] * 26

    for i in range(N):
        word1, word2 = input().split()

        count1 = [0] * 26
        count2 = [0] * 26

        for letter in word1:
            index = ord(letter) - ord('a')
            count1[index] += 1
        
        for letter in word2:
            index = ord(letter) - ord('a')
            count2[index] += 1
        
        for j in range(26):
            total[j] += max(count1[j], count2[j])
    
    for k in range(26):
        print(total[k])

if __name__ == "__main__":
    main()