class fastq:
    def __init__(self, fileName):
        '''fastq class; argument is the file name with file extention. Separates each read into the 2D list called reads'''        
        reads,lines = [], []                 
        with open(fileName, 'r') as f:
            for line in f:
                lines.append(line)
            f.close()
        while lines:
            reads.append(lines[:4])
            lines = lines[4:]    
        self.reads = reads        

    def sep_barcodes(self):
        '''separates a fastq file into separate fastq files based on the barcode that is the first 10 bases in each read'''
        import os
        path = 'separated_fastqs'
        if not os.path.isdir(path):
            os.mkdir(path)
        os.chdir(path)
        reads = self.reads
        for read in reads:
            tempBarcode = read[1][0:10]
            with open(tempBarcode + '.fq', 'a') as f:
                f.write(read[0]+ read[1][10:]+read[2]+read[3][10:])
            f.close()
        os.chdir('..')
        print('Separated fastqs created in the separated_fastqs directory!')
        
a = fastq('week3_seqs_bc.fq')
a.sep_barcodes()