import sys, random

def rev_comp(seq):
    '''seq is a string of DNA nucleotides'''
    rev = ''
    seq = seq[::-1] #reverses the sequence
    d = {'A':'T','T':'A','G':'C','C':'G','Y':'R','R':'Y','K':'M','M':'K','D':'H','H':'D','V':'B','B':'V'}
    for char in seq:
        if char in d:
            rev += d[char]
        else:
            rev += char   
    return rev

def main():
    try:
        inFile, outFile, readLen, depth = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
    except:
        print('Use with 4 arguments:\n\tInput fasta file name\n\tOutput fasta file name\n\tRead length\n\tRead depth')
        return

    #inFile, outFile, readLen, depth = 'chr2_CM000463.1_1000000-1100000.fasta', 'testOutput.fasta', 100, 10

    seq = ''
    with open(inFile, 'r') as f:
        for line in f:
            if line[0] != '>':
                seq += line.strip('\n')
        f.close()
    seqLength = len(seq)
    revseq = rev_comp(seq)
    numReads = int((depth * seqLength) / readLen)

    print('Number of reads:', numReads)
    qual = ''
    for i in range(readLen):
        qual += 'I'

    rev, norm = 0, 0
    with open(outFile, 'w') as f:
        for i in range(numReads):
            startIndex = random.randint(0, (seqLength - readLen))
            if random.randint(1,2) == 1: #reverse compliment
                tempSeq = revseq[startIndex:startIndex + readLen]
                f.write('@Read ' + str(i) + '\n' + tempSeq + '\n+\n' + qual + '\n')
                rev +=1
            else: #normal strand
                tempSeq = seq[startIndex:startIndex + readLen]
                f.write('@Read ' + str(i) + '\n' + tempSeq + '\n+\n' + qual + '\n')
                norm += 1
        f.close()
    print(outFile, 'created!')
    #print(rev, norm)

main()
