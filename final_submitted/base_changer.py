import sys, random

def main():
    try:
              
        inFile, outFile = sys.argv[1], sys.argv[2]
        try:
            errorRate = float(sys.argv[3])
        except: #sets default error rate
            errorRate = 0.0001
    except:
        print('Use with 3 arguments:\n\tInput fasta file name\n\tOutput errored fasta file name\n\tError Rate (default at 0.0001)\n')
        return

#inFile, outFile,errorRate = 'chr2_CM000463.1_1000000-1100000.fasta', 'errorFasta.fasta', 0.0001

    seq = ''

    with open(inFile, 'r') as f:
        for line in f:
            if line[0] == '>':            
                header = line
            else:            
                seq += line.strip('\n')
        f.close()

    for nuc in seq:
        if random.random() <= errorRate:
            temp = nuc
            while temp == nuc:
                nuc = random.choice('ATCG')
    seqList = []
    while seq:
        seqList.append(seq[:100])
        seq = seq[100:]

    with open(outFile, 'w') as f:
        f.write(header)
        for j in seqList:
            f.write(j + '\n')
        f.close()
    print(outFile, 'created!')
main()
