
t = input().strip()
k = int(input())
fq = {}
for i in range(len(t)-k+1):
    kmer=t[i:i+k]
    fq[kmer] = fq.get(kmer,0) + 1
    
    
m_c = max(fq.values())
     
          
seen = set()
for i in range(len(t)-k+1):
                    kmer = t[i:i+k]
                    if fq[kmer] == m_c and kmer not in seen:
                
                        print(kmer, end=" ")
                        seen.add(kmer)
            
