import sys, random

def main():
    try:
        errorRate= float(sys.argv[1])
    except:
        print('Use with 1 arguments:\n\tError Rate')
        return              
    fasta = sys.stdin.read().strip('\n')
    lineList = fasta.split('\n')    
    seq = ''       
    for line in lineList:
        if line[0] == '>':            
            header = line + '\n'
        else:            
            seq += line
        
    newSeq = ''
    for nuc in seq:
        if random.random() <= errorRate:
            temp = nuc
            newNuc = random.choice('ATCG')
            while temp == newNuc:
                newNuc = random.choice('ATCG')
            newSeq += newNuc
        else:
            newSeq += nuc
    seqList = []
    while newSeq:
        seqList.append(newSeq[:100])
        newSeq = newSeq[100:]
    
    sys.stdout.write(header)
    for i in seqList:

        sys.stdout.write(i + '\n')
    sys.stdout.flush()
main()