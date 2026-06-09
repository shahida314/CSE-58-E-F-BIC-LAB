

dna = input().strip()

c = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

r = ""

for ch in dna:
    r += c[ch]

print(r[::-1])
