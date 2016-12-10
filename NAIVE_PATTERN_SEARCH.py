def search(pat,txt):
    M=len(pat)
    N=len(txt)
    for i in range(N-M+1):
        for j in range(M):
            if txt[i+j] != pat[j]:
                break
            if j == M-1:
                print("The pattern is found at",i)
txt="AABAACAADAABAAABAA"
pat="AABA"
search (pat, txt)
