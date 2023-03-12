""" Longest Common Subsequence """
def lcs(str1, str2):
    match = set(str1).intersection(str2)
    return ''.join(sorted(match))

print("Longest Common Subsequence is:", lcs('ABACDFG','DAZGECSF'))
print('Coded By: Durani Mohammed Zaeem, Roll no: 429')