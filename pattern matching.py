# Using Naive Algorithm for Pattern Searching
def naive_search(pat, txt):
    M = len(pat)
    N = len(txt)
    for i in range(N - M + 1):
        j = 0
        while(j < M):
            if (txt[i + j] != pat[j]):break
            j += 1
    
        if (j == M):
            print("Pattern found at index ", i)

def standard_search(sub, txt: str):    #Using Std searching
    if sub in txt:
        indx = txt.find(sub)
        while indx != -1:
            print('Match found at index:', indx)
            indx = txt.find(sub, indx+1)

txt = "AABAACAADAABAAABAA"
pat = "AABA"
# Function call
naive_search(pat, txt)
print()
print()
standard_search(pat, txt)
print("Coded By Durani Mohammed Zaeem; Roll no: 425")