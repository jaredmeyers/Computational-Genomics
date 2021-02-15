import re, sys

def main():
    try:
        filename, n , size = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    except:
        print('Use with 3 arguments:\n\tInput fasta name\n\tN value (ex. 50 for N50)\n\tGenome size in bp')
        return
    
    threshold = (n/100) * size
    with open(filename, 'r') as f:    
        fasta = f.read()
        contigs = re.split('>.*\n', fasta)
        editcontigs = []
        for contig in contigs:
            contig = re.sub('\n','', contig)
            editcontigs.append(contig)
        editcontigs = editcontigs[1:] #gets rid of the empty first thing in list
        contig_lens = []
        for i in editcontigs:
            contig_lens.append(len(i))
        
        contig_lens = sorted(contig_lens, reverse = True)
        
        score, i = 0, 0
        while score < threshold:
            try:
                final = contig_lens[i]
                score += final                
                i += 1
            except:
                print('Score not existant')
                return
                
        print(f'N{n}: {final}')
main()           