
t = input().strip()
k, d = map(int, input().split())

def hamming(a, b):
    c = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            c += 1
    return c

patterns = []

def generate(crnt):
    if len(crnt) == k:
        patterns.append(crnt)
        return

    generate(crnt + "A")
    generate(crnt + "C")
    generate(crnt + "G")
    generate(crnt + "T")

generate("")

fq = {}

for pattern in patterns:
    c = 0

    for i in range(len(t) - k + 1):
        kmer = t[i:i+k]

        if hamming(pattern, kmer) <= d:
            c += 1

    fq[pattern] = c

max_c = max(fq.values())

for pattern in fq:
    if fq[pattern] == max_c:
        print(pattern, end=" ")
