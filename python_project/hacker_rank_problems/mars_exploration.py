#https://www.hackerrank.com/challenges/mars-exploration/problem?h_r=internal-search
def mars_exploration():
    S = input().strip()
    count = 0
    signal = ['S', 'O', 'S']
    for i in range(len(S)):
        if S[i] != signal[i % 3]:
            count += 1
    print(count)
mars_exploration()
